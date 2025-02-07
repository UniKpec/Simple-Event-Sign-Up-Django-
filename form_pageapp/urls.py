from django.urls import path
from . import views

app_name = 'form_pageapp'

urlpatterns = [
    path("sign-up/",views.registrationuserform,name='registrationuserform'),
]