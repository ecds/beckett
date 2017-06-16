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
from beckett.apps.people import views
from beckett.apps.people.views import arikha, boyle, bray, devine, harvey, hutchinson, lieberson, megged, myron, rosset, schneider

urlpatterns = [
    url(r'^$', views.PeopleList.as_view(template_name='people/person_list.html'), name="people"),
    url(r'^Detail/(?P<pk>[^/]+)/$', views.PersonDetail.as_view(template_name='people/person_detail.html'), name="detailperson"),
    url(r'^organizations/Detail/(?P<pk>[^/]+)/$', views.OrganizationDetail.as_view(template_name='people/organization_detail.html'), name="detailorganization"),
    url(r'^arikha$', arikha, name="arikha"),
    url(r'^boyle$', boyle, name="boyle"),
    url(r'^bray$', bray, name="bray"),
    url(r'^devine$', devine, name="devine"),
    url(r'^harvey$', harvey, name="harvey"),
    url(r'^hutchinson$', hutchinson, name="hutchinson"),
    url(r'^lieberson$', lieberson, name="lieberson"),
    url(r'^megged$', megged, name="megged"),
    url(r'^myron$', myron, name="myron"),
    url(r'^rosset$', rosset, name="rosset"),
    url(r'^schneider$', schneider, name="schneider"),
]
