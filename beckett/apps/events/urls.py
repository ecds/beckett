from django.conf.urls import include, url
from django.contrib import admin
from beckett.apps.events import views
from beckett.apps.events.views import chronology, AttendanceDetail, Public_eventDetail

urlpatterns = [
    url(r'^chronology$', chronology, name="chronology"),
     url(r'^attendance/Detail/(?P<pk>[^/]+)/$', views.AttendanceDetail.as_view(template_name='events/attendance_detail.html'), name="attendancedetail"),
      url(r'^publicEvent/Detail/(?P<pk>[^/]+)/$', views.Public_eventDetail.as_view(template_name='events/public_event_detail.html'), name="public_event_detail"),
]