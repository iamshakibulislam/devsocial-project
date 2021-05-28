from django.urls import path
from . import views
from django.views.generic import TemplateView
from dashboard.models import *

urlpatterns = [
		
		path('preprint-search/',views.preprint_search,name='preprint_search'),
		path('preprint_search/',TemplateView.as_view(template_name='search.html'),name='preprint_query_page'),
		path('search_by_topic/<str:topic>/',views.search_by_topic,name='search_by_topic'),
		path('preprint-details/<int:pk>/',views.preprint_details,name='preprint_details'),
		path('downloads/<int:pk>/',views.downloads,name='downloads')
   ]