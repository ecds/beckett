"""beckett URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from beckett.apps.works import views

urlpatterns = [
    url(r'^directing/Detail/(?P<pk>[^/]+)/$', views.DirectingDetail.as_view(template_name='works/directing_detail.html'), name="directingdetail"),
     url(r'^production/Detail/(?P<pk>[^/]+)/$', views.ProductionDetail.as_view(template_name='works/production_detail.html'), name="productiondetail"),
      url(r'^publication/Detail/(?P<pk>[^/]+)/$', views.PublicationDetail.as_view(template_name='works/publication_detail.html'), name="publicationdetail"),
       url(r'^reading/Detail/(?P<pk>[^/]+)/$', views.ReadingDetail.as_view(template_name='works/reading_detail.html'), name="readingdetail"),
        url(r'^translating/Detail/(?P<pk>[^/]+)/$', views.TranslatingDetail.as_view(template_name='works/translating_detail.html'), name="translatingdetail"),
         url(r'^writing/Detail/(?P<pk>[^/]+)/$', views.WritingDetail.as_view(template_name='works/writing_detail.html'), name="writingdetail")
]
