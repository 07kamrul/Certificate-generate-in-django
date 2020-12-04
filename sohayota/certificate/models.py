from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
from PIL import Image, ImageDraw, ImageFont
import os


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

    image = models.ImageField(blank=True)

    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):

        i = self.name
        im = Image.open(r'F:\Python\Projects\Certificate\sohayota\static\images\certificate.jpg')
        d = ImageDraw.Draw(im)
        location = (1400, 720)
        # text_color = (0, 137, 209)
        text_color = ("#0C0C98")
        font = ImageFont.truetype("calibri.ttf", 100)
        d.text(location, i, fill=text_color, font=font)
        im.save("F:\Python\Projects\Certificate\sohayota\static\images\certificate_" + i + ".png")
        # os.startfile("certificate_" + i + ".png")

        super(Sohayota,self).save(*args,**kwargs)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url