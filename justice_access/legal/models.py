from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

#legal information model
class LegalInformation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
#legal aid model (connecting users with legal aid organizations) 
class LegalAid(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    service_area = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#case tracking model(for tracking court cases)
class CourtCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    case_number = models.CharField(max_length=50)
    case_title = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.case_title 
    

#legal information articles
class LegalTopic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

#model for users to submit legal aid requests
class LegalAidRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    issue_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

