from django.shortcuts import render
from django.views import View #View class to handle requests
from django.http import HttpResponse #this is our responses
from django.views.generic.base import TemplateView
from .models import Dog, DogToy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


# class Dog:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# dogs = [
#     Dog("Bark", 4, "Female"),
#     Dog("Clifford", 103, "Male"),
#     Dog("Growlithe", 25, "Male"),
#     Dog("Doggo", 500, "Male"),
# ]

class Dog_List(TemplateView):
    template_name = 'doglist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #this gets the name query parameter to acces it
        name = self.request.GET.get('name')
        #if the query exists, we weill filter by name
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["dogs"] = Dog.objects.filter(name__icontains=name)
            context['header'] = f"searching for {name}"
        else:
            context['dogs'] = Dog.objects.all() # this is where we add the key into our context object for the view to use
            context['header'] = "Our Dogs"
        return context


class Dog_Create(CreateView):
    model = Dog
    fields = ['name', 'img', 'age', 'gender', 'dogtoys', 'user']
    template_name = 'dog_create.html'
    success_url = '/dogs/'
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})



class Dog_Detail(DetailView):
    model = Dog
    template_name = 'dog_detail.html'


class Dog_Update(UpdateView):
    model = Dog
    fields = ['name', 'img', 'age', 'gender', 'dogtoys']
    template_name = "dog_update.html"
    # success_url = "/cats/"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})


class Dog_Delete(DeleteView):
    model = Dog
    template_name = 'dog_delete_confirmation.html'
    success_url = '/dogs'


# Profile for the user
def profile(request, username):
    user = User.objects.get(username = username)
    # user = User.objects.get(username = 'romebell')
    dogs = Dog.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'dogs': dogs})




def dogtoys_index(request):
    dogtoys = DogToy.objects.all()
    return render(request, 'dogtoy_index.html', {'dogtoys': dogtoys})

def dogtoys_show(request, dogtoy_id):
    dogtoy = DogToy.objects.get(id=dogtoy_id)
    return render(request, 'dogtoy_show.html', {'dogtoy': dogtoy})

class DogToyCreate(CreateView):
    model = DogToy
    fields = '__all__'
    template_name = "dogtoy_form.html"
    success_url = '/dogtoys'

class DogToyUpdate(UpdateView):
    model = DogToy
    fields = ['name', 'color']
    template_name = "dogtoy_update.html"
    success_url = '/dogtoys'

class DogToyDelete(DeleteView):
    model = DogToy
    template_name = "dogtoy_confirm_delete.html"
    success_url = '/dogtoys'