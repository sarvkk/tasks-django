from django.urls import path
from . import views

urlpatterns=[
 path("isitnewyear",views.index,name="newyear"),
 path("ram",views.ram,name="ram")
]