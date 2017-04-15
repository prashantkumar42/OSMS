#!/usr/bin/python3
from services import models
import numpy as np


batches = models.Batch.objects.all()
print("hello")
print(len(batches))

for b in batches:
    gradeList = []
    print(b.name)
    students = models.Student.objects.filter(batch__id=b.pk)
    courses = models.Course.objects.filter(batch__id=b.pk)
    print(courses)
    for s in students:
        for c in courses:
            tmpGrade = np.random.randint(0, 3)
            g = models.Grades(student=s, course=c, grade=tmpGrade)
            gradeList.append(g)
    print(gradeList)
    models.Grades.object.bulk_create(gradeList)
    # insert grade per batch
