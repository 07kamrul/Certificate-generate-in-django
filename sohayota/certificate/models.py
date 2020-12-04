from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Sohayota(models.Model):

    OCCUPATION_STATUS = (
        ('Job','Job'),
        ('Business','Business'),
        ('Retired','Retired'),
        ('Housewife','Housewife'),
        ('Student','Student'),
        ('Other','Other'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, null = True)
    mobile_no = models.IntegerField(null= True, validators=[MaxValueValidator(99999999999)])
    email_id = models.EmailField(max_length= 50, null= True)
    address = models.CharField(max_length= 200, null= True)
    occupation = models.CharField(max_length = 100, null = True, choices=OCCUPATION_STATUS)

    # images = models.ImageField(default="certificate.jpg", null=True, blank=True)

    def __int__(self):
        return self.id


