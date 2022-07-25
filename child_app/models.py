from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"DBManager"), (2, "Employee"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminDB(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    Emp_id = models.CharField(max_length = 5, unique = True)
    PhNum = models.CharField(max_length = 10)
    EANo = models.CharField(max_length = 12)
    DOJ = models.DateField()
    RType = models.CharField(max_length = 10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Donation_History(models.Model):
    Don_id = models.CharField(max_length = 5, primary_key=True)
    DName = models.CharField(max_length = 20)
    DPanno = models.CharField(max_length = 10)
    Ddate = models.DateField()
    Amt = models.IntegerField()
    objects = models.Manager()
class Room(models.Model):
    room_id = models.CharField(max_length = 5, primary_key=True)
    floor = models.IntegerField()
    max_occupancy = models.IntegerField()
    objects = models.Manager()

class Child(models.Model):
    Child_id = models.CharField(max_length = 5, primary_key=True)
    First_Name = models.CharField(max_length = 20)
    Last_Name = models.CharField(max_length = 20)
    DOB = models.DateField()
    DOA = models.DateField()
    CPhoto = models.CharField(max_length = 40)
    CANo = models.CharField(max_length = 12)
    CPANo = models.CharField(max_length = 20)
    GName = models.CharField(max_length = 20)
    GANo = models.CharField(max_length = 20)
    GPANo = models.CharField(max_length = 20)
    rid = models.ForeignKey(Room,on_delete=models.CASCADE)
    objects = models.Manager()

class Medical_History(models.Model):
    mno = models.CharField(max_length = 5, primary_key=True)
    cid = models.ForeignKey(Child,on_delete=models.CASCADE)
    datech = models.DateField()
    mtype = models.BooleanField()
    rlink = models.CharField(max_length = 20)
    objects = models.Manager()
    

class Office_Bearers(models.Model):
    chair_no = models.CharField(max_length = 5, primary_key=True)
    position = models.CharField(max_length = 20)
    eid = models.ForeignKey(Employee,on_delete=models.CASCADE)
    objects = models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminDB.objects.create(admin=instance)
        if instance.user_type==2:
            Employee.objects.create(admin=instance,Emp_id="",PhNum="",EANo="",DOJ="2020-01-01",RType="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admindb.save()
    if instance.user_type==2:
        instance.employee.save()
