from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DropdownOption
from .serializers import DropdownOptionSerializer,LoginSerializer, RegisterSerializer
from .permissions import IsStaffAndSuperUser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth import  authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class DropdownOptionViewSet(viewsets.ModelViewSet):
    queryset = DropdownOption.objects.all()
    serializer_class = DropdownOptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffAndSuperUser]

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated, IsStaffAndSuperUser])
    def get_dropdowns(self, request):
        """
        Return dropdowns grouped by field_name for frontend
        """
        data = {}
        for field, _ in DropdownOption.FIELD_CHOICES:
            options = DropdownOption.objects.filter(field_name=field)
            data[field] = [opt.value for opt in options]
        return Response(data)

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.is_staff and user.is_superuser:
            # Admin user: return all patients
            return Patient.objects.all().order_by('-created_at')
        else:
            # Normal user: return only patients submitted by this user
            return Patient.objects.filter(submitted_by=user).order_by('-created_at')
    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)
User = get_user_model()
class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    authentication_classes = []   # disable session/auth
    permission_classes = [AllowAny]  # anyone can access

    # POST /api/login/
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # authenticate uses username internally
        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            # Determine role
            if user.is_superuser or user.is_staff:
                role = "admin"
            else:
                role = "user"

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': role,
                }
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Required for ModelViewSet
    serializer_class = RegisterSerializer
    permission_classes = permission_classes = [permissions.AllowAny ]  # Allow public access to register
    http_method_names = ['post'] 