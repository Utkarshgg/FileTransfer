from django.db import models
from AddEmployee.models import Identity

# Create your models here.

class File:
    file1 = models.FileField(upload_to='static/')
    uploaded_at = models.DateTimeField(auto_now_add=True, default=None)
    title = models.CharField(max_length=50 , primary_key=True)
    details = models.CharField(max_length=100)
    current_user = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    department = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='employee_department')
    designation = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='employee_designation')


    def __str__(self):
        return self.title + " " + self.details + " " + self.current_user + " " + self.creator + " " + self.department.department + " " + self.designation.designation










