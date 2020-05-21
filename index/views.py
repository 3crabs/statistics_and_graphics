from django.shortcuts import render


def get_courses(request):
    return render(request, 'index.html', locals())


def get_one_course(request, course_id):
    return render(request, 'course_info.html', locals())
