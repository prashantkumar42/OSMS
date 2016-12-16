from django.db import models
from django.utils import timezone

class Student(models.Model):
	name = models.CharField(max_length=255)
	father = models.CharField(max_length=255)
	mother = models.CharField(max_length=255)
	batch = models.IntegerField()
	contact = models.CharField(max_length=255)
	age = models.IntegerField()
	GENDERS = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
	gender = models.CharField(max_length=1, choices=GENDERS)
	address = models.CharField(max_length=2048)

	def __str__(self):
		text = self.name + ", " + self.father + ", " + self.mother + ", " + str(self.batch) + ", " + self.contact + ", " + str(self.age) + ", " + self.gender + ", " + self.address
		return text

class Batch(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name
