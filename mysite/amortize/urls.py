from django.urls import path

from . import views

app_name = 'amortize'
urlpatterns = [
    path('', views.get_loan, name='loan'),
    path('', views.get_loan, name='mortgage'),
]
