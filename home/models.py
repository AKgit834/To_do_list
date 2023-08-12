from django.db import models

# Create your models here.
class lis(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True,null=False)
    uname=models.CharField(max_length=122,default='')
    name=models.CharField(max_length=122)
    date=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

class contact_details(models.Model):
    name=models.CharField(max_length=122)
    phone=models.IntegerField()
    desc=models.CharField(max_length=122)
    date=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    
class sign(models.Model):
    name=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=122,default='')

    def __str__(self):
        return self.name
