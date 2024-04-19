from django.urls import path
from . import views


app_name="accounts"

urlpatterns = [
    
    path('student/register',views.student_register,name="student_register"),
    path ("staff/register",views.staff_register,name="staff_register"),
    path("orgnaization/register",views.orgnaization_register,name="orgnaization_register"),
    path("organization/login/",views.organization_login,name="organization_login"),
    path("staff/login/",views.staff_login,name="staff_login"),
    path("student/login/",views.student_login,name="student_login"),
    path("logout/",views.user_logout,name="user_logout")
]
