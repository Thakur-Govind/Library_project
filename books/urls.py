from django.urls import path
from . import views
urlpatterns = [
path('', views.BookListView.as_view(), name = 'home'),
path('add/', views.addbook, name = 'add'),
path('create',views.create, name = 'create'),
path('<str:bookt>',views.bookdetail, name='details'),
path('/up/<str:bookt>/',views.updatebook, name = 'ubook'),
path('update/<str:bookt>', views.update, name = 'update')
#path('', views.logIn, name = 'logIn'),
#path('signUp', views.signUp, name = 'signUp'),

]
