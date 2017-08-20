"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from portfolio import views
from website.views import newrelic as newrelic_view
from website.views import resume_dl
from website.views import resume_gh

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^newrelic/$', newrelic_view, name='newrelic'),
    url(r'^resume-dl/$', resume_dl, name='resume_dl'),
    url(r'^resume-gh/$', resume_gh, name='resume_gh'),
    url(r'^(?P<entry_slug>[\w\-]+)/$', views.portfolio_entry, name='entry'),
]
