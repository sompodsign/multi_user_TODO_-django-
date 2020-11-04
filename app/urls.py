from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('signout', views.signout, name='signout'),
    path('delete_todo/<int:id>', views.delete_todo),
    path('change_todo/<int:id>/<str:status>', views.change_todo),




]
