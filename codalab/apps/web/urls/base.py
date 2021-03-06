from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .. import views

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='web/index.html'), name='home'),
                       url(r'^my/', include('apps.web.urls.my')),
                       url(r'^competitions/', include('apps.web.urls.competitions')),                       
                       url(r'^experiments/', include('apps.web.urls.experiments')),
                       url(r'^help/', include('apps.web.urls.help'))
                       )
