from django.contrib import admin
from .models import Portfolio,Project,Education,Skill,Experience,Template
# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Template)
