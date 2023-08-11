from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from app.models import Person
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        roll=request.POST['roll']
        email=request.POST['email']
        Myuser=Person(first_name=fname,last_name=lname,roll_number=roll,email=email)
        Myuser.save()
        # print(fname,lname,roll,email)
        
        return redirect('index')
    return render(request,'index.html')


def adminpage(request):
    person=Person.objects.all()
    print(person)
    pp={'p':person,'k':'ajith is here'}
    return render(request,'adminpage.html',pp)

def delete_row(request, row_id):
    to_delete = get_object_or_404(Person, id=row_id)
    to_delete.delete() 

    messages.warning(request, "Row deleted successf ully!")
    return redirect('adminpage')

def edit_row(request, row_id):
    obj_to_edit = get_object_or_404(Person, id=row_id)
    if request.method == 'POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        roll=request.POST['roll']
        email=request.POST['email']
        
        obj_to_edit.roll_number=roll
        obj_to_edit.first_name=fname
        obj_to_edit.last_name=lname
        obj_to_edit.email=email
        obj_to_edit.save()
        messages.warning(request, "edited succesfully")
        return redirect('adminpage')
    context={'obj':obj_to_edit}

    return render(request, 'edittTable.html', context)