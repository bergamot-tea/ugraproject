from django.urls import path
from . views import summary_issue_view, IssueDetailView

app_name = 'issue'

urlpatterns = [

    path('', summary_issue_view, name='summary_issue_page'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue'),
]