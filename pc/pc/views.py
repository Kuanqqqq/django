from django.shortcuts import render
from CPU.models import CPU
import string
import secrets

from build.models import Build
alphabet = string.ascii_letters + string.digits


def home_page(request):
    if not request.session.has_key('user_token'):
        user_token = ''.join(secrets.choice(alphabet) for i in range(10))
        request.session['user_token'] = user_token
        new_build = Build()
        new_build.user_token = user_token
        new_build.save()
    # else:
    #     print(request.session['user_token'])
    # print(request.session.get_session_cookie_age())
    return render(request, 'home_page.html')


def list_page(request):
    user_token = request.session['user_token']
    build = Build.objects.get(user_token=user_token)
    return render(request, 'list.html', {'build': build})
    