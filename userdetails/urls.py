from django.urls import include, path

from .views import DetailView, UserDetailCreateView, UserDetailUpdateView, load_cities, load_state, load_district

urlpatterns =[
    path('details/',DetailView.as_view(),name='detail'),
    path('',UserDetailCreateView.as_view(),name='add'),
    path('update/<int:pk>',UserDetailUpdateView.as_view(),name='update'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path('ajax/load-states/', load_state, name='ajax_load_states'),
    path('ajax/load-districts/', load_district, name='ajax_load_districts'),
]