from django.urls import path
from . views import summary_project_view, ProjectDetailView
from . views import summary_member_view, MemberDetailView
from . views import summary_report_view, ReportDetailView
from . views import project_chat_view
from . views import summary_opendata_view, project_opendata_view

app_name = 'project'

urlpatterns = [

    path('', summary_project_view, name='summary_page'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/chat', project_chat_view, name='chat'),
    path('member/', summary_member_view, name='summary_member_page'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member'),
    path('report/', summary_report_view, name='summary_report_page'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report'),
    path('opendata/', summary_opendata_view, name='summary_opendata_page'),
    path('opendata/<fed_project>/', project_opendata_view, name='project_opendata_page'),
]