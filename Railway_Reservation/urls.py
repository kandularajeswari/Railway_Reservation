"""Railway_Reservation URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Railway import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Railway/', include('Railway.urls')),
    path('home/',views.home,name="hom" ),
    path('log/',views.log,name='log'),
    path('logout/',views.logout ),
    path('Reg/',views.Reg,name='Reg'),
    path('search/',views.search),
    path('search/trains',views.getTrains),
    path('schedule/',views.schedule),
    path('schedule/trains/',views.getTinfo),
    path('addR/',views.addR,name="addR"),
    path('addST/',views.addST),
    path('addT/',views.addT),
    path('addRT/',views.addRT),
    path('search/search/trains/cva/',views.cva),
    path('search/book1/',views.book1),
    path('search/book1/book/',views.book),
    path('cancel/',views.cancel),
    path('cancel/cancel/cn/',views.cn),
    path('pnr/',views.pnr,name="pnr"),






]
