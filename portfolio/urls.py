from django.contrib import admin
from django.urls import path,include
from .views import portfolio_view, project_view, education_view, experience_view, skill_view,show,form_show,handle_mail,save_template

urlpatterns = [
    path('<uuid:uuid>/',show,name='user_website'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('project/', project_view, name='project'),
    path('education/', education_view, name='education'),
    path('experience/', experience_view, name='experience'),
    path('skill/', skill_view, name='skill'),
    path('portfolio-form/', form_show, name='portfolio_form'),
    path('send-mail/<uuid:uid>',handle_mail,name='send_mail'),
    path('save-template/<template>',save_template,name='save_template'),
]