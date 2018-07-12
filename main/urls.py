from django.urls import path
from .views import home, consoles, game_types

urlpatterns = [
    path(
        '',
        home.IndexView.as_view(),
        name='index'
    )
]

# Adds console views urls
urlpatterns += [
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
    )
]

# Adds game_type views urls
urlpatterns += [
    path(
        'gametype',
        game_types.GameTypeListView.as_view(),
        name='game_type_list'
    ),
    path(
        'gametype/add',
        game_types.GameTypeAddView.as_view(),
        name='game_type_add'
    ),
    path(
        'gametype/<int:pk>',
        game_types.GameTypeShowView.as_view(),
        name='game_type_show'
    ),
    path(
        'gametype/<int:pk>/update',
        game_types.GameTypeUpdateView.as_view(),
        name='game_type_edit'
    ),
    path(
        'gametype/<int:pk>/delete',
        game_types.GameTypeDeleteView.as_view(),
        name='game_type_delete'
    )
]
