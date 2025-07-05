import django.shortcuts
from .models import Views
from .forms import UpdateForm

# Create your views here.



# view all instance of view model
def Viewsall(request):
  #taking all object
  data=Views.objects.all()
  return django.shortcuts.render(request, 'view/allview.html', {'data': data})


# view single instance of view model or by view_id
def ViewsSearch(request,view_id):
  #taking all object
  data=Views.objects.all().filter(view_id=view_id)
  return django.shortcuts.render(request, 'view/allview.html', {'data': data})




#update value
def ViewsUpdate(request,view_id):
  #taking object by view_id
  obj = django.shortcuts.get_object_or_404(Views, view_id=view_id)
  if request.method == 'POST':
    form = UpdateForm(request.POST, instance=obj)
    if form.is_valid():
      form.save()
      #! Redirect to the viewsearch page after updating by view_id
      return django.shortcuts.redirect('viewsearch',view_id=view_id)
  else:
    form = UpdateForm(instance=obj)
  return django.shortcuts.render(request, 'view/updateview.html', {'form': form})
    
  
  
  
  