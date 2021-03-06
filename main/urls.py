from django.urls import path
from .views import home, consoles, game_types, groups, users, games

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

# Adds group views urls
urlpatterns += [
    path(
        'group',
        groups.GroupListView.as_view(),
        name='group_list'
    ),
    path(
        'group/add',
        groups.GroupAddView.as_view(),
        name='group_add'
    ),
    path(
        'group/<int:pk>',
        groups.GroupShowView.as_view(),
        name='group_show'
    ),
    path(
        'group/<int:pk>/update',
        groups.GroupUpdateView.as_view(),
        name='group_edit'
    ),
    path(
        'group/<int:pk>/delete',
        groups.GroupDeleteView.as_view(),
        name='group_delete'
    )
]

# Adds group users urls
urlpatterns += [
    path(
        'user',
        users.UserListView.as_view(),
        name='user_list'
    ),
    path(
        'user/add',
        users.UserAddView.as_view(),
        name='user_add'
    ),
    path(
        'user/<int:pk>',
        users.UserShowView.as_view(),
        name='user_show'
    ),
    path(
        'user/<int:pk>/update',
        users.UserUpdateView.as_view(),
        name='user_edit'
    ),
    path(
        'user/<int:pk>/delete',
        users.UserDeleteView.as_view(),
        name='user_delete'
    )
]

# Adds group games urls
urlpatterns += [
    path(
        'game',
        games.GameListView.as_view(),
        name='game_list'
    ),
    path(
        'game/add',
        games.GameAddView.as_view(),
        name='game_add'
    ),
    path(
        'game/<int:pk>',
        games.GameShowView.as_view(),
        name='game_show'
    ),
    path(
        'game/<int:pk>/update',
        games.GameUpdateView.as_view(),
        name='game_edit'
    ),
    path(
        'game/<int:pk>/delete',
        games.GameDeleteView.as_view(),
        name='game_delete'
    )
]
