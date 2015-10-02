from __future__ import unicode_literals
from django.conf.urls import url

#from . import settings as app_settings
from . import views

urlpatterns = [
    url(
        r"^$",
        views.create_invoice,
        name="create_invoice"
    ),
    url(
        r"^subscribe/$",
        views.list_invoices,
        name="list_invoices"
    ),
]