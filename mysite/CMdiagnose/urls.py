from django.urls import path
from rest_framework import routers

from . import views

app_name = 'CMdiagnose'
urlpatterns = [
    path('index', views.BootIndexView.as_view(), name='bootindex'),
    path('', views.IndexView.as_view(), name='index'),
    path('create1/', views.NewDetailView.as_view(), name='newdetail'),
    path('createh/', views.NewDetailViewh.as_view(), name='newdetailh'),
    path('createy/', views.NewDetailYao.as_view(), name='newdetailyao'),
    path('createx/', views.NewDetailXue.as_view(), name='newdetailxue'),
    path('new/', views.newPerson, name='new'),
    path('newext/', views.newCasesExt, name='newext'),
    path('newexth/', views.newHcasesExth, name='newexth'),
    path('searchc/', views.newCasesExt2, name='newext2'),
    path('newx/', views.newXue, name='newx'),
    path('searchx/', views.newXue2, name='newx2'),
    path('listx/', views.XueList.as_view(), name='newx3'),
    path('listy/', views.YaoList.as_view(), name='newy3'),
    path('listf/', views.FangList.as_view(), name='newy3'),
    path('zlistx/', views.zXueList.as_view(), name='newxz'),
    path('zlisty/', views.zYaoList.as_view(), name='newyz'),
    path('zlistf/', views.zFangList.as_view(), name='newyz'),
    path('newy/', views.newYao, name='newy'),
    path('searchy/', views.newYaoExt2, name='newyext2'),
    path('newyext/', views.newYaoExt, name='newyext'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/resultsh/', views.ResultsHcases.as_view(), name='resultsh'),
    path('<int:pk>/resultsy/', views.ResultsYao.as_view(), name='resultsy'),
    path('<int:pk>/resultsxue/', views.ResultsXue.as_view(), name='resultsxue'),
    path('<int:person_id>/tell/', views.tell, name='tell'),
    path('listxue', views.ListXue.as_view()),
    path('xue/<name>/', views.MatchXue.as_view()),
    path('yao/<name>/', views.MatchYao.as_view()),
    path('cases/<name>/', views.MatchCases.as_view()),
    path('listxue/<int:pk>/', views.DetailXue.as_view()),
    
]

