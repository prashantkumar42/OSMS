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
        kwargs = {"name":rbatch}
        batch = models.Batch.objects.get(**kwargs)
        print("getting all student for " + rbatch)
        array = models.Student.objects.filter(batch=batch.id)
        students = []
        for a in array:
            fee = models.Fee.objects.filter(studentId=a.id)
            if len(fee):
                student = {"id":a.id, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":rbatch, "age":a.age, "fee":"Y", "installments":fee[0].installments, "amount":fee[0].amountPerInst, "paid":fee[0].paidInst}
            else:
                student = {"id":a.id, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":rbatch, "age":a.age, "fee":"N"}
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
        models.Fee.objects.filter(studentId=sid).delete()
    return redirect('../dashboard/?batch=' + rbatch)

def getBatchNames(request):
    if request.user.is_authenticated:
        array = models.Batch.objects.all()
        batches = []
        for a in array:
            batches.insert(len(batches), {"id":a.id, "name":a.name})
        batches.sort(key=lambda k: k["name"], reverse=False)
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

# handle the condition if this batch dne
def updateBatch(request):
    oname = request.POST["oname"]
    rname = request.POST["name"]
    validated = False
    if rname:
        validated = True    
    
    if validated and request.user.is_authenticated:
        batch = models.Batch.objects.get(name=oname)
        batch.name = rname
        batch.save()
    
    return redirect('../dashboard/?batch=' + rname)

# handle the condition if this batch dne
def deleteBatch(request):
    bName = request.GET.get('batch')
    if request.user.is_authenticated:
        bid = (models.Batch.objects.get(name=bName)).id
        models.Batch.objects.filter(name=bName).delete()
        students = models.Student.objects.filter(batch=bid)
        for std in students:
            models.Fee.objects.filter(studentId=std.id).delete()
        models.Student.objects.filter(batch=bid).delete()
    return redirect('../dashboard/')

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
        batch = models.Batch.objects.get(name=rbatch)

        student = models.Student(
            name = rname,
            father = rfather,
            mother = rmother,
            batch = batch.id,
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
        batch = models.Batch.objects.get(name=rbatch)
        student = models.Student.objects.get(id=rid)        
        student.name = rname
        student.father = rfather
        student.mother = rmother
        student.batch = batch.id
        student.age = rage
        student.gender = rgender
        student.address = raddress
        student.contact = rcontact
        student.save()

    return redirect('../dashboard/?batch=' + rbatch)

def studentFee(request):
    rid = request.POST["sid"]
    bid = request.POST["batch"]
    rinst = request.POST["installments"]
    ramnt = request.POST["amount"]
    rpaid = request.POST["paid"]
    rbatch = request.POST["batch"]

    # Validate the data recieved
    validated = False
    if rid and rinst and ramnt and rpaid and rbatch:
        validated = True 

    if validated and request.user.is_authenticated:
        fee = models.Fee.objects.filter(studentId=rid)
        if len(fee): 
            fee[0].installments = rinst
            fee[0].amountPerInst = ramnt
            fee[0].paidInst = rpaid
            fee[0].save()
        else:       
            fee = models.Fee(
                studentId = rid,
                installments = rinst,
                amountPerInst = ramnt,
                paidInst = rpaid
            )
            fee.save()

    return redirect('../dashboard/?batch=' + rbatch)


def search(request):
    # http://127.0.0.1:8000/services/search?keyword=zoobi&isbatch=0&batch=Class%201&isgender=1&gender=Male&isaddress=0&address=hkh&isfee=22
    keyword = request.GET.get('keyword')
    isbatch = request.GET.get('isbatch')
    rbatch = request.GET.get('batch')
    isgender = request.GET.get('isgender')
    gender = request.GET.get('gender')
    isaddress = request.GET.get('isaddress')
    address = request.GET.get('address')
    isfee = request.GET.get('isfee')

    kwargs = {}
    validated = False
    if keyword and isfee and isbatch and isgender and isaddress and address and rbatch and gender:
        validated = True
        kwargs['name__icontains'] = keyword
        if isbatch == '1':
            batchid = (models.Batch.objects.get(name=rbatch)).id
            kwargs['batch'] = batchid
        if isgender == '1':
            kwargs['gender'] = gender
        if isaddress == '1':
            kwargs['address'] = address
    print(kwargs)
    if validated and request.user.is_authenticated:
        array = models.Student.objects.filter(**kwargs)
        students = []
        for a in array:
            fee = models.Fee.objects.filter(studentId=a.id)
            if len(fee):
                if isfee == '1':
                    pass
                student = {"id":a.id, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":rbatch, "age":a.age, "fee":"Y", "installments":fee[0].installments, "amount":fee[0].amountPerInst, "paid":fee[0].paidInst}
            else:
                student = {"id":a.id, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":rbatch, "age":a.age, "fee":"N"}
            students.insert(len(students), student)
        students.sort(key=lambda k: k["name"], reverse=False)
        return JsonResponse({'response':students})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")