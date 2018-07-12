from django.contrib.auth.models import Group
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class GroupListView(generic.ListView):
    template_name = 'main/group/list.html'
    model = Group


class GroupShowView(generic.DetailView):
    template_name = 'main/group/show.html'
    model = Group


class GroupAddView(CreateView):
    template_name = 'main/group/add.html'
    model = Group
    fields = ['name']
    success_url = '/group'


class GroupUpdateView(UpdateView):
    template_name = 'main/group/add.html'
    model = Group
    fields = ['name']
    success_url = '/group'


class GroupDeleteView(DeleteView):
    template_name = 'main/group/delete.html'
    model = Group
    success_url = '/group'
