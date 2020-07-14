from django.shortcuts import render

import datetime
# Create your views here.


def index(request):
    data = datetime.datetime.now()
    ctx = {'data': data}
    return render(request, 'index.html', ctx)
