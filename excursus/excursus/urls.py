from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from rooms.views import CategoryCreate,CategoryDelete, CategoryUpdate, signup
urlpatterns = [
    url(r'^rooms/', include('rooms.urls')),
    url(r'^$', RedirectView.as_view(url='/rooms/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', signup, name='signup'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

