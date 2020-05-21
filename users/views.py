from django.shortcuts import render


def get_users(request):
    return render(request, 'users.html', locals())


def get_one_user(request, user_id):
    return render(request, 'user_info.html', locals())
