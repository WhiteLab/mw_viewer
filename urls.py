import views
from django.conf import settings
from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = patterns('',
                        url(r'^viewer/mw_viewer', views.mw_viewer, name='home page'),
                       url(r'^viewer/individuals', views.individual_view, name='view individuals')
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
