"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from APP.views import login, index, MDT, MDT_2, MDDTable, SingleTable, SingleTable_2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('login.html', login),
    path('index.html', index),
    path('Master-Detail-Table.html', MDT),
    path('Master-Detail-Table-2.html', MDT_2),
    path('M-D-D-Table.html', MDDTable),
    path('Single-Table.html', SingleTable),
    path('Single-Table-2.html', SingleTable_2)
]

