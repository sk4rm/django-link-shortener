import base64
import hashlib
from pydoc import pager
from ssl import get_protocol_name

from django.http import HttpResponseNotFound, HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.shortcuts import redirect, get_object_or_404, render
from django.template import loader
from django.views.decorators.csrf import csrf_protect

from shortener.models import Link


def hello_view(request):
    return HttpResponse('Hello World!')


def shorten_form(request):
    template = loader.get_template('new_link.html')
    return HttpResponse(template.render({}, request))


@csrf_protect
def shorten_link(request):
    if not request.POST:
        return HttpResponseNotAllowed('cannot do this bro')

    short_hash = hash_url(request.POST['destination_url'])
    Link.objects.get_or_create(short_hash=short_hash, destination_url=request.POST['destination_url'])

    return HttpResponse(f'http://{request.get_host()}/{short_hash}')


def hash_url(url: str) -> str:
    h = hashlib.md5(url.encode()).digest()
    b = base64.b64encode(h).decode()
    a = ''.join(c for c in b if c.isalpha())[:6]
    return a


def redirect_view(request, short_hash):
    return redirect(get_object_or_404(Link, short_hash=short_hash).destination_url)
