from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^ping/", TemplateView.as_view(template_name="ping.json"), name="ping"),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^waitlist_entries/', include('waitlist_entries.urls', namespace="waitlist_entries")),
    url(r'^vulnerabilities/', include('vulnerabilities.urls', namespace="vulnerabilities")),
    url(r'^users/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
