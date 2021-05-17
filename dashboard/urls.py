from django.urls import path
from . import views

urlpatterns = [
    path('add_preprint/', views.add_preprint ,name='add_preprint'),
    path('my_preprints/',views.my_preprints,name='my_preprints')
    
    ]