from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers
import datetime
import json
import re

from .models import User, Checklist, Item, Alert, Appointment, Leave

departments = ['All', 'General', 'Accounts', 'Front Office', 'Food and Beverage service', 'House keeping', 'Maintence', 'Managment', 'Security']
departments_key = ['All', 'HK', 'Accounts', 'FO', 'F&B', 'General', 'Maintence', 'Managment', 'Security', 'Accounts']

leave_types = ['Sick', 'Casual', 'Privillage']

@login_required
def index(request, message_success=None, message_danger=None):
    # Alerts page
    if request.user.is_authenticated:
        if request.user.is_authenticated and request.user.manager == True and request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            image_url = request.POST.get('img_url')
            department = request.POST.get('department')
            
            if department == "House keeping":
                department = "HK"
            elif department == "Front Office":
                department = "FO"
            elif department == "Food and Beverage service":
                department = "F&B"
            
            a_temp = Alert()
            a_temp.title = title
            a_temp.description = description
            a_temp.image_url = image_url
            a_temp.department = department
            a_temp.made_by = request.user
            a_temp.save()
            
            return HttpResponseRedirect(reverse('index'))
        else:
            if message_success:
                print(message_success)
                return render(request, "intracom/alerts.html", {
                    "alerts": Alert.objects.all(),
                    "departments": departments,
                    "message_success": message_success
                })
            elif message_danger:
                print(message_danger)
                return render(request, "intracom/alerts.html", {
                    "alerts": Alert.objects.all(),
                    "departments": departments,
                    "message_danger": message_danger
                })
            else:
                return render(request, "intracom/alerts.html", {
                    "alerts": Alert.objects.all(),
                    "departments": departments
                })
    else:
        return HttpResponseRedirect(reverse('login'))

@login_required
def delChecklist(request, id):
    if request.user.manager and request.user.is_authenticated:
        print(request.method)
        list_temp = Checklist.objects.get(id=id)
        list_temp.delete()
        message_success = "Deleted checklist successfully!!"
        return HttpResponseRedirect(reverse('checklists', args=[message_success]))

@login_required  
def delAlert(request, id):
    if request.user.manager and request.user.is_authenticated:
        print(request.method)
        alert_temp = Alert.objects.get(id=id)
        alert_temp.delete()
        message_danger = "Deleted alert successfully!!"
        return HttpResponseRedirect(reverse('checklists', args=[message_danger]))

@login_required   
def alertView(request, id):
    if request.user.is_authenticated:
        alert_original = Alert.objects.get(id=id)
        
        b = alert_original.description.splitlines()
        print(len(b))
        print(b)
        a = print(alert_original.description)
        print(a)
        alert = []
        alert.clear()
        alert.append(alert_original.title)
        alert.append(alert_original.made_by.username)
        alert.append(alert_original.creation_dt)
        alert.append(alert_original.department)
        alert.append(alert_original.description)
        
        print(alert)
        
        return JsonResponse({"alert": alert, "description": b})

@login_required    
def edit(request):
    if request.user.manager:
        if request.method == 'POST':        
            users = User.objects.all()  
            for user in users:
                print(request.POST.get(f"checkbox_{user.id}"))
                if user.manager == request.POST.get(f"checklist_{user.id}"):
                    pass
                else:
                    if request.POST.get(f"checkbox_{user.id}") == None:
                        id = user.id
                        print(id)
                        temp_user = User.objects.get(id=id)
                        print(temp_user)
                        temp_user.manager = False
                        print(temp_user.manager)
                        temp_user.save()
                    else:
                        id = user.id
                        print(id)
                        temp_user = User.objects.get(id=id)
                        print(temp_user)
                        temp_user.manager = True
                        print(temp_user.manager)
                        temp_user.save()
            return HttpResponseRedirect(reverse('edit'))
            
        else:
            users = User.objects.all()
            user_manager = []   
            user_active = []    
            for user in users:
                if user.manager:
                    user_manager.append(user.id)
                if user.is_active:
                    user_active.append(user.id)
            
            return render(request, "intracom/edit.html", {
                "users": users,
                "user_manager": user_manager,
                "user_active": user_active
            })
    else:
        return HttpResponseRedirect(reverse('index'))

def approve_user(request):
    if request.user.manager:
        if request.method == 'POST':        
            users = User.objects.all()  
            for user in users:
                print(request.POST.get(f"approve_{user.id}"))
                if user.is_active == request.POST.get(f"approve_{user.id}"):
                    pass
                else:
                    if request.POST.get(f"approve_{user.id}") == None:
                        id = user.id
                        temp_user = User.objects.get(id=id)
                        temp_user.is_active = False
                        temp_user.save()
                    else:
                        id = user.id
                        temp_user = User.objects.get(id=id)
                        temp_user.is_active = True
                        temp_user.save()
            return HttpResponseRedirect(reverse('edit'))
        else:
            return HttpResponseRedirect(reverse('edit'))
    else:
        return HttpResponseRedirect(reverse('edit'))

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

            # Attempt to sign user in
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            # Check if authentication successful
            if user is not None:
                if user.is_active:
                    print(user.is_active)
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "intracom/login.html", {
                    "message": "Invalid username and/or password."
                })
        else:
            return render(request, "intracom/login.html")
    else:
        return HttpResponseRedirect(reverse('index'))

@login_required        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "intracom/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.is_active = False
            user.save()
        except IntegrityError:
            return render(request, "intracom/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "intracom/register.html")

@login_required 
def checklists(request, message_success=None, message_danger=None):
    if request.method == 'POST':
        department = request.POST.get('department')
        print(department)
        default = str(department)
        if department == "House keeping":
            department = "HK"
        elif department == "Front Office":
            department = "FO"
        elif department == "Food and Beverage service":
            department = "F&B"
        if not department == "All":
            checklists = Checklist.objects.filter(department=department)
            print(checklists)
        else:
            checklists = Checklist.objects.all()
        return render(request, "intracom/checklists.html", {
            "checklists": checklists,
            "default": default,
            "departments": departments,
        })
        
        message_sucess = "New checklist has been created!"
        
        return HttpResponseRedirect(reverse('checklists', args=[message_sucess]))
        
    else:
        checklists = Checklist.objects.all()
        if message_success:
            return render(request, "intracom/checklists.html", {
                "checklists": checklists,
                "default": "All",
                "departments": departments,
                "message_success": message_success
            })
        elif message_danger:
            return render(request, "intracom/checklists.html", {
                "checklists": checklists,
                "default": "All",
                "departments": departments,
                "message_danger": message_danger
            })
        else:
            return render(request, "intracom/checklists.html", {
                "checklists": checklists,
                "default": "All",
                "departments": departments
            })

@login_required 
def newChecklist(request):
    if request.user.is_authenticated and request.user.manager == True and request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        img_url = request.POST.get('img_url')
        items_all = request.POST.get('items')
        items_list = items_all.splitlines()
        department = request.POST.get('department')
        print(department)
        
        if department == "House keeping":
            department = "HK"
        elif department == "Front Office":
            department = "FO"
        elif department == "Food and Beverage service":
            department = "F&B"
        
        print(title)
        print(description)
        print(items_list)
        print(img_url)
        print(department)
        
        checklist_temp = Checklist()
        checklist_temp.title = title
        checklist_temp.description = description
        checklist_temp.department = department
        checklist_temp.image = img_url
        checklist_temp.category = department
        
        res = [ele for ele in items_list if not ele.isspace()]
        while("" in res):
            res.remove("")
        
        print(res)
        
        print(checklist_temp)
        checklist_temp.save()
        
        for item in res:
            item_temp = Item()
            item_temp.checklist = checklist_temp
            item_temp.item = item
            item_temp.save()
        print(items_all)
            
        
        return HttpResponseRedirect(reverse('checklists'))
    else:
        return HttpResponseRedirect(reverse('checklists'))

@login_required 
def checklistView(request, id):
    if request.user.is_authenticated:
        checklist_original = Checklist.objects.get(id=id)
        checklist_id = checklist_original.id
        print(checklist_id)
        list_items = Item.objects.filter(checklist=checklist_id)
        
        checklist = []
        checklist.append(checklist_original.title)
        checklist.append(checklist_original.description)
        checklist.append(checklist_original.department)
        
        items = []
        for item in list_items:
            print(item.item)
            items.append(item.item)
        print(items)
        
        return JsonResponse({"checklist": checklist,  "items": items})

@login_required     
def appointment(request):
    if request.method == "POST":
        to_1 = request.POST.get('To')
        to = User.objects.get(username=to_1)
        m = Appointment()
        m.request_user = request.user
        m.requested_user = to
        m.frm = request.POST.get('start_date')
        m.to = request.POST.get('end_date')
        m.subject = request.POST.get('subject')
        m.description = request.POST.get('description')
        m.completed = 'Waiting'
        print(m)
        m.save()
        return HttpResponseRedirect(reverse('appointment'))
    else:
        appointments = Appointment.objects.filter(request_user=request.user)
        appointments_to = Appointment.objects.filter(requested_user=request.user)
        users = User.objects.filter(manager=True)
        appointments = appointments.union(appointments_to).order_by("frm")            
        
        for appointment in appointments:
            current_time_full = str(datetime.datetime.now())
            current_time = current_time_full[:16]
            time_full = str(appointment.to)
            time_filtered = time_full[:16]
            
            equal = False
            
            # Day
            dt = datetime.datetime.now()
            day = time_full[8:-15]
            current_day = dt.strftime('%d')
            month = time_full[5:-18]
            current_month = dt.strftime('%m')
            if time_full[:4] == current_time[:4]:
                # Year
                if month == current_month:
                    # Month
                    if day == current_day:
                        equal = True
            else:
                equal = False
             
            if equal == True and appointment.completed == "Waiting":
                return HttpResponseRedirect(reverse('decApt', args=[appointment.id]))
                
            
        return render(request, "intracom/appointment.html", {
            "appointments": appointments,
            "users": users,
            "datetime":  datetime.datetime.now()
        })

@login_required    
def accApt(request, id):
    if request.method == 'POST':
        message = request.POST.get('message')
        appo = Appointment.objects.get(id=id)
        appo.completed = "Accepted"
        appo.complete_msg = message
        appo.save()
        return HttpResponseRedirect(reverse('appointment'))

@login_required     
def decApt(request, id):
    appo = Appointment.objects.get(id=id)
    if appo.completed == "Waiting":
        if request.POST.get('message'):
            message = request.POST.get('message')
        else:
            message="This appointment was automatically declined due because the other user did not respond to your request and the meeting date as passed"
        appo.completed = "Rejected"
        appo.complete_msg = message
        appo.save()
        return HttpResponseRedirect(reverse('appointment'))
    else:
        return HttpResponseRedirect(reverse('appointment'))

@login_required         
def leave(request):
    if request.method == "POST":
        leave_type = request.POST.get('leave_type')
        reason = request.POST.get('reason')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        l = Leave()
        l.leave_type = leave_type
        l.reason = reason
        l.name = request.user
        l.approved = "Waiting"
        l.frm = start_date
        l.to = end_date
        l.save()
        return HttpResponseRedirect(reverse('leave'))
    else:
        if request.user.manager:
            leavs = Leave.objects.all()
        else:
            leavs = Leave.objects.filter(name=request.user)
            
        for leave in leavs:
            current_time_full = str(datetime.datetime.now())
            current_time = current_time_full[:16]
            time_full = str(leave.to)
            time_filtered = time_full[:16]
            
            equal = False
            
            # Day
            dt = datetime.datetime.now()
            day = time_full[8:-15]
            current_day = dt.strftime('%d')
            month = time_full[5:-18]
            current_month = dt.strftime('%m')
            if time_full[:4] == current_time[:4]:
                # Year
                if month == current_month:
                    # Month
                    if day == current_day:
                        equal = True
            else:
                equal = False
             
            if equal == True and leave.approved == "Waiting":
                return HttpResponseRedirect(reverse('decLeave', args=[leave.id]))
            
        return render(request, "intracom/leave.html", {
            "leavs": leavs,
            "leave_types": leave_types,
            "datetime":  datetime.datetime.now()
        })
    
@login_required          
def accLeave(request, id):
    leave = Leave.objects.get(id=id)
    if leave.approved == "Waiting":
        if request.POST.get('message'):
            message = request.POST.get('message')
        else:
            message="This leave application was automatically declined due because the managers did not respond to your request and the leave date as passed"
        leave.approved = "Accepted"
        leave.approve_msg = message
        leave.save()
        return HttpResponseRedirect(reverse('leave'))
    else:
        return HttpResponseRedirect(reverse('leave'))

@login_required       
def decLeave(request, id):
    leave = Leave.objects.get(id=id)
    if leave.approved == "Waiting":
        try:
            print(request.POST.get('message'))
        except:
            pass
        if request.POST.get('message'):
            message = request.POST.get('message')
        else:
            message = "This leave application was automatically declined due because the managers user did not respond to your request and the leave start date has passed"
        leave.approved = "Rejected"
        leave.approve_msg = message
        leave.save()
        return HttpResponseRedirect(reverse('leave'))
    else:
        return HttpResponseRedirect(reverse('leave'))  