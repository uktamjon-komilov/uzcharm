from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from blogs.views import index_page

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('user/', include('users.urls')),
)

urlpatterns.append(path("", index_page))
# urls for apps
urlpatterns += [
    path('rosetta/', include('rosetta.urls')),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
# 500, 404 page
handler500 = 'blogs.views.error_500'
handler404 = 'blogs.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


