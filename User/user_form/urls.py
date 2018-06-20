from django.urls import path
from . import views

app_name='user_form'

urlpatterns = [
        
    # /user_form/
    path('', views.user, name='user'),

]