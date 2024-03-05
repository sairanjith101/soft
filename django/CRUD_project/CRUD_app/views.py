from django.shortcuts import render
from CRUD_app.models import Student

# Create your views here.
def retrive(request):
    student = Student.objects.all()
    return render(request, 'CRUD_app/index.html', {'student': student})
