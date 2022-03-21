from django.urls import path
from .views import (
    home,
)
app_name = 'forntend_panel'

urlpatterns = [
    path('' ,home, name='home'),
]
