from django.http import HttpResponse
from django.shortcuts import render

from groups.models import Group
from index.models import GradeItems, Course
from index.xml_creator import create_xls_group
from users.models import User


def get_groups(request):
    sql = "select cohort.id as id, " \
          "       cohort.name as name, " \
          "(select count(*) " \
          "        from mdl_user as user, " \
          "             mdl_cohort_members as cohort_members " \
          "        where cohort_members.userid = user.id " \
          "          and cohort_members.cohortid = cohort.id) as count_users " \
          "from mdl_cohort as cohort"
    groups = Group.objects.raw(sql)
    return render(request, 'final_grade.html', locals())


def get_one_group(request, group_id):
    sql = "select cohort.id as id, " \
          "       cohort.name as name " \
          "from mdl_cohort as cohort " \
          "where cohort.id = " + str(group_id)
    group = Group.objects.raw(sql)[0]

    sql = "select user.id as id, " \
          "       user.firstname as name " \
          "from mdl_user as user, " \
          "     mdl_cohort_members as cohort_members " \
          "where cohort_members.userid = user.id " \
          "  and cohort_members.cohortid = " + str(group_id)
    users = User.objects.raw(sql)

    max_len = 0
    for user in users:
        user.courses = []
        sql = 'select course.id as id,' \
              '       course.shortname as name,' \
              '       grade_grades.finalgrade as final_grade ' \
              'from mdl_user as user, ' \
              '     mdl_course as course, ' \
              '     mdl_cohort_members as cohort_members, ' \
              '     mdl_grade_items as grade_items, ' \
              '     mdl_grade_grades as grade_grades ' \
              'where cohort_members.userid = user.id ' \
              '  and grade_items.courseid = course.id ' \
              '  and grade_grades.userid = user.id ' \
              '  and grade_items.courseid = course.id ' \
              '  and grade_grades.itemid = grade_items.id ' \
              '  and grade_items.itemtype = \'course\' ' \
              '  and cohort_members.cohortid =  ' + str(group_id) + \
              "  and user.id = " + str(user.id)
        courses = Course.objects.raw(sql)
        for course in courses:
            user.courses.append(course)
        if len(user.courses) > 0:
            header = user
            max_len = len(user.courses)

    for user in users:
        if len(user.courses) == 0:
            for i in range(max_len):
                user.courses.append(Course(final_grade=None))

    return render(request, 'group_final_grade.html', locals())


def download_one_group(request, group_id):
    sql = "select cohort.id as id, " \
          "       cohort.name as name " \
          "from mdl_cohort as cohort " \
          "where cohort.id = " + str(group_id)
    group = Group.objects.raw(sql)[0]

    sql = "select user.id as id, " \
          "       user.firstname as name " \
          "from mdl_user as user, " \
          "     mdl_cohort_members as cohort_members " \
          "where cohort_members.userid = user.id " \
          "  and cohort_members.cohortid = " + str(group_id)
    users = User.objects.raw(sql)

    max_len = 0
    for user in users:
        user.courses = []
        sql = 'select course.id as id,' \
              '       course.shortname as name,' \
              '       grade_grades.finalgrade as final_grade ' \
              'from mdl_user as user, ' \
              '     mdl_course as course, ' \
              '     mdl_cohort_members as cohort_members, ' \
              '     mdl_grade_items as grade_items, ' \
              '     mdl_grade_grades as grade_grades ' \
              'where cohort_members.userid = user.id ' \
              '  and grade_items.courseid = course.id ' \
              '  and grade_grades.userid = user.id ' \
              '  and grade_items.courseid = course.id ' \
              '  and grade_grades.itemid = grade_items.id ' \
              '  and grade_items.itemtype = \'course\' ' \
              '  and cohort_members.cohortid =  ' + str(group_id) + \
              "  and user.id = " + str(user.id)
        courses = Course.objects.raw(sql)
        for course in courses:
            user.courses.append(course)
        if len(user.courses) > 0:
            header = user
            max_len = len(user.courses)

    for user in users:
        if len(user.courses) == 0:
            for i in range(max_len):
                user.courses.append(Course(final_grade=None))

    path = create_xls_group(group.name, header, users)

    file = open(path, 'rb')
    response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=group.xlsx'
    return response
