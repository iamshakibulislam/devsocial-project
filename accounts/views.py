from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth

def signup(request):

	if request.method == 'GET':
		return render(request,'signup.html')


	if request.method == 'POST':

		fullname = request.POST['fullname']
		email = request.POST['email']
		cemail=request.POST['confirm-email']
		password = request.POST['password']

		try:
			User.objects.get(email=email)

			return render(request,'signup.html',
					{'userexist':'user aready exists'})
		except User.DoesNotExist:
			create_user=User.objects.create_user(password=password,full_name=fullname,email=email)
			return render(request,'signup.html',
						{'success':'account created successfully.You can login now'})




def login(request):
	if request.method == 'GET':
		return render(request,'login.html')

	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		authenticate=auth.authenticate(request,email=email,password=password)
		
		if authenticate is not None :
			auth.login(request,authenticate)

			return redirect('my_preprints')

		else:
			return render(request,'login.html',{'message':'username or password is incorrect !'})



def logout(request):
	auth.logout(request)
	return redirect('index')