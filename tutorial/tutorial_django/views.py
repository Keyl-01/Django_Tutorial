from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    # list (GET) --> xem danh sach khoa hoc
    # ... (POST) --> them khoa hoc
    # detail --> xem chi tiet 1 khoa hoc
    # ... (PUT) --> cap nhap
    # ... (DELETE) --> xoa khoa hoc





def index(request):
    return render(request, template_name='index.html', context={
        'name':'Keyl'
    })

def welcome(request, year):
    return HttpResponse("Hello " + str(year))

def welcome2(request, year):
    return HttpResponse("Hello2 " + str(year))

class TestView(View):
    def get(self, request):
        return HttpResponse("Get Testing")
    def post(self, request):
        pass