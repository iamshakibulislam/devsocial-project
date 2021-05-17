from django.shortcuts import render
from dashboard.models import *
from django.db.models import Q

def preprint_search(request):

	if request.method == 'POST':
		keyword = request.POST['keyword']

		search_result=PreprintDetails.objects.filter(Q(approved=True),Q(title__icontains=keyword) | Q(keywords__icontains=keyword))

		return render(request,'search.html',{'results':search_result})



def search_by_topic(request,topic):

	search_result=PreprintDetails.objects.filter(Q(approved=True),Q(title__icontains=topic) | Q(keywords__icontains=topic) | Q(selected_main_taxonomy__icontains=topic))

	return render(request,'search.html',{'results':search_result})




