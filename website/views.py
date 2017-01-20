from django.http import HttpResponse


def newrelic(request):
    return HttpResponse('ok')
