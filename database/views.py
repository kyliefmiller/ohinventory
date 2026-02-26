from django.shortcuts import render

from .models import OHEntry
from .filters import EntryFilter

def entry_list(request):
    entries = OHEntry.objects.all()

    entry_filter = EntryFilter(request.GET, queryset=entries)

    return render(request, 'entries.html', {'filter': entry_filter})

def single_entry(request, id=None):
    return render(request, 'single-entry.html', {'entry': OHEntry.objects.get(pk=id)}) 