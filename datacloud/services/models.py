from django.db import models
from django.utils import timezone

class Batch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDERS = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = models.CharField(max_length=6, choices=GENDERS)
    address = models.CharField(max_length=2048)

    def __str__(self):
        text = self.name + ", " + self.father + ", " + self.mother + ", " + str(self.batch) + ", " + self.contact + ", " + str(self.age) + ", " + self.gender + ", " + self.address
        return text

class Fee(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    installments = models.IntegerField()
    amountPerInst = models.IntegerField()
    paidInst = models.IntegerField()

    def __str__(self):
        return str(self.studentId)

class Course(models.Model):
    name = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.batch) + " " + self.name) 

class Grades(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseID = models.IntegerField()
    letterGrade = models.CharField(max_length=1)

    def __str__(self):
        return (str(self.studentId) + ", " + str(self.courseID) + ": " + self.letterGrade) 
