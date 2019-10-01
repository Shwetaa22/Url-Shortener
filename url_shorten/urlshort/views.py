import random
import string
from django.shortcuts import render


def customUrl(request):
    return render(request, 'urls.html')


def newshorturl(request):
    print('rew',request.method)
    url = request.GET.get('short_url')
    print(url)
    string_characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(string_characters) for i in range(6))
    short_url = "https://shorturl/"+ short_url
    print(short_url);
    data = {
        "url":url,
        "short_url":short_url
    }
    print(data)
    return render(request, 'urls.html', data)
    # return Response(url, status=status.HTTP_200_OK)
