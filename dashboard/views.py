from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
@login_required(login_url='/accounts/login/')
def add_preprint(request):

	if request.method == 'GET':
		return render(request,'add-preprint.html')

	if request.method == 'POST':
		service = request.POST.get('service','')
		file = request.FILES['file']
		title = request.POST.get('title','')
		public_data_link = request.POST.get('available-data-link','')
		public_data_not_available_describe = request.POST.get('not-available-describe','')
		type_available_link = request.POST.get('link','')
		type_available_link_type = request.POST.get('type','')
		type_not_availabe_description = request.POST.get('not-available-type-description','')
		license_type=request.POST.get('license-type','')
		year=request.POST.get('year','')
		copyright_holder=request.POST.get('copyright-holder','')
		doi=request.POST.get('doi','')
		pubdate=request.POST.get('pubdate','')
		keywords=request.POST.get('keywords','')
		absctract=request.POST.get('absctract','')
		selected_main_taxonomy=request.POST.get('selected-main-taxonomy','')
		selected_texonomy=request.POST.get('selected-texonomy','')
		authors = request.POST.get('authors','')
		conflict_interest_describe = request.POST.get('conflict-interest-describe','')

		try:
			PreprintDetails.objects.create(

				service = service,
				file = file,
				title = title,
				public_data_link = public_data_link,
				public_data_not_available_describe = public_data_not_available_describe,
				type_available_link = type_available_link,
				type_available_link_type = type_available_link_type,
				type_not_availabe_description = type_not_availabe_description,
				license_type = license_type,
				year = year,
				copyright_holder = copyright_holder,
				doi = doi,
				pubdate = pubdate,
				keywords = keywords,
				absctract = absctract,
				selected_main_taxonomy = selected_main_taxonomy,
				selected_texonomy = selected_texonomy,
				authors = authors,
				conflict_interest_describe = conflict_interest_describe,
				default_author = request.user


				)

			return redirect('my_preprints')


		except :

			return redirect('login')




@login_required(login_url='/accounts/login/')
def my_preprints(request):
	if request.method == 'GET':

		f=PreprintDetails.objects.filter(default_author=request.user)
		page = request.GET.get('page', 1)
		paginator = Paginator(f, 8)
		try:
			results = paginator.page(page)
		except PageNotAnInteger:
			results = paginator.page(1)
		except EmptyPage:
			results = paginator.page(paginator.num_pages)
		return render(request,'my-preprints.html',{'results':results})