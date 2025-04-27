# project-level urls.py (Unit_TestCase_Generator/urls.py)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('App_UTG.urls')),  # All API routes will be under /api/
    path('', include('App_UTG.urls')),  # Add this line to handle the root path
]
