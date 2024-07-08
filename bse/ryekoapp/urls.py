# creating this url so that we define url patent that maps to the route(app directory)
print("here Loading ryekoapp/urls.py")
# from django.urls import path
# from .views import moisture_list_view

# urlspatterns = [
#     path('', moisture_list_view, name='moisture_list'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.moisture_list_view, name='moisture_list'),
]