from django.urls import path
from . views import summary_issue_view, issue_view

app_name = 'issue'

urlpatterns = [

    path('', summary_issue_view, name='summary_issue_page'),
    path('<int:pk>/', issue_view, name='issue'),
]