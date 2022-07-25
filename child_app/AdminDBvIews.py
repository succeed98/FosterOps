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
from child_app.models import Employee
from child_app.models import CustomUser
from child_app.models import Office_Bearers
from child_app.models import Medical_History


def admin_home(request):
    return render(request,"admindb_template/home_content.html")

def add_child(request):
    return render(request,"admindb_template/add_child_template.html")

def add_medical_history(request):
    return render(request,"admindb_template/add_medical_history_template.html")
    
def add_child_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        Child_id=request.POST.get("Child_id")
        First_Name=request.POST.get("First_Name")
        Last_Name=request.POST.get("Last_Name")
        DOB=parse_date(request.POST.get("DOB"))
        DOA=parse_date(request.POST.get("DOA"))
        CPhoto=request.POST.get("CPhoto")
        CANo=request.POST.get("CANo")
        CPANNo=request.POST.get("CPANNo")
        GName=request.POST.get("GName")
        GANo=request.POST.get("GANo")
        GPANNo=request.POST.get("GPANNo")
        rid_id=request.POST.get("rid_id")
        curr = connection.cursor()
        try:
            curr.execute("INSERT INTO child_app_child VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [Child_id,First_Name,Last_Name,DOB,DOA,CPhoto,CANo,CPANNo,GName,GANo,GPANNo,rid_id])
            messages.success(request,"Successfully Added Child")
            return HttpResponseRedirect(reverse("add_child"))
        except:
            messages.error(request,"Failed to Add Child")
            return HttpResponseRedirect(reverse("add_child"))
def add_room_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        room_id=request.POST.get("room_id")
        floor=int(request.POST.get("floor"))
        max_occupancy=int(request.POST.get("max_occupancy"))
        curr = connection.cursor()
        try:
            curr.execute("INSERT INTO child_app_room VALUES (%s, %s, %s)", [room_id,floor,max_occupancy])
            messages.success(request,"Successfully Added Room")
            return HttpResponseRedirect(reverse("add_room"))
        except:
            messages.error(request,"Failed to Add Room")
            return HttpResponseRedirect(reverse("add_room"))

def add_medical_history_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        mno=request.POST.get("mno")
        datech=parse_date(request.POST.get("datech"))
        mtype=bool(request.POST.get("mtype"))
        rlink=request.POST.get("rlink")
        cid=request.POST.get("cid")
        curr = connection.cursor()
        try:
            curr.execute("INSERT INTO child_app_medical_history VALUES (%s, %s, %s, %s, %s)", [mno,datech,mtype,rlink,cid])
            messages.success(request,"Successfully Added Medical History")
            return HttpResponseRedirect(reverse("add_medical_history"))
        except:
            messages.error(request)
            return HttpResponseRedirect(reverse("add_medical_history"))


def add_room(request):
    return render(request,"admindb_template/add_room_template.html")



def add_office_bearers(request):
    return render(request,"admindb_template/add_office_bearers_template.html")

def add_office_bearers_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        chair_no=request.POST.get("chair_no")
        position=request.POST.get("position")
        eid_id=request.POST.get("eid_id")
        curr = connection.cursor()
        try:
            curr.execute("INSERT INTO child_app_office_bearers VALUES (%s, %s, %s)", [chair_no,position,eid_id])
            messages.success(request,"Successfully Added Office Bearer")
            return HttpResponseRedirect(reverse("add_office_bearers"))
        except:
            messages.error(request)
            return HttpResponseRedirect(reverse("add_office_bearers"))
            
def add_donation_history(request):
    return render(request,"admindb_template/add_donation_history_template.html")

def add_donation_history_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        Don_id=request.POST.get("don_id")
        DName=request.POST.get("DName")
        DPanno=request.POST.get("DPanno")
        Ddate=parse_date(request.POST.get("Ddate"))
        Amt=int(request.POST.get("Amt"))
        curr = connection.cursor()
        try:
            curr.execute("INSERT INTO child_app_donation_history VALUES (%s, %s, %s, %s, %s)", [Don_id,DName,DPanno,Ddate,Amt])
            messages.success(request,"Successfully Added Donation History")
            return HttpResponseRedirect(reverse("add_donation_history"))
        except:
            messages.error(request,"Failed to Add Donation History")
            return HttpResponseRedirect(reverse("add_donation_history"))

def add_employee(request):
    return render(request,"admindb_template/add_employee_template.html")

def add_employee_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Emp_id=request.POST.get("Emp_id")
        PhNum=request.POST.get("PhNum")
        EANo=request.POST.get("EANo")
        DOJ=parse_date(request.POST.get("DOJ"))
        RType=request.POST.get("RType")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.employee.Emp_id=Emp_id
            user.employee.PhNum=PhNum
            user.employee.EANo=EANo
            user.employee.DOJ=DOJ
            user.employee.RType=RType
            user.save()
            messages.success(request,"Successfully Added Employee")
            return HttpResponseRedirect(reverse("add_employee"))
        except:
            messages.error(request,"Failed to Add Employee")
            return HttpResponseRedirect(reverse("add_employee"))

def manage_child(request):
    childrens = Child.objects.raw('SELECT * FROM child_app_child')
    return render(request,"admindb_template/manage_child_template.html", {"childrens":childrens})

def manage_room(request):
    rooms = Room.objects.raw('SELECT * FROM child_app_room')
    return render(request,"admindb_template/manage_room_template.html", {"rooms":rooms})

def manage_medical_history(request):
    medicalhistory = Medical_History.objects.raw('SELECT * FROM child_app_medical_history')
    return render(request,"admindb_template/manage_medical_history_template.html", {"medicalhistory":medicalhistory})

def manage_office_bearers(request):
    officeBearers = Office_Bearers.objects.raw('SELECT * FROM child_app_office_bearers')
    return render(request,"admindb_template/manage_office_bearers_template.html", {"officeBearers":officeBearers})

def manage_donation_history(request):
    donations = Donation_History.objects.raw('SELECT * FROM child_app_donation_history')
    return render(request,"admindb_template/manage_donation_history_template.html", {"donations":donations})

def manage_employee(request):
    employees=Employee.objects.all()
    return render(request,"admindb_template/manage_employee_template.html", {"employees":employees})

def edit_child(request,Child_id):
    child=Child.objects.raw('SELECT * FROM child_app_child WHERE Child_id = %s',[Child_id])[0]
    return render(request,"admindb_template/edit_child_template.html",{"child":child})

def edit_child_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        Child_id=request.POST.get("Child_id")
        First_Name=request.POST.get("First_Name")
        Last_Name=request.POST.get("Last_Name")
        DOB=parse_date(request.POST.get("DOB"))
        DOA=parse_date(request.POST.get("DOA"))
        CPhoto=request.POST.get("CPhoto")
        CANo=request.POST.get("CANo")
        CPANo=request.POST.get("CPANo")
        GName=request.POST.get("GName")
        GANo=request.POST.get("GANo")
        GPANo=request.POST.get("GPANo")
        rid_id=request.POST.get("rid")
        curr = connection.cursor()
        try:
            curr.execute("UPDATE child_app_child SET First_Name = %s,Last_Name = %s,DOB = %s,DOA = %s,CPhoto = %s,CANo = %s,CPANo = %s,GName = %s,GANo = %s,GPANo = %s,rid_id = %s  WHERE child_id = %s", [First_Name,Last_Name,DOB,DOA,CPhoto,CANo,CPANo,GName,GANo,GPANo,rid_id,Child_id])
            messages.success(request,"Successfully Edited Child Details")
            return HttpResponseRedirect("/edit_child/"+Child_id)
        except:
            messages.error(request)
            return HttpResponseRedirect("/edit_child/"+Child_id)

def edit_room(request,room_id):
    room=Room.objects.raw('SELECT * FROM child_app_room WHERE room_id = %s',[room_id])[0]
    return render(request,"admindb_template/edit_room_template.html",{"room":room})

def edit_room_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        room_id=request.POST.get("room_id")
        floor=int(request.POST.get("floor"))
        max_occupancy=int(request.POST.get("max_occupancy"))
        curr = connection.cursor()
        try:
            curr.execute("UPDATE child_app_room SET floor = %s, max_occupancy = %s WHERE room_id = %s", [floor,max_occupancy,room_id])
            messages.success(request,"Successfully Edited Room Details")
            return HttpResponseRedirect("/edit_room/"+room_id)
        except:
            messages.error(request,"Failed to Edit Room Details")
            return HttpResponseRedirect("/edit_room/"+room_id)

def edit_medical_history(request,mno):
    medicalhistory= Medical_History.objects.raw('SELECT * FROM child_app_medical_history WHERE mno = %s',[mno])[0]
    return render(request,"admindb_template/edit_medical_history_template.html",{"medicalhistory":medicalhistory})

def edit_medical_history_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mno=request.POST.get("mno")
        datech=parse_date(request.POST.get("datech"))
        rlink=(request.POST.get("rlink"))
        mtype=bool(request.POST.get("mtype"))
        cid_id=request.POST.get("cid")
        curr = connection.cursor()
        try:
            curr.execute("UPDATE child_app_medical_history SET datech = %s,rlink = %s,mtype =%s, cid_id =%s WHERE mno = %s", [datech,rlink,mtype,cid_id,mno])
            messages.success(request,"Successfully Edited Medical History Details")
            return HttpResponseRedirect("/edit_medical_history/"+mno)
        except:
            messages.error(request,"Failed to Edit Medical History Details")
            return HttpResponseRedirect("/edit_medical_history/"+mno)


def edit_office_bearers(request,chair_no):
    officeBearers=Office_Bearers.objects.raw('SELECT * FROM child_app_office_bearers WHERE chair_no = %s',[chair_no])[0]
    return render(request,"admindb_template/edit_office_bearers_template.html",{"officeBearers":officeBearers})

def edit_office_bearers_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        chair_no=request.POST.get("chair_no")
        position=request.POST.get("position")
        eid_id=request.POST.get("eid")
        curr = connection.cursor()
        try:
            curr.execute("UPDATE child_app_office_bearers SET position = %s, eid_id=%s WHERE chair_no = %s", [position,eid_id,chair_no])
            messages.success(request,"Successfully Edited Office Bearer Details")
            return HttpResponseRedirect("/edit_office_bearers/"+chair_no)
        except:
            messages.error(request,"Failed to Edit Office Bearer Details")
            return HttpResponseRedirect("/edit_office_bearers/"+chair_no)

def edit_donation_history(request,Don_id):
    donation=Donation_History.objects.raw('SELECT * FROM child_app_donation_history WHERE Don_id = %s',[Don_id])[0]
    return render(request,"admindb_template/edit_donation_history_template.html",{"donation":donation})

def edit_donation_history_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        Don_id=request.POST.get("Don_id")
        DName=request.POST.get("DName")
        DPanno=request.POST.get("DPanno")
        Ddate=parse_date(request.POST.get("Ddate"))
        Amt=int(request.POST.get("Amt"))
        curr = connection.cursor()
        try:
            curr.execute("UPDATE child_app_donation_history SET DName = %s, DPanno = %s,Ddate = %s,Amt = %s WHERE Don_id = %s", [DName,DPanno,Ddate,Amt,Don_id])
            messages.success(request,"Successfully Edited Donation Details")
            return HttpResponseRedirect("/edit_donation_history/"+Don_id)
        except:
            messages.error(request,"Failed to Edit Donation Details")
            return HttpResponseRedirect("/edit_donation_history/"+Don_id)

def edit_employee(request,emp_no):
    emp=Employee.objects.get(admin=emp_no)
    return render(request,"admindb_template/edit_employee_template.html", {"emp":emp,"emp_no":emp_no})

def edit_employee_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        emp_no=request.POST.get("emp_no")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        Emp_id=request.POST.get("Emp_id")
        PhNum=request.POST.get("PhNum")
        EANo=request.POST.get("EANo")
        DOJ=parse_date(request.POST.get("DOJ"))
        RType=request.POST.get("RType")

        try:
            user=CustomUser.objects.get(id=emp_no)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            employee=Employee.objects.get(admin=emp_no)
            employee.Emp_id=Emp_id
            employee.PhNum=PhNum
            employee.EANo=EANo
            employee.DOJ=DOJ
            employee.RType=RType
            employee.save()
            messages.success(request,"Successfully Edited Employee")
            return HttpResponseRedirect("/edit_employee/"+emp_no)
        except:
            messages.error(request,"Failed to Edit Employee")
            return HttpResponseRedirect("/edit_employee/"+emp_no)