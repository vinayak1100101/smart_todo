
from django.urls import path
from .views import*
urlpatterns = [
    path('',loginn),
    path('register/',register),
    path('loginn/',loginn),
    path('todo/',todo),
    path('delete/<int_id>', deleteedit, name="delete"),
    path('edit/<int_id>',editor,name="edit")
    
]