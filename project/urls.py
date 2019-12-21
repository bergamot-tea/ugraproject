from django.urls import path
from . views import summary_project_view, ProjectDetailView
from . views import summary_member_view, MemberDetailView

app_name = 'project'

urlpatterns = [

    path('', summary_project_view, name='summary_page'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path('member/', summary_member_view, name='summary_member_page'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member'),
]