from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import django_u2f.urls
import views
admin.autodiscover()

urlpatterns = [
    url(r'', include('registration.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^backend/events/', include('events.urls')),
    url(r'^backend/volunteer/', include('volunteer.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^u2f/', include(django_u2f.urls, namespace='u2f')),
	url(r'^api/pull/$', views.pull, name='pull'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
