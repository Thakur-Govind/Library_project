from django.urls import path
#from .models import BooksConfig
from .views import BookViewSet,UserViewSet
from .views import BookAPIView,BookDetail,UserList,UserDetail
from rest_framework.routers import SimpleRouter #THere are 2 types, were using
#the simple one here
"""
------------- Using Routers instead of the code below ------------------------
"""
urlpatterns = [

    path('', BookAPIView.as_view()),
    path('bd/<str:pk>/' ,BookDetail.as_view()),
    #title is the primary key
    path('users/', UserList.as_view()),
    path('users/<int:pk>/',UserDetail.as_view())

]
"""
---------------ROUTER CODE: NEEDS WORK--------------
router = SimpleRouter()
router.register('users', UserViewSet, base_name = 'users')
router.register('', BookViewSet, base_name='books')

urlpatterns = router.urls
"""
