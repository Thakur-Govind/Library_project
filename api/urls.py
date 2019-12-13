from django.urls import path
#from .models import BooksConfig
from .views import BookAPIView,BookDetail,UserList,UserDetail

urlpatterns = [

    path('', BookAPIView.as_view()),
    path('bd/<str:pk>/' ,BookDetail.as_view()),
    #title is the primary key
    path('users/', UserList.as_view()),
    path('users/<int:pk>/',UserDetail.as_view())

]
