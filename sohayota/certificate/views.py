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

            obj = form.save(commit=False)

            obj.image = "certificate_" + obj.name + ".png"
            obj.save()

            sohayota = Sohayota.objects.latest('id')
            lastId = sohayota.id

            return redirect('showCertificate',lastId)


    context = {'form':form}

    return render(request,'certificate/createCertificate.html', context)


def showCertificate(request,pk_test):
    certificate = Sohayota.objects.get(id=pk_test)

    context = {'certificate':certificate}

    return render(request,"certificate/showCertificate.html",context)
