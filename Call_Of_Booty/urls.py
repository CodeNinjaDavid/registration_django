from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('insert/', views.insert, name="insert"),
    path('people/', views.people, name="people"),
    path('contact_us/', views.contact, name="contact_us"),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update'),
]
