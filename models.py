from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
	fullname = models.CharField(max_length=30)
	shortname = models.CharField(max_length=4)
	slug = models.SlugField(max_length=100)
	def __unicode__(self):
		return self.shortname	
			
class Professor(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	department = models.ManyToManyField(Department, related_name="professors")
	email = models.EmailField(max_length=100)
	office = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	def __unicode__(self):
		return self.lastname

class Course(models.Model):
	crn = models.IntegerField(max_length=5)
	department = models.ManyToManyField(Department, related_name="courses")
	level = models.IntegerField(max_length=3)
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=500)
	professor = models.ManyToManyField(Professor, related_name="courses")
	slug = models.SlugField(max_length=100)
	def __unicode__(self):
		return self.department + self.level
	
class ObieConnectProfile(models.Model):
	user = models.OneToOneField(User, related_name='obieconnectprofile')
	course = models.ManyToManyField(Course, related_name="users")
	bio = models.TextField(max_length=500)
	activation_key = models.CharField(max_length=40)
	key_expires = models.DateTimeField()
	def __unicode__(self):
		return self.username
	
# django contrib comments - documentation (batteries included)
# django contrib auth - we did this.
# django registration
