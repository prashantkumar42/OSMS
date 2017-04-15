# Online School Management System
Developers: Pranshu Gupta, Prashant Kumar

## Introduction
As evey thing is going digital, we are actively promoting paperless schools one important aspect is digitalizing the school management along with the teaching process and examinations. There is a lot of paprwork often involved during the admission of students and later for fee and grades management.

Our aim is to develop a web based application that allows that school management to maintain all these procedures online. 

## Features
Currently, the features availbale in the system are the following:
+ Secure login for Administrators
+ Adding and Modifying new batches of students
+ Adding and modifying students in a batch
+ Adding course plan for a batch
+ Deleting a batch
+ Deregistering a student
+ Adding fee payment status for a student
+ Awarding grades to a student
+ Some basic Analytics Visulizations

## Interface
![Login](/images/login.png)

![Dashboard](/images/dashboard.png)

![Add Batch](/images/addbatch.png)

![Add Student](/images/addstudent.png)

![Search](/images/search.png)

![Charts](/images/charts.png)


## Implementation Details
We have implemented the Online School Management System using the Django Web Framework. The database management system used is MySQL. We have created different tables for student details, batches, grades, fees and courses with appropriate foreign keys and indexing.

To further improve the performance of our system, we have implemented pagination at two levels - alphabetical filtering for students in a batch on top of the pagination based on the number of results shown in a single api hit. We have tested with 100000 students in a batch with 10 batches - a total of 1000000 students and the dashboard is loaded almost instantaneously. Searches actively employ the indexing on names and other foreign key references and thus are very fast and results are availbale within one second.

## Future Improvements
We intend to focus on Analytics and visualization as the next step. The analytics charts involve heavy computation so they currently take 2-3 seconds to load. We wish to optimize that too.

Adding some important features like managing the co-curricular activity data of students and maintaining data related to different academic sessions will also be added.