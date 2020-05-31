from django.shortcuts import render

from groups.models import Group


def get_groups(request):
    sql = "select mdl_groups.id as id, " \
          "       mdl_groups.name as name " \
          "from mdl_groups"
    groups = Group.objects.raw(sql)
    return render(request, 'final_grade.html', locals())
