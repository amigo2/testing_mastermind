from django.contrib import admin
from django.urls import path, include

from api.coronavstech.companies.views import Company
#ßfrom companies.views import send_company_email


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include(companies_router.urls)),
    # path("send-email", send_company_email),
]