"""
URL configuration for x_trade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', include('rest_framework.urls')),
    path('api/schema', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(), name="swagger"),
    path('factory/', include('trade_net.urls.factory')),
    path('retail_network/', include('trade_net.urls.retail_network')),
    path('sole_trader/', include('trade_net.urls.sole_trader')),
]
