from django.shortcuts import render

from index.models import Course
from users.models import User


def get_users(request):
    name = request.GET.get("name", "")
    sql = "select user.id        as id, " \
          "       user.firstname as name, " \
          "" \
          "(select count(*) " \
          "from mdl_user as user_1, " \
          "     mdl_course as cource, " \
          "     mdl_role_assignments as role_assignments, " \
          "     mdl_context as context " \
          "where role_assignments.userid = user_1.id " \
          "  and role_assignments.contextid = context.id " \
          "  and context.instanceid = cource.id " \
          "  and user_1.id = user.id) as count_course," \
          "" \
          "(select max(timeaccess) " \
          "from mdl_user_lastaccess as user_lastaccess " \
          "where user_lastaccess.userid = user.id) as last_access " \
          "from mdl_user as user " \
          "where 1"
    if name:
        sql += " and user.firstname LIKE '%%" + name + "%%'"
    users = User.objects.raw(sql)
    return render(request, 'users.html', locals())


def get_one_user(request, user_id):
    sql = "select user.id        as id, " \
          "       user.firstname as name " \
          "from mdl_user as user " \
          "where user.id = " + user_id
    user = User.objects.raw(sql)[0]
    sql = "select course.id        as id, " \
          "       course.shortname as name," \
          "       role.shortname as role " \
          "from mdl_user as user, " \
          "     mdl_role_assignments as role_assignments, " \
          "     mdl_context as context, " \
          "     mdl_course as course," \
          "     mdl_role as role " \
          "where context.instanceid = course.id " \
          "  and role_assignments.contextid = context.id " \
          "  and role_assignments.userid = user.id" \
          "  and role.id = role_assignments.roleid " \
          "  and user.id = " + user_id
    courses = Course.objects.raw(sql)
    return render(request, 'user_info.html', locals())
