from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include("customers.urls", namespace="customers")),
    path('jobs/', include("jobs.urls", namespace="jobs")),
    path('invoices/', include("invoices.urls", namespace="invoices")),
    path('expenses/', include("expenses.urls", namespace="expenses")),
    path('quotations/', include("quotations.urls", namespace="quotations")),
    path('', include("authentication.urls", namespace="authentication")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
