from django.contrib import admin
from django.urls import path, include


# Main URL configuration for Library Inventory
urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', include('pages.urls')),

    # Library Inventory
    path('inventory/', include('inventory.urls')),
]
