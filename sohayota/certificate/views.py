import os

from PIL import Image, ImageDraw, ImageFont

from django.shortcuts import render, redirect

# Create your views here.
from .form import *
from .models import *

def home(request):

    return render(request,'certificate/index.html')


def createCertificate(request):
    form = SohayotaForm()

    if request.method == 'POST':
        form = SohayotaForm(request.POST)

        if form.is_valid():
            form.save()
            sohayota = Sohayota.objects.latest('id')
            lastId = sohayota.id
            print("****************************")
            print(sohayota)
            print(lastId)

            obj = Sohayota.objects.get(id=lastId)

            name = obj.name
            mobileNo = obj.mobile_no
            print("////////////////////////")
            print(name)
            print(mobileNo)

            i = name

            im = Image.open(r'F:\Python\Projects\Certificate\sohayota\static\images\certificate.jpg')
            d = ImageDraw.Draw(im)
            location = (1400, 720)
            # text_color = (0, 137, 209)
            text_color = ("#0C0C98")
            font = ImageFont.truetype("calibri.ttf", 100)
            d.text(location, i, fill=text_color, font=font)
            im.save("F:\Python\Projects\Certificate\sohayota\static\images\certificate_" + i + ".png")
            # os.startfile("certificate_" + i + ".png")
            # return redirect('showCertificate',lastId)
            # return showCertificate(sohayota)

    context = {'form':form}

    return render(request,'certificate/createCertificate.html', context)


def showCertificate(request,pk_test):
    certificate = Sohayota.objects.get(id=pk_test)

    name = certificate.name
    mobileNo = certificate.mobile_no
    print("////////////////////////")
    print(name)
    print(mobileNo)

    i = name

    im = Image.open(r'certificate.png')

    d = ImageDraw.Draw(im)
    location = (250, 650)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("calibri.ttf", 70)
    d.text(location, i, fill=text_color, font=font)
    im.save("certificate_" + i + ".png")
    # os.startfile("certificate_" + i + ".png")

    return render(request,"certificate/index.html",{'certificate':certificate})

