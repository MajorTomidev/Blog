from django.urls import path
from .views import register, home, signup,signin, logout

urlpatterns = [
    path('register/', register, name='register' ),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('', home, name= 'home' )
]