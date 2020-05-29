from django.shortcuts import render

from index.models import Course


def get_courses(request):
    sql = "select " \
          "course.id as id, " \
          "course.shortname as name, " \
          "user.firstname as teacher_name, " \
          "(select count(*) from mdl_user as user, mdl_role_assignments as role_assignments, mdl_context as context where role_assignments.userid = user.id and role_assignments.roleid = 5 and role_assignments.contextid = context.id and context.instanceid = course.id) as count_user, " \
          "(select avg(grade_grades.rawgrade) from mdl_grade_grades as grade_grades, mdl_grade_items as grade_items where grade_grades.itemid = grade_items.id and grade_grades.rawgrade IS NOT NULL and grade_items.courseid = course.id) as avg, " \
          "(select max(time) from mdl_log as log where log.course = course.id) as last_time, " \
          "(select count(*) from mdl_log as log where log.course = course.id and log.action) as count_entry, " \
          "(select count(*) from mdl_logstore_standard_log as log where log.courseid = course.id and log.action = 'viewed') as count_viewed, " \
          "(select count(*) from mdl_course_modules as course_modules where course_modules.course = course.id) as count_modules " \
          "from mdl_user as user, mdl_role_assignments as role_assignments, mdl_context as context, mdl_course as course where role_assignments.userid = user.id and role_assignments.roleid = 3 and role_assignments.contextid = context.id and context.instanceid = course.id"
    courses = Course.objects.raw(sql)
    return render(request, 'index.html', locals())


def get_one_course(request, course_id):
    sql = "select " \
          "course.id as id, " \
          "course.shortname as name, " \
          "user.firstname as teacher_name, " \
          "(select count(*) from mdl_user as user, mdl_role_assignments as role_assignments, mdl_context as context where role_assignments.userid = user.id and role_assignments.roleid = 5 and role_assignments.contextid = context.id and context.instanceid = course.id) as count_user, " \
          "(select avg(grade_grades.rawgrade) from mdl_grade_grades as grade_grades, mdl_grade_items as grade_items where grade_grades.itemid = grade_items.id and grade_grades.rawgrade IS NOT NULL and grade_items.courseid = course.id) as avg, " \
          "(select max(time) from mdl_log as log where log.course = course.id) as last_time, " \
          "(select count(*) from mdl_log as log where log.course = course.id and log.action) as count_entry, " \
          "(select count(*) from mdl_logstore_standard_log as log where log.courseid = course.id and log.action = 'viewed') as count_viewed, " \
          "(select count(*) from mdl_course_modules as course_modules where course_modules.course = course.id) as count_modules " \
          "from mdl_user as user, mdl_role_assignments as role_assignments, mdl_context as context, mdl_course as course " \
          "where role_assignments.userid = user.id and role_assignments.roleid = 3 and role_assignments.contextid = context.id and context.instanceid = course.id " \
          "and course.id = " + str(course_id)
    course = Course.objects.raw(sql)[0]
    return render(request, 'course_info.html', locals())
