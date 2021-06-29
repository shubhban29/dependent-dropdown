from django import forms
from .models import UserDetails, State, District, City, Country

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('name','country','state','district','city')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.all().order_by('name')
        self.fields['state'].queryset = State.objects.none()
        self.fields['district'].queryset = District.objects.none()
        self.fields['city'].queryset = City.objects.none()
        print(self.data)

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['district'].queryset = District.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.state.district_set.order_by('name')
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')