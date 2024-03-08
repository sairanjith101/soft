from django.shortcuts import render,redirect
from CRUD_app.models import Student
from CRUD_app.forms import StudentForm

# Create your views here.
def retrive(request):
    student = Student.objects.all()
    return render(request, 'CRUD_app/index.html', {'student': student})

def create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'CRUD_app/create.html', {'form': form})

def delete_view(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/check')

def update_view(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'CRUD_app/update.html', {'student': student})

