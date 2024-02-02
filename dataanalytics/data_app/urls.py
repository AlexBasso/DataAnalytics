from django.urls import path, include
from .views import main_view

app_name = 'data_app'

urlpatterns = [
    path('', main_view, name='home'),

]
