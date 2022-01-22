from django.db import models

# Create your models here.
class AdminDetails(models.Model):
    name = models.CharField(max_length=210, null=True, blank=True)
    email = models.CharField(max_length=210, null=True, blank=True)
    password = models.CharField(max_length=210, null=True, blank=True)
    auth_token = models.CharField(max_length=210, null=True, blank=True)

    class Meta:
        db_table = 'admin_details'

class Books(models.Model):
    b_name = models.CharField(max_length=210, null=True, blank=True)
    b_publisher = models.CharField(max_length=210, null=True, blank=True)
    b_type = models.CharField(max_length=210, null=True, blank=True)
    book_token = models.CharField(max_length=210, null=True, blank=True)   
    
    class Meta:
        db_table = 'book_details'