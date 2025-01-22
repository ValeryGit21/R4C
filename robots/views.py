from django.shortcuts import render, HttpResponse

import json

from robots.forms import RobotForm


def robot_view(request):
    if request.method == 'GET':
        obj = json.loads(request.body)
        form = RobotForm(obj)
        if form.is_valid():
            form.save()

    return HttpResponse('Hello World')
