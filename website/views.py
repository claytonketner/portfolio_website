from django.db.models import F
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.defaults import page_not_found

from website.constants import RESUME_LINKS
from website.models import ViewCounter


def increment_view_counter_for_url(url_path):
    vc, _ = ViewCounter.objects.get_or_create(url=url_path)
    vc.views = F('views') + 1
    vc.save()


def count_view(func):
    """
    Wrapper for counting a view via the ViewCounter model. Note the portfolio app's models have
    their own view counter field. This is mostly just for counting clicks on the resume buttons.
    """
    def wrapper(request, *args, **kwargs):
        increment_view_counter_for_url(request.path)
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


def record_404_view(request, exception):
    # Keep track of how many random URLs bots try to look at, because that's pretty fun
    increment_view_counter_for_url('404')
    page_not_found(request, exception, template_name="errors/404.html")
