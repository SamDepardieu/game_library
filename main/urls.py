from django.urls import path
from .views import home, consoles

urlpatterns = [
    path(
        '',
        home.IndexView.as_view(),
        name='index'
    ),
    path(
        'console',
        consoles.ConsoleListView.as_view(),
        name='console_list'
    ),
    path(
        'console/add',
        consoles.ConsoleAddView.as_view(),
        name='console_add'
    ),
    path(
        'console/<int:pk>',
        consoles.ConsoleShowView.as_view(),
        name='console_show'
    ),
    path(
        'console/<int:pk>/update',
        consoles.ConsoleUpdateView.as_view(),
        name='console_edit'
    ),
    path(
        'console/<int:pk>/delete',
        consoles.ConsoleDeleteView.as_view(),
        name='console_delete'
    ),
]
