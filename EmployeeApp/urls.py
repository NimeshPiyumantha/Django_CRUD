from django.urls import path, include
from EmployeeApp import views

urlpatterns=[
                    path('department/', views.departmentApi),
                    path('department/<int:id>', views.departmentApi),
]