from django.urls import path
from . import views



urlpatterns = [
    path('create',views.create,name='create'),
    path('<int:invoice_id>',views.detail, name="detail"),
    path('home/<int:pk>',views.delete, name="delete"),
    # path('<int:invoice_id/home>',views.delete, name="delete"),
]