from django.urls import path
from . import views

urlpatterns = [
    path('web',views.testfun,name='web')
]
