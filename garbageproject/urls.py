"""
URL configuration for garbageproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from garbageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('userregister',views.userregister,name="userregister"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('logout',views.logout,name="logout"),
    path('userpage',views.userpage,name="userpage"),
    path('usercomp',views.usercomp,name="usercomp"),
    path('mycomplaint',views.mycomplaint,name="mycomplaint"),
    path('admin2',views.admin2,name="admin2"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('createbin',views.createbin,name="createbin"),
    path('createdriver',views.createdriver,name="createdriver"),
    path('driverlogin',views.driverlogin,name="driverlogin"),
    path('driver2',views.driver2,name="driver2"),
    path('viewcomplaint',views.viewcomplaint,name="viewcomplaint"),
    path('viewcomplaint2/<int:id>',views.viewcomplaint2,name="viewcomplaint2"),
    path('userdetails',views.userdetails,name="userdetails"),
    path('updatebin',views.updatebin,name="updatebin"),
    path('updatebin1/<int:id>',views.updatebin1,name="updatebin1"),
    path('deletebin/<int:id>',views.deletebin,name="deletebin"),
    path('updatedriver',views.updatedriver,name="updatedriver"),
    path('updatedriver1/<int:id>',views.updatedriver1,name="updatedriver1"),
    path('deletedriver/<int:id>',views.deletedriver,name="deletedriver"),
    path('driverwork',views.driverwork,name='driverwork'),
    path('workreport',views.workreport,name='workreport'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('driverlogout',views.driverlogout,name='driverlogout'),
    path('send-notification/', views.admin_send_notification, name='admin_send_notification'),
    path('notifications/read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('delete_notification_Admin/<int:notification_id>/', views.delete_notification_Admin, name='delete_notification_Admin'),
     path('payment',views.payment,name='payment'),
                path('paycon',views.paycon,name='paycon'),
]
