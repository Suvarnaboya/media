from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.feed,name="home"),
    path('login',views.loginView,name="login"),
    path('register',views.register,name='register'),
    path('post',views.postView,name='post'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutView,name='logout'),
    path('display/<int:rid>',views.single,name="onePost"),
    path('delete/<int:rid>',views.deleteView,name="delete"),
    path('manufacture',views.manu,name="manufacture"),
    path('create',views.createCar,name="create_car"),
    path('cars',views.showCars,name="cars"),
    path('updateTweet/<int:rid>',views.updateView,name="updateTweet"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)