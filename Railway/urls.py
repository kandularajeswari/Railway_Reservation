from django.contrib import admin
from django.urls import path,include
from Railway import views
urlpatterns = [
    path('home/',views.home,name="hom" ),
    path('log/',views.log,name='log'),
    path('logout/',views.logout ),
    path('Reg/',views.Reg,name='Reg'),
    path('search/',views.search),
    path('search/trains/',views.getTrains),
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
