from django.db import models
from accounts.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

class PreprintDetails(models.Model):
	date = models.DateField(auto_now_add=True,auto_now=False)
	service = models.CharField(null=True,blank=True,max_length=40)
	file = models.FileField(null=True,upload_to='media',blank=True)
	title = models.CharField(null=True,blank=True,max_length=250)
	public_data_link = models.CharField(null=True,blank=True,max_length=50)
	public_data_not_available_describe = models.TextField(null=True,blank=True)
	type_available_link = models.CharField(null=True,blank=True,max_length=100)
	type_available_link_type = models.CharField(null=True,blank=True,max_length=100)
	type_not_availabe_description = models.TextField(null=True,blank=True)
	license_type = models.CharField(null=True,blank=True,max_length=40)
	year = models.CharField(null=True,blank=True,max_length=30)
	copyright_holder = models.CharField(null=True,blank=True,max_length=110)
	doi = models.CharField(null=True,blank=True,max_length=30)
	pubdate=models.CharField(null=True,blank=True,max_length=12)
	keywords = models.CharField(null=True,blank=True,max_length=250)
	absctract = models.TextField(null=True,blank=True)
	selected_main_taxonomy = models.CharField(null=True,blank=True,max_length=240)
	selected_texonomy = models.CharField(null=True,blank=True,max_length=300)
	authors= models.CharField(null=True,blank=True,max_length=60)
	conflict_interest_describe = models.TextField(null=True,blank=True)
	default_author = models.ForeignKey(User,null=True,blank=True,max_length=30,on_delete=models.CASCADE)
	approved = models.BooleanField(default=False)
	rejected = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.approved == True :
			try:
				send_mail('Your preprint has been approved', 'Congratulations ! your preprint has been approved by the administrator', 'preprints@olib.org', [self.default_author.email,])
			except:
				pass
		elif self.rejected == True:
			try:
				send_mail('Unfortunately your preprint has been rejected', 'We are sorry , your preprint has been rejected by the administrator', 'preprints@olib.org', [self.default_author.email,])
			except:
				pass
		super(PreprintDetails, self).save(*args, **kwargs)

	def summery(self):
		return self.absctract[:250]

	class Meta:
		verbose_name = 'preprint details'
		verbose_name_plural = 'preprint details'
		
	def __str__(self):
		return str(self.title)


@receiver(post_save, sender=PreprintDetails)
def set_to_downloads(sender, instance, created, **kwargs):
    d=Downloads.objects.filter(preprint=instance)
    if len(d) == 0:
    	Downloads.objects.create(preprint=instance,counter=0)
        


class Downloads(models.Model):
	preprint = models.OneToOneField(PreprintDetails,on_delete=models.CASCADE)
	counter = models.IntegerField(default=0)


	def __str__(self):
		return str(self.preprint.title)