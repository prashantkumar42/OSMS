from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from . import models
import json

# Create your views here.

def api(request):
    rbatch = request.GET.get('batch')
    if request.user.is_authenticated:
        # Create and send a JSON response
        array = models.Student.objects.filter(batch=rbatch)
        students = []
        for a in array:
            student = {"id":a.id, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":a.batch, "age":a.age}
            students.insert(len(students), student)
        students.sort(key=lambda k: k["name"], reverse=False)
        return JsonResponse({'response':students})

    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def stddelete(request):
    sid = request.GET.get('sid')
    rbatch = request.GET.get('bid')
    if request.user.is_authenticated:
        # Delete the student entry with id = sid
        models.Student.objects.filter(id=sid).delete()
    return redirect('../dashboard/?batch=' + rbatch)

def getBatchNames(request):
    if request.user.is_authenticated:
        array = models.Batch.objects.all()
        batches = []
        for a in array:
            batches.insert(len(batches), a.name)
        batches.sort()
        return JsonResponse({'response':batches})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def addBatch(request):
    rname = request.POST["name"]
    validated = False
    if rname:
        validated = True    
    
    if validated and request.user.is_authenticated:
        batch = models.Batch(
            name = rname
        )
        batch.save()
    
    return redirect('../dashboard/?batch=' + rname)

def collect(request):
    rname = request.POST["name"]
    rfather = request.POST["father"]
    rmother = request.POST["mother"]
    rbatch = request.POST["batch"]
    rage = request.POST["age"]
    rgender = request.POST["gender"]
    raddress = request.POST["address"]
    rcontact = request.POST["contact"]

    # Validate the data recieved
    validated = False
    if rname and rfather and rmother and rbatch and rage and rgender and raddress and rcontact:
        validated = True

    # Create an entry in the activity table
    if validated and request.user.is_authenticated:
        student = models.Student(
            name = rname,
            father = rfather,
            mother = rmother,
            batch = rbatch,
            age = rage,
            gender = rgender,
            address = raddress,
            contact = rcontact
        )
        student.save()

    return redirect('../dashboard/?batch=' + rbatch)

def stdupdate(request):
    rid = request.POST["id"]
    rname = request.POST["name"]
    rfather = request.POST["father"]
    rmother = request.POST["mother"]
    rbatch = request.POST["batch"]
    rage = request.POST["age"]
    rgender = request.POST["gender"]
    raddress = request.POST["address"]
    rcontact = request.POST["contact"]

    # Validate the data recieved
    validated = False
    if rname and rfather and rmother and rbatch and rage and rgender and raddress and rcontact:
        validated = True

    if validated and request.user.is_authenticated:
        # Delete old entry in the student table
        models.Student.objects.filter(id=rid).delete()

        # Create an entry in the student table
        
        student = models.Student(
            name = rname,
            father = rfather,
            mother = rmother,
            batch = rbatch,
            age = rage,
            gender = rgender,
            address = raddress,
            contact = rcontact
        )
        student.save()

    return redirect('../dashboard/?batch=' + rbatch)

