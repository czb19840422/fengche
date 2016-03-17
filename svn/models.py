from django.db import models

# Create your models here.
class svn_group(models.Model):
    groupname = models.CharField(max_length=30)

class svn_user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    createuser_date = models.DateField()
    modifyuser_date = models.DateField()
    svn_group = models.ForeignKey(svn_group)

class svn_resource(models.Model):
    svnurl = models.CharField(max_length=300)
    svnread = models.CharField(max_length=10)
    svnwrite = models.CharField(max_length=10)
    svn_users = models.ManyToManyField(svn_user)
    svn_groups = models.ManyToManyField(svn_group)