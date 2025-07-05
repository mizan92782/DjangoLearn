from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    """
    Render the home page for the students section.
    """
    user=request.user
    
    
    return render(request, 'student/student_home.html',{'user':user})


# input taken from the user
def inputStudent(request):
    #if user clicks submit button
    if request.method=='POST':
        # 1. get the data from the form
        
        #take full data in object from form
        form =StudentForm(request.POST)
        
    
        ''' or cane take individual variables
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        batch = request.POST.get('batch')
        '''

        #2. validate the data:check use fill all fields
        if form.is_valid():
            #3. save the data to the database
            form.save()
            #4. create a response message to a file
            return redirect('output_students')
        

    else:
        # not valid data, render the form again or empty form
        form = StudentForm()
    
    
    # render the form in the template
    return render(request, 'student/input_student.html', {'form': form})
           



def  outputStudent(args):
    """
    Render the output page displaying all students.
    """
    # 1. get all the data from the database
    students = Student.objects.all()
    
    # 2. create a response message
    # 3. render the data in the template
    return render(args, 'student/output_student.html', {'students': students})


def studentBatch(request, batch):
    """
    Render the output page displaying students from a specific batch.
    """
    # 1. get all the data from the database for the specified batch
    students = Student.objects.filter(batch=batch)
    
    
    
    # 2. create a response message
    # 3. render the data in the template
    return render(request, 'student/batch_student.html', {'student': students})