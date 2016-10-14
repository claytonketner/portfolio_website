from django.db.models import F
from django.shortcuts import render

from portfolio.models import PortfolioEntry


def portfolio_entry(request, entry_slug):
    all_entries = PortfolioEntry.objects.order_by('-is_index', '-when_created')
    all_entries = all_entries.exclude(is_index=True)
    current_entry = PortfolioEntry.objects.get(slug=entry_slug)
    current_entry.views = F('views') + 1
    current_entry.save()
    context = {
        'all_entries': all_entries,
        'current_entry': current_entry,
    }
    return render(request, 'portfolio/entry.html', context)


def index(request):
    index_page = PortfolioEntry.objects.get(is_index=True)
    return portfolio_entry(request, index_page.slug)
