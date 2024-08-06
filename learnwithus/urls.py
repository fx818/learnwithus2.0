from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("admin_at_learnwithus_secured_via_high_security/", admin.site.urls),
    path('',include('component.urls')),
    path('learnwithusai/',include('app_learnwithusai.urls')),
    path('',include('app_opportunities.urls')),
    path('',include('app_courses.urls')),
    path('',include('app_infoPage.urls')),
    path('',include('app_notespedia.urls')),
    path('',include('app_programmingHub.urls')),
    path("accounts/",include("allauth.urls")),
]





urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)