from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from drf_yasg.utils import swagger_auto_schema

from .models import Course, Lesson, Tag, User
from .serializers import CourseSerializer, LessonSerializer, UserSerializer



class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    # swagger_schema = None

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    # list (GET) --> xem danh sach khoa hoc
    # ... (POST) --> them khoa hoc
    # detail --> xem chi tiet 1 khoa hoc
    # ... (PUT) --> cap nhap
    # ... (DELETE) --> xoa khoa hoc

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer


    @swagger_auto_schema(
        operation_description='API này dùng để ẩn một bài viết từ phía client',
        responses={
            status.HTTP_200_OK: LessonSerializer()
        }
    )
    @action(methods=['post'], detail=True, url_path="hide-lesson")
    # /lessons/{pk}/hide_lesson
    def hide_lesson(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            lesson.active = False
            lesson.save()
        except Lesson.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=LessonSerializer(lesson, context={'request': request}).data, status=status.HTTP_200_OK)


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