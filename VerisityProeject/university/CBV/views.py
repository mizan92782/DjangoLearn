import django.http
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# view cbv
class simpleCBV(View):
  def get(self,request):
    print("This is a simple CBV GET request.")
    return HttpResponse("Hello, this is a simple CBV response.")
  def post(self,request):    
    return HttpResponse("This is a POST request response from a simple CBV.")


# template cbv
class templeteCVB(TemplateView):
    #show this template when this view is called:must be in the templates folder
    
    template_name = "CBV/templete.html" # Specify the template to be used
    
    '''
     1. first get show wellcame message
     2.after submit post will repalce the message by given name in templet
     ** by using it it very easy to change the templete **
    
    '''

    def get(self, request, *args, **kwargs):
        # Handle GET request
        
        #get context data
        context = self.get_context_data(**kwargs)
        #pass value by context
        context['message'] = 'Welcome to the home page!'
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # Handle POST request (for example, form submission)
        name = request.POST.get('name')  # get data from submitted form
        context = self.get_context_data(**kwargs)
        context['message'] = f'Hello, {name}!'
        return self.render_to_response(context)
      



from django.views.generic.base import RedirectView


from django.views.generic.base import RedirectView

class DynamicRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user

        if user.is_authenticated:
          
          # go to admin paned id it be a user
            if user.is_superuser:
                return '/admin/'
              #for other user if uer not be a admin
            else:
                return '/students/home/'
            
        else:
            # not logged in users
            return '/login/'


from django.views.generic.edit import CreateView
from .models import Friends  # Assuming you have a model named Friends

#! crated view  that crate a instance of a model
class FriendsCreateView(CreateView):
    model = Friends  # Assuming you have a model named Friends
    template_name = "CBV/student_create.html"
    fields = ['first_name', 'last_name', 'home', 'email'] 
    
    #! using this i have to give full path ,but if use reverse_lazy i can use the name of the url
    #success_url='list_view' 
    success_url = reverse_lazy('list_view')
    
    

from django.views.generic.list import ListView
class FriedsListView(ListView):
    model = Friends
    context_object_name = 'info'
    template_name='CBV/list_view.html'
    


from django.views.generic.edit import UpdateView

class FriendsUpdateView(UpdateView):
    model = Friends  # Assuming you have a model named Friends
    template_name = "CBV/friend_update.html"
    fields = ['first_name', 'last_name', 'home', 'email'] 
    
    #! using this i have to give full path ,but if use reverse_lazy i can use the name of the url
    #success_url='list_view' 
    success_url = reverse_lazy('list_view')
    