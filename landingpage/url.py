from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.landing_view, name='landing_view'),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^about/', views.about, name='about'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)