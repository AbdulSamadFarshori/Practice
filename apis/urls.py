from .views import *
from django.urls import path

urlpatterns = [
    path('operations', OperationsApiView.as_view(), name='operations'),
    path('operations/<int:pk>', OperationsApiView.as_view(), name='operations'),

]
