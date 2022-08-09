from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
# from .admin import admin_site

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)

urlpatterns = [
    # path('', views.index, name="index"),
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('welcome/<int:year>', views.welcome, name="welcome"),
    re_path(r'^welcome2/(?P<year>[0-9]{4})/$', views.welcome2, name="welcome"),
    path('test/', views.TestView.as_view())
]
