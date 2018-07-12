from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class UserListView(generic.ListView):
    template_name = 'main/user/list.html'
    model = User


class UserShowView(generic.DetailView):
    template_name = 'main/user/show.html'
    model = User


class UserAddView(CreateView):
    template_name = 'main/user/add.html'
    model = User
    fields = ['username', 'password']
    success_url = '/user'


class UserUpdateView(UpdateView):
    template_name = 'main/user/add.html'
    model = User
    fields = ['username']
    success_url = '/user'


class UserDeleteView(DeleteView):
    template_name = 'main/user/delete.html'
    model = User
    success_url = '/user'
