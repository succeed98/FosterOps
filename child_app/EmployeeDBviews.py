from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from django.utils.dateparse import parse_date

# from child_app.forms import AddStudentForm, EditStudentForm
from child_app.models import Child
from child_app.models import Room
from child_app.models import Donation_History
from child_app.models import Medical_History


def employee_home(request):
    return render(request,"employeedb_template/home_content.html")

# def manage_child(request):
#     childrens = Child.objects.raw('SELECT * FROM child_app_child')
#     return render(request,"admindb_template/manage_child_template.html", {"childrens":childrens})

def manage_room_emp(request):
    rooms = Room.objects.raw('SELECT * FROM child_app_room')
    return render(request,"employeedb_template/manage_room_template.html", {"rooms":rooms})

def manage_donation_history_emp(request):
     donations = Donation_History.objects.raw('SELECT * FROM child_app_donation_history')
     return render(request,"employeedb_template/manage_donation_history_template.html", {"donations":donations})
    
def manage_child_emp(request):
    childrens = Child.objects.raw('SELECT * FROM child_app_child')
    return render(request,"employeedb_template/manage_child_template.html", {"childrens":childrens})

def manage_medical_history_emp(request):
    medicalhistory = Medical_History.objects.raw('SELECT * FROM child_app_medical_history')
    return render(request,"employeedb_template/manage_medical_history_template.html", {"medicalhistory":medicalhistory})

# def edit_child(request,Child_id):
#     child=Child.objects.raw('SELECT * FROM child_app_child WHERE Child_id = %s',[Child_id])[0]
#     return render(request,"admindb_template/edit_child_template.html",{"child":child})

# def edit_child_save(request):
#     if request.method!="POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         Child_id=request.POST.get("Child_id")
#         First_Name=request.POST.get("First_Name")
#         Last_Name=request.POST.get("Last_Name")
#         DOB=parse_date(request.POST.get("DOB"))
#         DOA=parse_date(request.POST.get("DOA"))
#         CPhoto=request.POST.get("CPhoto")
#         CANo=request.POST.get("CANo")
#         CPANo=request.POST.get("CPANo")
#         GName=request.POST.get("GName")
#         GANo=request.POST.get("GANo")
#         GPANo=request.POST.get("GPANo")
#         rid_id=request.POST.get("rid")
#         curr = connection.cursor()
#         try:
#             curr.execute("UPDATE child_app_child SET First_Name = %s,Last_Name = %s,DOB = %s,DOA = %s,CPhoto = %s,CANo = %s,CPANo = %s,GName = %s,GANo = %s,GPANo = %s,rid_id = %s  WHERE child_id = %s", [First_Name,Last_Name,DOB,DOA,CPhoto,CANo,CPANo,GName,GANo,GPANo,rid_id,Child_id])
#             messages.success(request,"Successfully Edited Child Details")
#             return HttpResponseRedirect("/edit_child/"+Child_id)
#         except:
#             messages.error(request)
#             return HttpResponseRedirect("/edit_child/"+Child_id)

# def edit_room(request,room_id):
#     room=Room.objects.raw('SELECT * FROM child_app_room WHERE room_id = %s',[room_id])[0]
#     return render(request,"admindb_template/edit_room_template.html",{"room":room})

# def edit_room_save(request):
#     if request.method!="POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         room_id=request.POST.get("room_id")
#         floor=int(request.POST.get("floor"))
#         max_occupancy=int(request.POST.get("max_occupancy"))
#         curr = connection.cursor()
#         try:
#             curr.execute("UPDATE child_app_room SET floor = %s, max_occupancy = %s WHERE room_id = %s", [floor,max_occupancy,room_id])
#             messages.success(request,"Successfully Edited Room Details")
#             return HttpResponseRedirect("/edit_room/"+room_id)
#         except:
#             messages.error(request,"Failed to Edit Room Details")
#             return HttpResponseRedirect("/edit_room/"+room_id)

# def edit_donation_history(request,Don_id):
#     donation=Donation_History.objects.raw('SELECT * FROM child_app_donation_history WHERE Don_id = %s',[Don_id])[0]
#     return render(request,"admindb_template/edit_donation_history_template.html",{"donation":donation})

# def edit_donation_history_save(request):
#     if request.method!="POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         Don_id=request.POST.get("Don_id")
#         DName=request.POST.get("DName")
#         DPanno=request.POST.get("DPanno")
#         Ddate=parse_date(request.POST.get("Ddate"))
#         Amt=int(request.POST.get("Amt"))
#         curr = connection.cursor()
#         try:
#             curr.execute("UPDATE child_app_donation_history SET DName = %s, DPanno = %s,Ddate = %s,Amt = %s WHERE Don_id = %s", [DName,DPanno,Ddate,Amt,Don_id])
#             messages.success(request,"Successfully Edited Donation Details")
#             return HttpResponseRedirect("/edit_donation_history/"+Don_id)
#         except:
#             messages.error(request,"Failed to Edit Donation Details")
#             return HttpResponseRedirect("/edit_donation_history/"+Don_id)