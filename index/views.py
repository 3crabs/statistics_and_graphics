from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

from index.models import Course, GradeItems
from users.models import User


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
          "      and context.instanceid = course.id)    as count_user, " \
          "" \
          "(select max(user_lastaccess.timeaccess) " \
          "from mdl_user_lastaccess as user_lastaccess " \
          "where user_lastaccess.courseid = course.id) last_access, " \
          "" \
          "(select avg(grade_grades.finalgrade) " \
          "from mdl_grade_grades as grade_grades, " \
          "     mdl_grade_items as grade_items " \
          "where grade_grades.itemid = grade_items.id " \
          "  and grade_items.itemtype = 'course' " \
          "and grade_items.courseid = course.id) as avg_final_grade,  " \
          "" \
          "(select count(*) " \
          "from mdl_logstore_standard_log as log " \
          "where log.action = 'viewed' " \
          "  and log.target = 'course' " \
          "  and log.courseid = course.id) as count_views " \
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
          "       user.firstname as name, " \
          "(select max(timeaccess) " \
          "        from mdl_user_lastaccess as user_lastaccess " \
          "        where user_lastaccess.courseid = course.id) as last_access, " \
          "" \
          "(select grade_grades.finalgrade as grade " \
          "from mdl_course as course, " \
          "     mdl_user as user_1, " \
          "     mdl_grade_items as grade_items, " \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id " \
          "  and grade_grades.itemid = grade_items.id " \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'course' " \
          "  and course.id = " + str(course_id) + \
          "  and user_1.id = user.id) as end_grade, " \
          "" \
          "(select grade_grades.id " \
          "from mdl_course as course, " \
          "     mdl_user as user_1, " \
          "     mdl_grade_items as grade_items, " \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id " \
          "  and grade_grades.itemid = grade_items.id " \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'course' " \
          "  and course.id = " + str(course_id) + \
          "  and user_1.id = user.id) as end_grade_id " \
          "" \
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
          "  and course.id = " + course_id + \
          "  and user.id = " + user_id
    user = User.objects.raw(sql)[0]

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

    sql = "select grade_items.id as id, " \
          "       grade_items.itemname name, " \
          "       grade_items.grademin grade_min, " \
          "       grade_items.grademax grade_max, " \
          "       grade_items.itemmodule as type, " \
          "       grade_grades.finalgrade as grade, " \
          "       grade_grades.id as grade_id, " \
          "" \
          "(select user_1.firstname " \
          "        from mdl_user as user_1 " \
          "        where grade_grades.usermodified = user_1.id) as user_modified " \
          "" \
          "from mdl_course as course, " \
          "     mdl_user as user, " \
          "     mdl_grade_items as grade_items," \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id" \
          "  and grade_grades.itemid = grade_items.id" \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'mod'" \
          "  and course.id = " + str(course_id) + \
          "  and user.id = " + str(user_id)
    items = GradeItems.objects.raw(sql)

    sql = "select grade_items.id as id, " \
          "       grade_items.itemname name, " \
          "       grade_items.grademin grade_min, " \
          "       grade_items.grademax grade_max, " \
          "       grade_items.itemmodule as type, " \
          "       grade_grades.finalgrade as grade " \
          "from mdl_course as course, " \
          "     mdl_user as user, " \
          "     mdl_grade_items as grade_items," \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id" \
          "  and grade_grades.itemid = grade_items.id" \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'course'" \
          "  and course.id = " + str(course_id) + \
          "  and user.id = " + str(user_id)
    end_grade = GradeItems.objects.raw(sql)
    if end_grade:
        end_grade = end_grade[0]

    return render(request, 'student_info.html', locals())


def save_one_course(request, course_id):
    sql = "select user.id        as id, " \
          "       user.firstname as name, " \
          "(select max(timeaccess) " \
          "        from mdl_user_lastaccess as user_lastaccess " \
          "        where user_lastaccess.courseid = course.id) as last_access, " \
          "" \
          "(select grade_grades.finalgrade as grade " \
          "from mdl_course as course, " \
          "     mdl_user as user_1, " \
          "     mdl_grade_items as grade_items, " \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id " \
          "  and grade_grades.itemid = grade_items.id " \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'course' " \
          "  and course.id = " + str(course_id) + \
          "  and user_1.id = user.id) as end_grade, " \
          "" \
          "(select grade_grades.id " \
          "from mdl_course as course, " \
          "     mdl_user as user_1, " \
          "     mdl_grade_items as grade_items, " \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id " \
          "  and grade_grades.itemid = grade_items.id " \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'course' " \
          "  and course.id = " + str(course_id) + \
          "  and user_1.id = user.id) as end_grade_id " \
          "" \
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
    for user in users:
        key = str(user.end_grade_id)
        if key != 'None':
            old_value = user.end_grade
            new_value = request.POST[key]
            if str(new_value) != str(old_value):
                cursor = connection.cursor()
                sql = "update mdl_grade_grades set finalgrade = " + str(new_value) + " where id = " + str(key)
                cursor.execute(sql)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def save_course_one_user(request, course_id, user_id):
    sql = "select grade_items.id as id, " \
          "       grade_items.itemname name, " \
          "       grade_items.grademin grade_min, " \
          "       grade_items.grademax grade_max, " \
          "       grade_items.itemmodule as type, " \
          "       grade_grades.finalgrade as grade," \
          "       grade_grades.id as grade_id " \
          "from mdl_course as course, " \
          "     mdl_user as user, " \
          "     mdl_grade_items as grade_items," \
          "     mdl_grade_grades as grade_grades " \
          "where grade_items.courseid = course.id" \
          "  and grade_grades.itemid = grade_items.id" \
          "  and grade_grades.userid = user.id " \
          "  and grade_items.itemtype = 'mod'" \
          "  and course.id = " + str(course_id) + \
          "  and user.id = " + str(user_id)
    items = GradeItems.objects.raw(sql)

    for item in items:
        key = str(item.grade_id)
        if key != 'None':
            old_value = item.grade
            new_value = request.POST[key]
            if str(new_value) != str(old_value):
                cursor = connection.cursor()
                sql = "update mdl_grade_grades set finalgrade = " + str(new_value) + " where id = " + str(key)
                cursor.execute(sql)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
