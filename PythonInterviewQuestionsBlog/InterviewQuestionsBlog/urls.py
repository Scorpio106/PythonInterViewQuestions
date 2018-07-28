from django.conf.urls import url
from . import views
app_name = 'InterviewQuestionsBlog'
urlpatterns = [
    url(r'^IV/$', views.PythonInterViewQuestions.as_view(), name='questions'),

]