from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
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




def update_profile(request):
	if request.method == 'GET':

		return render(request,'update-profile.html')


	if request.method == 'POST':
		name = request.POST['full_name']
		passavailable=False
		try:
			s=User.objects.get(email=request.user.email)
			s.full_name = name
			s.save()
			curr_pass = request.POST['current_pass']
			new_pass = request.POST['new_pass']
			check_pass=check_password(curr_pass,request.user.password)
			passavailable = True
			print('your status',passavailable)

		except:
			return render(request,'update-profile.html',{'message':'Updated information'})

		if passavailable == True:
			sel=User.objects.get(email=request.user.email)
			sel.set_password(new_pass)
			sel.save()
			return render(request,'update-profile.html',{'message':'Updated information'})

		

