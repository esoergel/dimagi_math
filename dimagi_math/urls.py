from django.conf.urls import patterns, include, url
from django.contrib import admin

from math_engine.views import MathView, HxView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MathView.as_view()),
    url(r'^history$', HxView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
