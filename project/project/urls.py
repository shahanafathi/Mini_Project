"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Login',views.Login,name='Login'),
   
    
    
    path('register',views.register,name='register'),
    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('profileedit/<int:id>',views.profileedit,name='profileedit'),
    path('userhome1',views.userhome1,name='userhome1'),
    path('viewhistory',views.viewhistory,name='viewhistory'),
    path('deposite',views.deposite,name='deposite'),
    path('withdraw',views.withdraw,name='withdraw'),
    
    
    #### bank......
    path('bankhome',views.bankhome,name='bankhome'),
    path('profileview',views.profileview,name='profileview'),
    path('viewuser', views.viewuser, name='viewuser'),
    path('bankuserprofile/<int:id>',views.bankuserprofile,name='bankuserprofile'),
    path('userhistory/<int:id>', views.userhistory, name='userhistory'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('all', views.all, name='all'),
    
    #### admin......
    # path('admregstr',views.admregstr,name='admregstr'),
    path('admregstr', views.admregstr, name='admregstr'),
 
 ]


if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    