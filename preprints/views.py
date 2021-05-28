from django.shortcuts import render
from dashboard.models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect


def preprint_search(request):

	if request.method == 'GET':
		page = request.GET.get('page', 1)
		keyword = request.GET.get('keyword','')

		search_result=PreprintDetails.objects.filter(Q(approved=True),Q(title__icontains=keyword) | Q(keywords__icontains=keyword)).order_by('-id')


		for x in search_result:
			get_tags = str(x.keywords)
			splitit=get_tags.split(',')
			x.keywords=splitit

		paginator = Paginator(search_result, 7)
		try:
			results = paginator.page(page)
		except PageNotAnInteger:
			results = paginator.page(1)
		except EmptyPage:
			results = paginator.page(paginator.num_pages)


		return render(request,'search.html',{'results':results,'keyword':keyword})



def search_by_topic(request,topic):
	page = request.GET.get('page', 1)
	
	keyword = request.GET.get('keyword','#####')


	search_result=PreprintDetails.objects.filter(Q(approved=True),Q(title__icontains=topic) | Q(keywords__icontains=topic) | Q(selected_main_taxonomy__icontains=topic) | Q(title__icontains=keyword))
	for x in search_result:
		get_tags = str(x.keywords)
		splitit=get_tags.split(',')
		x.keywords=splitit
	paginator = Paginator(search_result, 7)

	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
	return render(request,'search.html',{'results':results,'keyword':topic})





def preprint_details(request,pk):
	sel_preprint=PreprintDetails.objects.get(id=pk)

	get_tags = str(sel_preprint.keywords)
	splitit=get_tags.split(',')
	sel_preprint.keywords=splitit
	try:
		pub_data_len = len(sel_preprint.public_data_link)
	except:
		pub_data_len = 0

	try:
		pub_data_describe_len = len(sel_preprint.public_data_not_available_describe)
	except:
		pub_data_describe_len = 0

	try:
		type_data_len = len(sel_preprint.type_available_link)
	except:
		type_data_len = 0

	try:
		type_data_describe_len = len(sel_preprint.type_not_availabe_description)
	except:
		type_data_describe_len = 0

	try:
		d_count = Downloads.objects.get(preprint=sel_preprint).counter

	except:
		d_count = 0


	return render(request,'preprint-details.html',{'preprint':sel_preprint,'pubdata_len':pub_data_len,'pubdata_desc':pub_data_describe_len,'type_data_len':type_data_len,'type_data_describe_len':type_data_describe_len,'downloaded':d_count})




def downloads(request,pk):
	sel= PreprintDetails.objects.get(id=pk)
	try:
		down = Downloads.objects.get(preprint=sel)
		down.counter = down.counter + 1
		down.save()
	except:
		Downloads.objects.create(preprint=sel,counter=0)

	downurl = sel.file.url 

	return HttpResponseRedirect(downurl)

