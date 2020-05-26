from django.shortcuts import render

from index.models import MdlCourse


def get_courses(request):
    courses = MdlCourse.objects.all()
    return render(request, 'index.html', locals())


def get_one_course(request, course_id):
    return render(request, 'course_info.html', locals())
