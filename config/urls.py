from django.conf import settings
from django.contrib import admin
from django.urls import path

# from drf_spectacular import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Estate Management API",
#         default_version="v1",
#         description="An Estate Management API",
#         contact=openapi.Contact(email="yoyongdev@gmail.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Estate Management API"
admin.site.site_title = "Estate Management API Portal"
admin.site.index_title = "Welcome to Estate Management Admin Portal"
