from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class DropdownOption(models.Model):
    FIELD_CHOICES = [
        ('blood_group', 'Blood Group'),
        ('relation', 'Relation'),
        ('occupation', 'Occupation'),
        ('service', 'Service'),
        ('identity_type', 'Identity Type'),
        ('insurance_provider', 'Insurance Provider'),
        ('state', 'State'),
        ('referred_doctor', 'Referred Doctor'),
        ('nationality', 'nationality'),
    ]

    field_name = models.CharField(max_length=50, choices=FIELD_CHOICES)
    value = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.value
class Patient(models.Model):
    uhid = models.CharField(max_length=50, unique=True)
    registration_no = models.CharField(max_length=50, unique=True)

    relation = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='relation_options',limit_choices_to={'field_name': 'relation'})
    relation_name = models.CharField(max_length=100, blank=True)

    address = models.TextField(blank=True)
    mobile_no = models.CharField(max_length=15)

    occupation = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='occupation_options', limit_choices_to={'field_name': 'occupation'})
    service = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='service_options', limit_choices_to={'field_name': 'service'})

    nationality = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='nationality_options', limit_choices_to={'field_name': 'nationality'})
    date_of_birth = models.DateField(null=True, blank=True)

    blood_group = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='blood_group_options', limit_choices_to={'field_name': 'blood_group'}  )
    identity_type = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='identity_type_options',limit_choices_to={'field_name': 'identity_type'})
    identity_no = models.CharField(max_length=100, blank=True)

    insurance_provider = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='insurance_provider_options',limit_choices_to={'field_name': 'insurance_provider'})
    insurance_no = models.CharField(max_length=100, blank=True)

    city = models.CharField(max_length=100, blank=True)
    state = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='state_options',limit_choices_to={'field_name': 'state'} )
    pin_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, default="India")

    photo = models.ImageField(upload_to='patients/photos/', blank=True, null=True)
    biometric = models.ImageField(upload_to='patients/biometric/', blank=True, null=True)

    REFERRED_BY_CHOICES = (
        ('internal', 'Internal'),
        ('external', 'External'),
    )
    referred_by = models.CharField(max_length=10, choices=REFERRED_BY_CHOICES)
    referred_doctor = models.ForeignKey('DropdownOption', on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_doctor_options',limit_choices_to={'field_name': 'referred_doctor'})
    referred_mobile_no = models.CharField(max_length=15, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.uhid} - {self.registration_no}"
