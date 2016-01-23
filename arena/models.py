from django.db import models
from . import forms

class Document(models.Model):
	foldername = 'bots'
	docfile = models.FileField(upload_to=foldername)