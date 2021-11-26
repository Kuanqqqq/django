from django.shortcuts import redirect, render
from build.models import Build
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def add_component(request, name, pk):
    print('in add component')
    print(name)
    user_token = request.session['user_token']
    object = ContentType.objects.get(model=name).get_object_for_this_type(pk=pk)
    print(object)
    build = Build.objects.get(user_token=user_token)
    print(build)
    setattr(build, name, object)
    build.save()
    return redirect('/list/')

def delete_component(request, name):
    user_token = request.session['user_token']
    build = Build.objects.get(user_token=user_token)
    setattr(build, name, None)
    build.save()
    return redirect('/list/')