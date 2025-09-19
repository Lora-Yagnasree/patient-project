
from rest_framework import serializers
from .models import DropdownOption, Patient
from django.contrib.auth.models import User
# app3monkeys/serializers.py
class DropdownOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownOption
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    referred_by = serializers.ChoiceField(
        choices=Patient.REFERRED_BY_CHOICES,
        style={'base_template': 'radio.html'}  # renders radio buttons in DRF browsable API
    )
    class Meta:
        model = Patient
        fields = [
            "uhid",
            "registration_no",
            "relation",
            "relation_name",
            "address",
            "mobile_no",
            "occupation",
            "service",
            "nationality",
            "date_of_birth",
            "blood_group",
            "identity_type",
            "identity_no",
            "insurance_provider",
            "insurance_no",
            "city",
            "state",
            "pin_code",
            "country",
            "photo",
            "biometric",
            "referred_by",
            "referred_doctor",
            "referred_mobile_no",
            "created_at"
        ]

    # Keep your validators as you already have
    def validate_mobile_no(self, value):
        import re
        if not re.match(r'^[6-9]\d{9}$', value):
            raise serializers.ValidationError("Invalid mobile number (must be 10 digits starting 6-9).")
        return value

    def validate_pin_code(self, value):
        import re
        if value and not re.match(r'^\d{6}$', value):
            raise serializers.ValidationError("Invalid Pin Code (6 digits required).")
        return value

    def validate_date_of_birth(self, value):
        from datetime import date
        if value and value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)