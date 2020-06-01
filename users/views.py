from django.shortcuts import render

from index.models import Course
from users.models import User


def get_users(request):
    name = request.GET.get("name", "")
    sql = "select user.id        as id, " \
          "       CONCAT(user.lastname, ' ', user.firstname) as name, " \
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
          "(select count(*) " \
          "from mdl_logstore_standard_log as log " \
          "where log.action = 'viewed' " \
          "  and log.target like '%%course%%' " \
          "  and log.userid = user.id) as count_views, " \
          "" \
          "(select count(*) " \
          "from mdl_logstore_standard_log as log " \
          "where log.action = 'viewed' " \
          "  and log.target like 'course' " \
          "  and log.userid = user.id) as count_in, " \
          "" \
          "(select max(timeaccess) " \
          "from mdl_user_lastaccess as user_lastaccess " \
          "where user_lastaccess.userid = user.id) as last_access " \
          "from mdl_user as user " \
          "where 1"
    if name:
        sql += " and CONCAT(user.lastname, ' ', user.firstname) LIKE '%%" + name + "%%'"
    users = User.objects.raw(sql)
    return render(request, 'users.html', locals())


def get_one_user(request, user_id):
    sql = "select user.id        as id, " \
          "       CONCAT(user.lastname, ' ', user.firstname) as name " \
          "from mdl_user as user " \
          "where user.id = " + user_id
    user = User.objects.raw(sql)[0]
    sql = "select course.id        as id, " \
          "       course.shortname as name," \
          "       role.shortname as role, " \
          "" \
          "(select user_lastaccess.timeaccess " \
          "from mdl_user_lastaccess as user_lastaccess " \
          "where user_lastaccess.courseid = course.id " \
          "  and user_lastaccess.userid = user.id) as last_access, " \
          "" \
          "(select grade_grades.finalgrade " \
          "from mdl_grade_grades as grade_grades, " \
          "     mdl_grade_items as grade_items " \
          "where grade_grades.itemid = grade_items.id " \
          "  and grade_items.itemtype = 'course' " \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.courseid = course.id) as final_grade, " \
          "" \
          "(select count(*) " \
          "from mdl_logstore_standard_log as log " \
          "where log.action = 'viewed' " \
          "  and log.target like '%%course%%' " \
          "  and log.userid = user.id " \
          "  and log.courseid = course.id) as count_views, " \
          "" \
          "(select count(*) " \
          "from mdl_logstore_standard_log as log " \
          "where log.action = 'viewed' " \
          "  and log.target like 'course' " \
          "  and log.userid = user.id " \
          "  and log.courseid = course.id) as count_in " \
          "" \
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
