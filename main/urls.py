from main.views import index, contact, about, plan
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('apropos/', about, name="about"),
    path('assurance/plan/<int:pk>', plan, name="plan")
]
