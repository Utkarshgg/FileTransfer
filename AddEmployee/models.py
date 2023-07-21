from django.db import models

# Create your models here.


class Identity(models.Model):
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.designation+" "+self.department


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employeeid = models.CharField(max_length=100, primary_key=True)
    designation = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='employee_designation')
    department = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='employee_department')

    #relate employee id to user id


    def __str__(self):
        return self.name+" "+self.employeeid+" "+self.designation.designation+" "+self.department.department