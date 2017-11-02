from django.shortcuts import render
from django.views.generic import ListView, DetailView
from beckett.apps.events.models import Attendance, Public_event


def chronology(request):
  return render(request, 'chronology.html')

class AttendanceDetail(DetailView):
    model = Attendance
    queryset = Attendance.objects.all()
    template_name = 'attendance/attendance_detail.html'

class Public_eventDetail(DetailView):
    model = Public_event
    queryset = Public_event.objects.all()
    template_name = 'publicEvent/public_event_detail.html'