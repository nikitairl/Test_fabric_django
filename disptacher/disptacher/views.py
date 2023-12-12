import json

from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from api.models import Client, Dispatch, Message

from .settings import SOCIAL_AUTH_AUTH0_DOMAIN, SOCIAL_AUTH_AUTH0_KEY


def index(request):
    total_dispatches = Dispatch.objects.count()
    total_clients = Client.objects.count()
    total_messages = Message.objects.count()

    context = {
        'total_dispatches': total_dispatches,
        'total_clients': total_clients,
        'total_messages': total_messages,
    }
    return render(request, 'index.html', context)


def profile(request):
    user = request.user
    auth0_user = user.social_auth.get(provider='auth0')
    user_data = {
        'user_id': auth0_user.uid,
        'user_name': user.first_name,
        'picture': auth0_user.extra_data['picture'],
    }
    context = {
        'user_data': json.dumps(user_data, indent=4),
        'auth0_user': auth0_user,

    }
    return render(request, 'profile.html', context)


def logout(request):
    django_logout(request)
    domain = SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000/'

    return HttpResponseRedirect(
        f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}'
    )
