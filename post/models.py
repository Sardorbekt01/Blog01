from django.db import models
import uuid

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),blank=False,null=False,primary_key=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField(auto_now=True)

