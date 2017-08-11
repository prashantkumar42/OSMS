#!/usr/bin/python3
from services import models
import numpy as np


batches = models.Batch.objects.all()
print("Hello !")

for b in batches:
    gradeList = []
    print("Inserting For Batch: "+b.name)
    students = models.Student.objects.filter(batch__id=b.pk)
    courses = models.Course.objects.filter(batch__id=b.pk)
    for s in students:
        for c in courses:
            tmpGrade = np.random.randint(2, 5)*2
            g = models.Grades(student=s, course=c, grade=tmpGrade)
            gradeList.append(g)
    models.Grades.objects.bulk_create(gradeList)
    # insert grade per batch

print("grades insertion done")
