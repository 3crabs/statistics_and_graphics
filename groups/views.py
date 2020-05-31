from django.shortcuts import render

from groups.models import Group
from users.models import User


def get_groups(request):
    sql = "select mdl_groups.id as id, " \
          "       mdl_groups.name as name, " \
          "(select count(*) " \
          "        from mdl_user as user, " \
          "             mdl_groups_members as groups_members " \
          "        where groups_members.userid = user.id " \
          "          and groups_members.groupid = mdl_groups.id) as count_users " \
          "from mdl_groups"
    groups = Group.objects.raw(sql)
    return render(request, 'final_grade.html', locals())


def get_one_group(request, group_id):
    sql = "select mdl_groups.id as id, " \
          "       mdl_groups.name as name " \
          "from mdl_groups " \
          "where mdl_groups.id = " + str(group_id)
    group = Group.objects.raw(sql)[0]

    sql = "select user.id as id, " \
          "       user.firstname as name " \
          "from mdl_user as user, " \
          "     mdl_groups_members as groups_members " \
          "where groups_members.userid = user.id " \
          "  and groups_members.groupid = " + str(group_id)
    users = User.objects.raw(sql)
    return render(request, 'group_final_grade.html', locals())
