"""home_automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lights.api_views import LightList, LightCreate, LightRetrieveUpdateDestroy
from thermostat.api_views import TemperatureList, TemperatureCreate, TemperatureRetrieveUpdate

urlpatterns = [
    path('api/v1/lights/', LightList.as_view()),
    path('api/v1/thermostat/', TemperatureList.as_view()),
    path('api/v1/lights/new', LightCreate.as_view()),
    path('api/v1/thermostat/new', TemperatureCreate.as_view()),
    path('api/v1/lights/<int:id>/', 
        LightRetrieveUpdateDestroy.as_view()
    ),
    path('api/v1/thermostate/<int:id>/', TemperatureRetrieveUpdate.as_view()),

    path('admin/', admin.site.urls),
]
