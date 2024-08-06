from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('home/',views.home,name = 'home'),
    path('techblog',views.techblog,name = 'techblog'),
    path('hackathon',views.hackathon,name = 'hackathon'),

    path('techblog/githubblog/',views.githubblog,name = 'githubblog'),
    path('emailotp',views.emailotp,name = 'emailotp'),
    path('verifyotp',views.verifyotp,name = 'verifyotp'),
    path('finalregister',views.finalregister,name = 'finalregister'),

    
    path('book',views.book,name = 'book'),
    path('msg',views.msg,name = 'msg'),
    path('loginerror',views.loginerror,name = 'loginerror'),
    path('logout',views.logout,name = 'logout'),
    path("profile_page", views.profile_page, name="profile_page"),
    path("profile_page/edit_your_profile", views.edit_your_profile, name="edit_your_profile"),
    
    
    path('daily_leetcode_questions',views.daily_leetcode_questions,name = 'daily_leetcode_questions'),
    path('soon',views.soon,name = 'soon'),
    path('news',views.news,name = 'news'),
    path('writetechblog',views.writetechblog,name = 'writetechblog'),
]