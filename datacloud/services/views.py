from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q
from . import models
import json

# Create your views here.

def api(request):
    rbatch = request.GET.get('batch')
    if request.user.is_authenticated:
        # Create and send a JSON response
        array = models.Student.objects.filter(batch__id=rbatch).select_related('batch')
        students = []
        for a in array:
            fee = models.Fee.objects.filter(studentId=a)
            if len(fee):
                student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "batch":a.batch.name, "bid":a.batch.id, "address":a.address, "age":a.age, "fee":"Y", "installments":fee[0].installments, "amount":fee[0].amountPerInst, "paid":fee[0].paidInst}
            else:
                student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "batch":a.batch.name, "bid":a.batch.id, "address":a.address, "age":a.age, "fee":"N"}
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
            batches.insert(len(batches), {"id":a.pk, "name":a.name})
        batches.sort(key=lambda k: k["name"], reverse=False)
        return JsonResponse({'response':batches})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def addBatch(request):
    rname = request.POST["name"]
    validated = False
    
    id = None

    if rname:
        validated = True    
    
    if validated and request.user.is_authenticated:
        batch = models.Batch(
            name = rname
        )
        batch.save()
        id = batch.id
    
    return redirect('../dashboard/?batch=' + str(id))

# handle the condition if this batch dne
def updateBatch(request):
    oname = request.POST["oname"]
    rname = request.POST["name"]
    validated = False

    id = None

    if rname:
        validated = True    
    
    if validated and request.user.is_authenticated:
        batch = models.Batch.objects.get(name=oname)
        batch.name = rname
        batch.save()
        id = batch.id

    return redirect('../dashboard/?batch=' + str(id))

# handle the condition if this batch dne
def deleteBatch(request):
    bid = request.GET.get('batch')
    if request.user.is_authenticated:
        batch = models.Batch.objects.filter(pk=bid)
        if batch:
            batch.delete()
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
        batch = models.Batch.objects.get(pk=rbatch)

        student = models.Student(
            name = rname,
            father = rfather,
            mother = rmother,
            batch = batch,
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
        batch = models.Batch.objects.get(pk=rbatch)
        student = models.Student.objects.get(id=rid)        
        student.name = rname
        student.father = rfather
        student.mother = rmother
        student.batch = batch
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
        fee = models.Fee.objects.filter(studentId=rid).select_related('student')
        if len(fee): 
            fee[0].installments = rinst
            fee[0].amountPerInst = ramnt
            fee[0].paidInst = rpaid
            fee[0].save()
        else:       
            fee = models.Fee(
                studentId = models.Student.objects.get(pk=rid),
                installments = rinst,
                amountPerInst = ramnt,
                paidInst = rpaid
            )
            fee.save()

    return redirect('../dashboard/?batch=' + rbatch)


def search(request):
    # http://127.0.0.1:8000/services/search?keyword=zoobi&isbatch=0&batch=Class%201&isgender=1&gender=Male&isaddress=0&address=hkh&isfee=22
    keyword = request.GET.get('keyword')
    keytype = request.GET.get('keytype')
    isbatch = request.GET.get('isbatch')
    rbatch = request.GET.get('batch')
    isgender = request.GET.get('isgender')
    gender = request.GET.get('gender')
    isaddress = request.GET.get('isaddress')
    address = request.GET.get('address')
    isfee = request.GET.get('isfee')

    kwargs = {}
    validated = False
    if isfee and isbatch and isgender and isaddress and address and rbatch and gender:
        validated = True

        if keytype == "1":
            kwargs['name__icontains'] = keyword
        elif keytype == "2":
            kwargs['father__icontains'] = keyword
        elif keytype == "3":
            kwargs['mother__icontains'] = keyword

        if isbatch == '1':
            batchid = (models.Batch.objects.get(name=rbatch)).pk
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
            fee = models.Fee.objects.filter(studentId=a.pk)
            batch = models.Batch.objects.get(id=a.batch)
            if len(fee):
                if isfee == '1':
                    pass
                student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":batch.name, "bid":a.batch, "age":a.age, "fee":"Y", "installments":fee[0].installments, "amount":fee[0].amountPerInst, "paid":fee[0].paidInst}
            else:
                student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":batch.name, "bid":a.batch, "age":a.age, "fee":"N"}
            students.insert(len(students), student)
        students.sort(key=lambda k: k["name"], reverse=False)
        return JsonResponse({'response':students})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")


def addCourse(request):
    batchid = request.POST["bid"]
    rbatch = request.POST["bname"]
    acourse = request.POST["course"]
    # Validate the data recieved
    validated = False
    if batchid and acourse:
        validated = True 

    if validated and request.user.is_authenticated:      
        course = models.Course(
            name = acourse,
            batch = batchid
        )
        course.save()

    return redirect('../dashboard/?batch=' + rbatch)

def getCourses(request):
    bid = request.GET.get('bid')
    batch = models.Batch.objects.get(pk=bid)
    if request.user.is_authenticated:
        array = models.Course.objects.filter(batch=batch)
        courses = []
        for a in array:
            courses.insert(len(courses), {"id":a.pk, "name":a.name})
        courses.sort(key=lambda k: k["name"], reverse=False)
        return JsonResponse({'response':courses})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def deleteCourse(request):
    cid = request.GET.get('cid')
    if request.user.is_authenticated:
        models.Course.objects.filter(id=cid).delete()
        return HttpResponse("Done")
    return HttpResponse("invalid request, either you are not authorized or request was malformed")

def addGrades(request):
    if request.user.is_authenticated:
        bid = int(request.POST["bidforgrade"])
        rbatch = (models.Batch.objects.get(id=bid)).name
        sid = int(request.POST["sidforgrade"])
        n = int(request.POST["numberofcourses"])
        for i in range(0,n):
            grades = (request.POST["grading"+str(i)]).split('_')
            cid, lettergrade = int(grades[0]), grades[1]
            models.Grades.objects.filter(studentId=sid).filter(courseID=cid).delete()
            grade = models.Grades(
                studentId = sid,
                courseID = cid,
                letterGrade = lettergrade        
            )
            grade.save()            
        return redirect('../dashboard/?batch=' + rbatch)
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def getGrades(request):
    if request.user.is_authenticated:
        sid = request.GET.get('sid')
        courses = json.loads(request.GET.get('cjson'))
        
        query = Q()
        for cid in courses:
            query = query | Q(courseID=cid)
        array = models.Grades.objects.filter(studentId=sid).filter(query)
        
        response = []
        for a in array:
            response.insert(len(response), {"sid":a.studentId, "cid":a.courseID, "grade":a.letterGrade})
        return JsonResponse({'response':response})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")    
