from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from rooms.views import category
urlpatterns = [
    url(r'^rooms/', include('rooms.urls')),
    url(r'^$', RedirectView.as_view(url='/rooms/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^category/(?P<slug>[^/]+)/$', category)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
