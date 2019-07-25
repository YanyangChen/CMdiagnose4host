from django.urls import path

from . import views

app_name = 'CMdiagnose'
urlpatterns = [
    path('index', views.BootIndexView.as_view(), name='bootindex'),
    path('', views.IndexView.as_view(), name='index'),
    path('create1/', views.NewDetailView.as_view(), name='newdetail'),
    path('createy/', views.NewDetailYao.as_view(), name='newdetailyao'),
    path('createx/', views.NewDetailXue.as_view(), name='newdetailxue'),
    path('new/', views.newPerson, name='new'),
    path('newext/', views.newPersonExt, name='newext'),
    path('newx/', views.newXue, name='newx'),
    path('newy/', views.newYao, name='newy'),
    path('newyext/', views.newYaoExt, name='newyext'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/resultsy/', views.ResultsYao.as_view(), name='resultsy'),
    path('<int:pk>/resultsxue/', views.ResultsXue.as_view(), name='resultsxue'),
    path('<int:person_id>/tell/', views.tell, name='tell'),
    path('listxue', views.ListXue.as_view()),
    path('listxue/<int:pk>/', views.DetailXue.as_view()),
    
]