from django.urls import path


urlpatterns = [
    path('', home,name='home'),
    path('login', Login,name='login'),
    path('logout', Logout,name='logout'),
    path('signup', signup,name='signup'),
    path('about', about,name='about'),
    path('contact', contact,name='contact'),
]