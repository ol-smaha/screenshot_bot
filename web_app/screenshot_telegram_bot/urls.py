from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bot.bot import web_hook


urlpatterns = [
    path('admin/', admin.site.urls),
    path('web_hook/', web_hook),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
