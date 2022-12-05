from turtle import pos

import django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from EMS.models import Admin

from .models import *


# Create your views here.
def home(request):
    # email=Adsmin.objects('email_id')
    # password=Admin.objects.get('password')
    # det={'email':email,'password':password}
    return render (request,'home.html')   


def login(request):
    
    return render(request,'login.html')

def cata(request):
    emp_data = Employee.objects.filter()
    d = {'employee':emp_data}
    return render(request, 'cata.html',d)



def index(request):
    # if request.method== 'POST':
    #     username = request.POST['username']
    #     Password = request.POST['password']
    #     return redirect('login')

    #     user = auth.authenticate(username=username,password=Password)

    #     if user is not None:
    #         auth.login(request,user)
    #         return redirect("/")
    #     else:
    #         messages.info(request,'invalid credentials')
    #         return redirect('index')

    # else:
    return render(request,'index.html')


def createEmployeee(request):
    if request.method == "POST":
        name = request.POST['name']
        doj = request.POST['doj']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        emp_obj = Employee.objects.create(name=name,doj=doj,zipcode=zipcode,state=state)
        messages.success(request, "Employee created successfully")
        return redirect('employee_list')
    return render(request, 'create_employeee.html')


def rof(request):
    if request.method == "POST":
        department = request.POST['department']
        name = request.POST['name']
        category = request.POST['category']
        email = request.POST['email']
        priority = request.POST['priority']
        mobile = request.POST['mobile']
        # description = request.POST['description']
        emp_obj = add.objects.create(department=department,name=name,category=category,email=email,priority=priority,mobile=mobile)
        messages.success(request, "Ticket Submited")
        return redirect('cata')
    return render(request, 'rof.html')

def submit(request):
    emp_data = add.objects.filter()
    d = {'add':emp_data}
    return render(request, 'submit.html',d)

def view(request):
    emp_data = add.objects.filter()
    d = {'add':emp_data}
    return render(request, 'view.html',d)

def employee_list(request):
    emp_data = Employee.objects.filter()
    d = {'employee':emp_data}
    return render(request, 'employee_list.html',d)

def edit_employee(request, pid):
    emp_data =Employee.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        doj = request.POST['doj']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        emp_obj = Employee.objects.filter(id=pid).update(name=name,doj=doj,zipcode=zipcode,state=state)
        messages.success(request, "Employee Updated successfully")
        return redirect('employee_list')
    return render(request, 'edit_employeee.html', {'emp_data':emp_data})

# def delete_employee(request, pid):
#     data = Employee.objects.get(id=pid)
#     data.delete()
#     messages.success(request, "Employee Deleted successfully")
#     return redirect('employee_list')

def delete_employee(request, pid):
    data = add.objects.get(id=pid)
    data.delete()
    messages.success(request, "Employee Deleted successfully")
    return redirect('submit')

def leave_status(request, pid):
    data = Employee.objects.get(id=pid)
    if data.on_leave:
        data.on_leave = False
    else:
        data.leave_count = data.leave_count + 1
        data.on_leave = True
    data.save()
    messages.success(request, "Employee leave status Changed successfully.")
    return redirect('employee_list')



def replay(request, pid):
    data = add.objects.get(id=pid)
    # if data.on_leave:
    #     data.on_leave = False
    # else:
    #     data.leave_count = data.leave_count + 1
    #     data.on_leave = True
    # data.save()
    messages.success(request, "Issue Sloved")
    return redirect('employee_list')
