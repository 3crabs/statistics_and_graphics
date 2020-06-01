from django.shortcuts import render

from groups.models import Group
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
    return render(request, 'group_final_grade.html', locals())
