from django import forms
from django.contrib import admin
from .models import Patient, DropdownOption

# Custom form for PatientAdmin
class PatientAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter each dropdown by field_name
        self.fields['relation'].queryset = DropdownOption.objects.filter(field_name='relation')
        self.fields['occupation'].queryset = DropdownOption.objects.filter(field_name='occupation')
        self.fields['service'].queryset = DropdownOption.objects.filter(field_name='service')
        self.fields['blood_group'].queryset = DropdownOption.objects.filter(field_name='blood_group')
        self.fields['identity_type'].queryset = DropdownOption.objects.filter(field_name='identity_type')
        self.fields['insurance_provider'].queryset = DropdownOption.objects.filter(field_name='insurance_provider')
        self.fields['state'].queryset = DropdownOption.objects.filter(field_name='state')
        self.fields['referred_by'].queryset = DropdownOption.objects.filter(field_name='referred_by')

# Register PatientAdmin with custom form
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = ('uhid', 'registration_no', 'relation', 'occupation', 'blood_group', 'created_at')
    list_filter = ('relation', 'occupation', 'blood_group', 'service', 'insurance_provider', 'state', 'referred_by')
    search_fields = ('uhid', 'registration_no', 'relation_name', 'mobile_no', 'identity_no', 'insurance_no', 'referred_doctor')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
admin.site.register(DropdownOption)