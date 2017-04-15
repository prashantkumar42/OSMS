from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q
from django.db.models import Avg
from . import models
import json

# import your views here
# from .charts import views

# Create your views here.

def api(request):
    kwargs = {}
    rbatch = request.GET.get('batch')
    alpha = request.GET.get('alpha')
    page = int(request.GET.get('page')) - 1
    if request.user.is_authenticated:
        # Create and send a JSON response
        batch = models.Batch.objects.get(pk=rbatch)
        kwargs["batch__id"] = rbatch
        kwargs["name__istartswith"] = alpha
        array = models.Student.objects.filter(**kwargs).order_by('name')[page*1000:(page+1)*1000]
        students = []
        for a in array:
            student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "batch":batch.name, "bid":batch.id, "address":a.address, "age":a.age}    
            students.insert(len(students), student)
        # students.sort(key=lambda k: k["name"], reverse=False)
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
        fee = models.Fee.objects.filter(student__id=rid)
        if len(fee): 
            fee[0].installments = rinst
            fee[0].amountPerInst = ramnt
            fee[0].paidInst = rpaid
            fee[0].save()
        else:       
            fee = models.Fee(
                student = models.Student.objects.get(pk=rid),
                installments = rinst,
                amountPerInst = ramnt,
                paidInst = rpaid
            )
            fee.save()

    return redirect('../dashboard/?batch=' + bid)

def getFee(request):
    sid = request.GET.get('sid')
    if request.user.is_authenticated:
        fee = models.Fee.objects.get(student__id=sid)
        print(fee.installments, fee.amountPerInst, fee.paidInst)
        fees = {"installments":fee.installments, "amount":fee.amountPerInst, "paid":fee.paidInst}
        return JsonResponse({'response':fees})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")    

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
            kwargs['name__istartswith'] = keyword
        elif keytype == "2":
            kwargs['father__istartswith'] = keyword
        elif keytype == "3":
            kwargs['mother__istartswith'] = keyword

        if isbatch == '1':
            batch = (models.Batch.objects.get(pk=rbatch))
            kwargs['batch'] = batch
        if isgender == '1':
            kwargs['gender'] = gender[0]
        if isaddress == '1':
            kwargs['address'] = address

    print(kwargs)
    if validated and request.user.is_authenticated:
        array = models.Student.objects.filter(**kwargs).select_related('batch')
        students = []
        for a in array:
            fee = models.Fee.objects.filter(student=a)
            if len(fee):
                if isfee == '1':
                    pass
                student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":a.batch.name, "bid":a.batch.id, "age":a.age, "fee":"Y", "installments":fee[0].installments, "amount":fee[0].amountPerInst, "paid":fee[0].paidInst}
            else:
                student = {"id":a.pk, "name":a.name, "father":a.father, "mother":a.mother, "gender":a.gender, "contact":a.contact, "address":a.address, "batch":a.batch.name, "bid":a.batch.id, "age":a.age, "fee":"N"}
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
            batch = models.Batch.objects.get(pk=batchid)
        )
        course.save()

    return redirect('../dashboard/?batch=' + batchid)

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
            # convert letter grade to int
            intGrade = (ord('F') - ord(lettergrade))*2
            grade = models.Grades.objects.filter(student_id=sid).filter(course_id=cid)
            if(len(grade)):
                grade[0].grade = intGrade
                grade[0].save()
            else:
                Grade = models.Grades(
                    student = models.Student.objects.get(pk=sid),
                    course = models.Course.objects.get(pk=cid),
                    grade = intGrade
                )
                Grade.save()
        return redirect('../dashboard/?batch=' + str(bid))
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def getGrades(request):
    if request.user.is_authenticated:
        sid = request.GET.get('sid')
        courses = json.loads(request.GET.get('cjson'))
        
        query = Q()
        for c in courses:
            print(c)
            query = query | Q(course=c)
        array = models.Grades.objects.filter(student__id=sid).filter(query)
        
        response = []
        for a in array:
            grade = chr(ord('F')-(int)(a.grade/2))
            response.insert(len(response), {"sid":sid, "cid":a.course.pk, "grade": grade})
        return JsonResponse({'response':response})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")


# Charts Views
def getChartNumStudents(request): #return number of Girls & Boys in each Class
    if request.user.is_authenticated:
        # models.Batch
        array = models.Batch.objects.all()
        response = {}
        batches = []
        numGirls = []
        numBoys = []
        for a in array:
            batches.append(a.name)
            numGirls.append(models.Student.objects.filter(batch__id=a.pk, gender='F').count())
            numBoys.append(models.Student.objects.filter(batch__id=a.pk, gender='M').count())

        response["Categories"] = batches
        response["Girls"] = numGirls
        response["Boys"] = numBoys
        return JsonResponse(response)
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def getChartAvgPerformance(request): # return the average cpi/grade of each batch/class
    if request.user.is_authenticated:
        # models.Batch
        response = {}
        batches = []
        avgGirls = []
        avgBoys = []
        avgAllStudents = []

        batchArray = models.Batch.objects.all()
        for b in batchArray:
            # print(b.name)
            batches.append(b.name)
            courseArray = models.Course.objects.filter(batch__id=b.pk)
            # constructing the OR query to get grades corresponding to the courses of a batch

            query = Q()
            for c in courseArray:
                query = query | Q(course=c)
            # store average grade of each batch in an array
            if len(courseArray):
                avgAllStudents.append(models.Grades.objects.filter(query).aggregate(Avg('grade')))
                # array = models.Grades.objects.filter(query)
            else:
                avgAllStudents.append({'grade__avg': 0})
                # array =[]

        for i in range(len(avgAllStudents)):
            # print(avgAllStudents[i]['grade__avg'])
            avgAllStudents[i] = avgAllStudents[i]['grade__avg']*10
        # print(avgAllStudents)

        response["Categories"] = batches
        response["Girls"] = avgGirls
        response["Boys"] = avgBoys
        response["All"] = avgAllStudents
        return JsonResponse(response)
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")
