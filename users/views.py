from django.shortcuts import render

from index.models import User, Course


def get_users(request):
    sql = "select user.id        as id, " \
          "       user.firstname as name " \
          "from mdl_user as user"
    users = User.objects.raw(sql)
    return render(request, 'users.html', locals())


def get_one_user(request, user_id):
    sql = "select user.id        as id, " \
          "       user.firstname as name " \
          "from mdl_user as user " \
          "where user.id = " + user_id
    user = User.objects.raw(sql)[0]
    sql = "select course.id        as id, " \
          "       course.shortname as name " \
          "from mdl_user as user, " \
          "     mdl_role_assignments as role_assignments, " \
          "     mdl_context as context, " \
          "     mdl_course as course " \
          "where context.instanceid = course.id " \
          "  and role_assignments.contextid = context.id " \
          "  and role_assignments.userid = user.id " \
          "  and user.id = " + user_id
    courses = Course.objects.raw(sql)
    return render(request, 'user_info.html', locals())
