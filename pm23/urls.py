"""
URL configuration for pm23 project.

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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('contact', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('register/', include('register.urls')),
    path('venue/', include('venue.urls')),
    path('gift/', include('gift.urls')),
    path('backend/', include('backend.urls')),
]
