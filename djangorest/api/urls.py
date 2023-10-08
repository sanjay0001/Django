from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show),
    path('add/',views.add),
    path("get/<str:id>/",views.get),
    path("display/",views.Display.as_view()),
    path("display/<str:id>",views.Display.as_view()),
    path("list/",views.CustomListView.as_view())
]
