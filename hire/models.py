from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class UploadModel(models.Model):
# 	product_id 		= models.AutoField
# 	image_name		= models.CharField(max_length=50)
# 	image_desc		= models.CharField(max_length=200)
# 	water_mark		= models.CharField(max_length=50)
# 	owner_name		= models.CharField(max_length=60)
# 	image			= models.FileField(upload_to='uploadimages/images')


# 	def __str__(self):
# 		return self.image_name


class UserProfile1(models.Model):
	user 				=	models.OneToOneField(User, on_delete= models.CASCADE)
	skills				=	models.CharField(max_length=1000, blank=True)
	stackoverflow_link	=	models.URLField(max_length=1000, blank=True) 
	codechef_link		=	models.URLField(max_length=1000, blank=True)
	techgig_link		=	models.URLField(max_length=1000, blank=True)
	codeforces_link		=	models.URLField(max_length=1000, blank=True)
	stackoverflow_points=	models.CharField(max_length=200, blank=True, default='00')
	codechef_points		=	models.CharField(max_length=200, blank=True, default='00')
	techgig_points		=	models.CharField(max_length=200, blank=True, default='00')
	codeforces_points	=	models.CharField(max_length=200, blank=True, default='00')
	profile_pic			=	models.FileField(upload_to='hire/images')
	tag_line			=	models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return self.user.username



class CompanyProfile(models.Model):
	user 				=	models.OneToOneField(User, on_delete= models.CASCADE)
	company_name		=	models.CharField(max_length=200, blank=True) 
	company_id			=	models.CharField(max_length=200, blank=True)
	company_logo		=	models.FileField(upload_to='hire/images')
	company_link		=	models.URLField(max_length=1000, blank=True)


	def __str__(self):
		return self.user.username		




class contactDB(models.Model):
	name		=	models.CharField(max_length=200, blank=True)
	user_email		=	models.CharField(max_length=200, blank=True)
	sender_name		=	models.CharField(max_length=200, blank=True)