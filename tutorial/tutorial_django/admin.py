from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag, User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

from django.contrib.auth.models import Permission


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonTagInline(admin.StackedInline): # TabularInline
    model = Lesson.tags.through

class LessonAmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css', )
        }
    form = LessonForm
    list_display = ["id", "subject", "created_date", "active", "course"]
    search_fields = ["subject", "created_date", "course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]
    inlines = (LessonTagInline, )

    def avatar(self, lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='300' />".format(img_url=lesson.image.name, alt=lesson.subject))


class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course'

class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline, )

class TagAdmin(admin.ModelAdmin):
    inlines = (LessonTagInline, )




class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY KHOA HOC'

    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()

    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count=Count('lessons_query')).values("id", "subject", "lesson_count")

        return TemplateResponse(request, 'admin/course-stats.html', {
            'course_count': course_count,
            'stats': stats
        })

# admin_site = CourseAppAdminSite('mycourse')

# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User)
admin.site.register(Permission)

# admin_site.register(Category)
# admin_site.register(Course, CourseAdmin)
# admin_site.register(Lesson, LessonAmin)
# admin_site.register(Tag, TagAdmin)