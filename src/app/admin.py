from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(UC)
admin.site.register(Class)
admin.site.register(StudentUC)
admin.site.register(ClassUC)
admin.site.register(Composed)
admin.site.register(ComposedClasses)
admin.site.register(ScheduleSlot)
admin.site.register(Request)
admin.site.register(SingleRequest)
admin.site.register(Rating)