from django.http import HttpResponse
from django.shortcuts import HttpResponsePermanentRedirect
from django.urls import reverse


def Index(request):
    return HttpResponsePermanentRedirect(reverse('App_Blog:blog_list'))
