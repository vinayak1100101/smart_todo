from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    srn=models.AutoField(auto_created=True,primary_key=True)
    title=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
