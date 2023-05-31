
from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("login", views.login_view, name="login"),
    path("home", views.index, name="index"),
    path("home/delAlert/<int:id>", views.delAlert, name="delAlert"),
    path("home/alertView/<int:id>", views.alertView, name="alertView"),
    path("home/checklists", views.checklists, name="checklists"),
    path("home/checklists/<str:message_success>", views.checklists, name="checklists"),
    path("home/checklists/<str:message_danger>", views.checklists, name="checklists"),
    path("home/newChecklist", views.newChecklist, name="newChecklist"),
    path("home/checklistView/<int:id>", views.checklistView, name="checklistView"),
    path("home/delChecklist/<int:id>", views.delChecklist, name="delChecklist"),
    path("home/appointment", views.appointment, name="appointment"),
    path("home/accApt/<int:id>", views.accApt, name="accApt"),
    path("home/decApt/<int:id>", views.decApt, name="decApt"),
    path("home/leave", views.leave, name="leave"),
    path("home/accLeave/<int:id>", views.accLeave, name="accLeave"),
    path("home/decLeave/<int:id>", views.decLeave, name="decLeave"),
    path("home/edit", views.edit, name="edit"),
    path("home/approve", views.approve_user, name="approve_user"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
