from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # templates
    path("anything-but-admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
    # api
    path("api/v1", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/rest-auth/", include("rest_auth.urls")),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
