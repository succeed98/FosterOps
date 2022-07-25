"""OrphanageDBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from OrphanageDBMS import settings
from child_app import views, AdminDBvIews, EmployeeDBviews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',AdminDBvIews.admin_home,name="admin_home"),
    path('employee_home',EmployeeDBviews.employee_home,name="employee_home"),
    path('add_child',AdminDBvIews.add_child,name="add_child"),
    path('add_child_save',AdminDBvIews.add_child_save,name="add_child_save"),
    # path('add_child_save',AdminDBvIews.add_child_save,name="add_child_save"),
    path('add_medical_history',AdminDBvIews.add_medical_history,name="add_medical_history"),
    path('add_medical_history_save',AdminDBvIews.add_medical_history_save,name="add_medical_history_save"),
    path('add_office_bearers',AdminDBvIews.add_office_bearers,name="add_office_bearers"),
    path('add_office_bearers_save',AdminDBvIews.add_office_bearers_save,name="add_office_bearers_save"),
    path('add_room',AdminDBvIews.add_room,name="add_room"),
    path('add_room_save',AdminDBvIews.add_room_save,name="add_room_save"),
    path('add_donation_history',AdminDBvIews.add_donation_history,name="add_donation_history"),
    path('add_donation_history_save',AdminDBvIews.add_donation_history_save,name="add_donation_history_save"),
    path('add_employee',AdminDBvIews.add_employee,name="add_employee"),
    path('add_employee_save',AdminDBvIews.add_employee_save,name="add_employee_save"),
    path('manage_child',AdminDBvIews.manage_child,name="manage_child"),
    path('manage_medical_history',AdminDBvIews.manage_medical_history,name="manage_medical_history"),
    path('manage_room',AdminDBvIews.manage_room,name="manage_room"),
    path('manage_room_emp',EmployeeDBviews.manage_room_emp,name="manage_room_emp"),
    path('manage_child_emp',EmployeeDBviews.manage_child_emp,name="manage_child_emp"),
    path('manage_medical_history_emp',EmployeeDBviews.manage_medical_history_emp,name="manage_medical_history_emp"),
    path('manage_donation_history_emp',EmployeeDBviews.manage_donation_history_emp,name="manage_donation_history_emp"),
    path('manage_donation_history',AdminDBvIews.manage_donation_history,name="manage_donation_history"),
    path('manage_employee',AdminDBvIews.manage_employee,name="manage_employee"),
    path('manage_office_bearers',AdminDBvIews.manage_office_bearers,name="manage_office_bearers"),
    path('edit_child/<str:Child_id>', AdminDBvIews.edit_child,name="edit_child"),
    path('edit_child_save', AdminDBvIews.edit_child_save,name="edit_child_save"),
    path('edit_medical_history/<str:mno>', AdminDBvIews.edit_medical_history,name="edit_medical_history"),
    path('edit_medical_history_save', AdminDBvIews.edit_medical_history_save,name="edit_medical_history_save"),
    path('edit_office_bearers/<str:chair_no>', AdminDBvIews.edit_office_bearers,name="edit_office_bearers"),
    path('edit_office_bearers_save', AdminDBvIews.edit_office_bearers_save,name="edit_office_bearers_save"),
    path('edit_room/<str:room_id>', AdminDBvIews.edit_room,name="edit_room"),
    path('edit_room_save', AdminDBvIews.edit_room_save,name="edit_room_save"),
    path('edit_donation_history/<str:Don_id>', AdminDBvIews.edit_donation_history,name="edit_donation_history"),
    path('edit_donation_history_save', AdminDBvIews.edit_donation_history_save,name="edit_donation_history_save"),
    path('edit_employee/<str:emp_no>', AdminDBvIews.edit_employee,name="edit_employee"),
    path('edit_employee_save', AdminDBvIews.edit_employee_save,name="edit_employee_save"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
