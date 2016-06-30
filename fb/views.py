from __future__ import unicode_literals

import json
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from fb.models import Entry


def start(request):
    if not request.method == "POST":
        return HttpResponseRedirect(reverse('fb:home'))

    name = request.POST.get("name")
    mail = request.POST.get("email")

    if ((not name) or (not mail)):
        return HttpResponseRedirect(reverse('fb:home'))

    # if they've played before, trash any incomplete entries...
    previous_deal_entries = Entry.objects.filter(email=mail).filter(source__isnull=True)
    previous_deal_entries.delete()

    e = Entry()
    e.name = name
    e.email = mail
    #e.start = timezone.now()
    e.save()

    return render_to_response('home.html', {"entry": e})


@csrf_exempt
def check(request):
    inputs = json.loads(request.body)
    source = inputs["source"]
    array = inputs["payload"]
    entry_id = inputs["entryid"]

    entry = get_object_or_404(Entry, pk=entry_id)

    correct = []
    for x in range(1,101):
        s = ""
        if x % 3 == 0:
            s += "Fizz"
        if x % 5 == 0:
            s += "Buzz"
        if s == "":
            s = x
        correct.append(s)

    if array != correct:
        entry.bad_source = source
        entry.save()
        return HttpResponseBadRequest()

    entry.source = source
    entry.stop = timezone.now()
    entry.save()

    return HttpResponse()


def home(request):
    return render(request, 'start.html')


def table(request):
    if 'uncensored' in request.GET:
        template = 'results_uncensored.html'
    else:
        template = 'results.html'

    m = None
    if 'mail' in request.GET:
        m = request.GET['mail']

    results = Entry.objects.all().filter(source__isnull=False)
    s = sorted(results, key=Entry.duration)
    return render(request, template, {"results": s, 'email': m})
