from django.contrib import admin
from .models import Student
from .forms import StudentRegistration

# Register your models here.
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
