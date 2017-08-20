from django.http import HttpResponse
from django.http import HttpResponseRedirect

from website.constants import RESUME_LINKS


def newrelic(request):
    return HttpResponse('ok')


def resume_dl(request):
    return HttpResponseRedirect(RESUME_LINKS['resume_dl_link'])


def resume_gh(request):
    return HttpResponseRedirect(RESUME_LINKS['resume_gh_link'])
