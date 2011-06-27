from django.db import models
from django.contrib import admin


# Create your models here.

class Poll(models.Model):
	question=models.TextField()
	created=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll=models.ForeignKey(Poll)
	choice=models.CharField(max_length=255)
	votes=models.IntegerField()

	def __unicode__(self):
		return self.choice

admin.site.register(Poll)
admin.site.register(Choice)
