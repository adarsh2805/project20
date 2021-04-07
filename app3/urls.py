from django.urls import path
from app3 import views

app_name='app3'
urlpatterns = [
    
    path('<name>',views.sample3,name='sample3')
]
