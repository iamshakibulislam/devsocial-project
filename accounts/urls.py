from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup ,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/reset.html',html_email_template_name='accounts/password-reset-email-template.html'),name='password_reset'),
	path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset-email.html'),name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset-conf.html'),name='password_reset_confirm'),
	path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset-suc.html'),name='password_reset_complete'),
	path('update-profile/',views.update_profile,name='update_profile')

    ]