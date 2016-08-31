from django.shortcuts import render

from portfolio.models import PortfolioEntry


def portfolio_entry(request, entry_slug):
    all_entries = PortfolioEntry.objects.order_by('when_created')
    current_entry = PortfolioEntry.objects.get(slug=entry_slug)
    context = {
        'all_entries': all_entries,
        'current_entry': current_entry,
    }
    return render(request, 'portfolio/entry.html', context)


def index(request):
    index_page = PortfolioEntry.objects.order_by('when_created').first()
    return portfolio_entry(request, index_page.slug)
