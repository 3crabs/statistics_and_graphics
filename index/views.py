from django.shortcuts import render

from index.models import Course, User


def get_courses(request):
    sql = "select course.id  as id, " \
          "       course.shortname as name, " \
          "       user.firstname   as teacher_name, " \
          "" \
          "(select count(*)" \
          "    from mdl_user as user," \
          "         mdl_role_assignments as role_assignments, " \
          "         mdl_context as context " \
          "    where role_assignments.userid = user.id " \
          "      and role_assignments.roleid = 5 " \
          "      and role_assignments.contextid = context.id " \
          "      and context.instanceid = course.id)    as count_user " \
          "" \
          "from mdl_user as user, " \
          "     mdl_role_assignments as role_assignments, " \
          "     mdl_context as context, " \
          "     mdl_course as course " \
          "where role_assignments.userid = user.id " \
          "  and role_assignments.roleid = 3 " \
          "  and role_assignments.contextid = context.id " \
          "  and context.instanceid = course.id"
    courses = Course.objects.raw(sql)
    return render(request, 'index.html', locals())


def get_one_course(request, course_id):
    sql = "select course.id  as id, " \
          "       course.shortname as name, " \
          "       user.firstname   as teacher_name, " \
          "" \
          "(select count(*)" \
          "    from mdl_user as user," \
          "         mdl_role_assignments as role_assignments, " \
          "         mdl_context as context " \
          "    where role_assignments.userid = user.id " \
          "      and role_assignments.roleid = 5 " \
          "      and role_assignments.contextid = context.id " \
          "      and context.instanceid = course.id)    as count_user " \
          "" \
          "from mdl_user as user, " \
          "     mdl_role_assignments as role_assignments, " \
          "     mdl_context as context, " \
          "     mdl_course as course " \
          "where role_assignments.userid = user.id " \
          "  and role_assignments.roleid = 3 " \
          "  and role_assignments.contextid = context.id " \
          "  and context.instanceid = course.id " \
          "  and course.id = " + course_id
    course = User.objects.raw(sql)[0]
    sql = "select user.id        as id, " \
          "       user.firstname as name " \
          "from mdl_user as user, " \
          "     mdl_role_assignments as role_assignments, " \
          "     mdl_context as context, " \
          "     mdl_course as course " \
          "where role_assignments.userid = user.id " \
          "  and role_assignments.roleid = 5 " \
          "  and role_assignments.contextid = context.id " \
          "  and context.instanceid = course.id " \
          "  and course.id = " + course_id
    users = User.objects.raw(sql)
    return render(request, 'course_info.html', locals())


def get_course_one_user(request, course_id, user_id):
    return None