from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('user.urls')),
    # path('sign_in', include('user.urls')),
    # path('img_game', include('imggame.urls')),
    # path('dictionary', include('dictionary.urls')),
    # path('word_game', include('word_game.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()