from django.urls import path
from . views import summary_view

app_name = 'project'

urlpatterns = [

    path('', summary_view, name='summary_page'),

]