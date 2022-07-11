from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task


#Login Page
class CustomLoginView(LoginView):
    template_name= 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    #Override success url
    def get_success_url(self) -> str:
        return reverse_lazy('mytasks')

#Registration Page
class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('mytasks')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    #Redirect to tasks page once registered
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('mytasks')
        return super(RegisterPage, self).get(args, **kwargs)

#Task List Page
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'mytasks'

    #User Specific Data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mytasks'] = context['mytasks'].filter(user=self.request.user)
        context['count'] = context['mytasks'].filter(finished=False).count()

        #Search functionality
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['mytasks'] = context['mytasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        
        return context 

class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_details.html'

#Create a new Task
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'finished']
    success_url = reverse_lazy('mytasks')

    #form validation
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

#Update/Edit a Task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'finished']
    success_url = reverse_lazy('mytasks')

#Delete a Task
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('mytasks')
    template_name = 'todo/task_delete.html'

