from django.shortcuts import render
from .models import UserDetails, State, Country, District, City
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import UserDetailsForm
# Create your views here.
class DetailView(ListView):
    model = UserDetails
    queryset = UserDetails.objects.all().order_by('name')
    context_object_name = 'UserDetail'

class UserDetailCreateView(CreateView):
    model = UserDetails
    form_class = UserDetailsForm
    success_url = reverse_lazy('detail')

class UserDetailUpdateView(UpdateView):
    model = UserDetails
    form_class = UserDetailsForm
    success_url = reverse_lazy('detail')

def load_state(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country=country_id).order_by('name')
    return render(request,'userdetails/state_dropdown_options.html',{'states':states})


def load_district(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state=state_id).order_by('name')
    return render(request,'userdetails/district_dropdown_options.html',{'districts':districts})


def load_cities(request):
    district_id = request.GET.get('district')
    cities = City.objects.filter(district=district_id).order_by('name')
    return render(request,'userdetails/city_dropdown_options.html',{'cities':cities})