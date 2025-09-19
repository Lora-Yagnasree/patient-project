from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import PatientViewSet, DropdownOptionViewSet, LoginViewSet, RegisterViewSet # your viewsets

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'dropdowns', DropdownOptionViewSet)
router.register(r'login', LoginViewSet, basename='login')
router.register(r'signup', RegisterViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls)),

    # DRF login/logout for browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
