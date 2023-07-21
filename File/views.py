from django.shortcuts import render
from AddEmployee.models import Employee, Identity
from .models import File
from django.shortcuts import redirect

# Create your views here.


def transfer_file(request):
    print('yes')
    if request.method=='POST':
        department_id = request.POST.get('department')
        designation_id = request.POST.get('designation')
        transferred_file_id = request.POST.get('file_id')


        department =  Identity.objects.get(pk=department_id)
        designation = Identity.objects.get(pk=designation_id)
        transferred_file = File.objects.get(pk=transferred_file_id)

        employees = Employee.objects.filter(department = department, designation = designation)

        for employee in employees:
            File.objects.create(
                title = transferred_file.title,
                details = transferred_file.details,
                current_user = employee.employeeid,
                creator = transferred_file.creator,
                department = department,
                designation = designation,
                file1 = transferred_file.file
            )

        return redirect('base.html')
    
    departments= Identity.objects.values('department').distinct()
    designations = Identity.objects.values('designation').distinct()

    for department in departments:
        print(department['department']) 
    return render(request, 'base.html', {'departments': departments, 'designations': designations})





