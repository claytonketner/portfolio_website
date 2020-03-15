from django.db.models import F
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from website.constants import RESUME_LINKS
from website.models import ViewCounter


def count_view(func):
    """
    Wrapper for counting a view via the ViewCounter model. Note the portfolio app's models have
    their own view counter field. This is mostly just for counting clicks on the resume buttons.
    """
    def wrapper(request, *args, **kwargs):
        vc, _ = ViewCounter.objects.get_or_create(url=request.path)
        vc.views = F('views') + 1
        vc.save()
        return func(request, *args, **kwargs)
    return wrapper


def newrelic(request):
    return HttpResponse('ok')


@count_view
def resume_dl(request):
    return HttpResponseRedirect(RESUME_LINKS['resume_dl_link'])


@count_view
def resume_gh(request):
    return HttpResponseRedirect(RESUME_LINKS['resume_gh_link'])
