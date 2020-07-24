from django.urls import reverse
from django.db.models import F
from django.http import Http404
from django.shortcuts import render

from portfolio.models import PortfolioEntry
from website.views import increment_view_counter_for_url


def portfolio_entry(request, entry_slug):
    all_entries = PortfolioEntry.objects.order_by('-is_index', '-when_created')
    all_entries = all_entries.exclude(is_index=True)
    try:
        current_entry = PortfolioEntry.objects.get(slug=entry_slug)
    except PortfolioEntry.DoesNotExist:
        raise Http404("Entry does not exist")
    current_entry.views = F('views') + 1
    current_entry.save()
    # According to Django docs, when you use an F expression, you need to
    # reload the object to be able to read the value of that field (views)
    current_entry = PortfolioEntry.objects.get(slug=entry_slug)
    # Using this method isn't really necessary since PortfolioEntry already has a view counter.
    # Mostly just doing it for consistency
    increment_view_counter_for_url(request.path)
    # Allow for {variables} in entries. Doing it in the view rather than when
    # the entry is initally loaded into the DB allows for better separation of
    # variables, like a kind of namespace
    entry_vars = {
        'resume_dl_link': reverse('resume_dl'),
        'resume_gh_link': reverse('resume_gh'),
    }
    current_entry.body = current_entry.body.format(**entry_vars)
    context = {
        'all_entries': all_entries,
        'current_entry': current_entry,
    }
    return render(request, 'portfolio/entry.html', context)


def index(request):
    index_page = PortfolioEntry.objects.get(is_index=True)
    return portfolio_entry(request, index_page.slug)
