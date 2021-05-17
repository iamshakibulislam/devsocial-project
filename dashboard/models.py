from django.db import models
from accounts.models import User

class PreprintDetails(models.Model):
	service = models.CharField(null=True,blank=True,max_length=40)
	file = models.FileField(null=True,upload_to='media',blank=True)
	title = models.CharField(null=True,blank=True,max_length=50)
	public_data_link = models.CharField(null=True,blank=True,max_length=50)
	public_data_not_available_describe = models.TextField(null=True,blank=True)
	type_available_link = models.CharField(null=True,blank=True,max_length=100)
	type_available_link_type = models.CharField(null=True,blank=True,max_length=100)
	type_not_availabe_description = models.TextField(null=True,blank=True)
	license_type = models.CharField(null=True,blank=True,max_length=40)
	year = models.CharField(null=True,blank=True,max_length=30)
	copyright_holder = models.CharField(null=True,blank=True,max_length=30)
	doi = models.CharField(null=True,blank=True,max_length=30)
	pubdate=models.CharField(null=True,blank=True,max_length=12)
	keywords = models.CharField(null=True,blank=True,max_length=50)
	absctract = models.TextField(null=True,blank=True)
	selected_main_taxonomy = models.CharField(null=True,blank=True,max_length=40)
	selected_texonomy = models.CharField(null=True,blank=True,max_length=30)
	authors= models.CharField(null=True,blank=True,max_length=60)
	conflict_interest_describe = models.TextField(null=True,blank=True)
	default_author = models.ForeignKey(User,null=True,blank=True,max_length=30,on_delete=models.CASCADE)
	approved = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'preprint details'
		verbose_name_plural = 'preprint details'
		
	def __str__(self):
		return str(self.title)


