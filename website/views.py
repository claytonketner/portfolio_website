from django.http import HttpResponse
from django.http import HttpResponseRedirect

from website.constants import RESUME_LINK


def newrelic(request):
    return HttpResponse('ok')


def resume(request):
    return HttpResponseRedirect(RESUME_LINK)
