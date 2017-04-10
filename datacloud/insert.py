from services import models
import numpy as np

names_female = []
names_male = []
surnames = []

# read the names dataset
with open("names.txt") as f:
    for line in f:
        # print(line)
        data = line.split(',')
        if data[1] == 'F':
            names_female.insert(len(names_female), data[0])
        elif data[1] == 'M':
            names_male.insert(len(names_male), data[0])

#print(names_female)

# # read the surnames dataset
with open("surnames.txt") as f:
    for line in f:
        data = line.split(',')
        surnames.insert(len(surnames), data[0])

#print(names_male)

b = models.Batch.objects.all()

print(b)

#age range
a1 = 2
a2 = 3
a3 = 4

for a in b:
    print(a)
    a1 += 1
    a2 += 1
    a3 += 1
    ages = [a1, a2, a3]
    studentList = []
    for i in range(10000):
        # pick a random gender 
        g = np.random.randint(0, 2)
        # pick random surname and parents' names
        surname = surnames[np.random.randint(0, len(surnames))]
        ifather = names_male[np.random.randint(0, len(names_male))] + " " + surname
        imother = names_female[np.random.randint(0, len(names_female))] + " " + surname
        iname = None
        igender = None
        # pick random age from the age set for this class
        iage = ages[np.random.randint(0, 3)]
        # pick random name as per the gender
        if g == 1:
            igender = 'F'
            iname = names_female[np.random.randint(0, len(names_female))] + " " + surname
        else:
            igender = 'M'
            iname = names_male[np.random.randint(0, len(names_male))] + " " + surname
        # create an object for insertion
        x = models.Student(name = iname, father = ifather, mother = imother, batch = a, age = iage, gender = igender, address = "Street 1, City 1", contact = "8156425678")
        studentList.insert(len(studentList), x)
    # perform bulk insertion for this batch
    models.Student.objects.bulk_create(studentList)

print(b)