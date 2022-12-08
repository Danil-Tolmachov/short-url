from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core import services


@api_view(http_method_names=(['post']))
def create_link(request):

    try:
        source_link = request.POST['link']
        short_link = services.set_link(request, source_link)
    except MultiValueDictKeyError:
        return Response({'error': 'link not provided'})

    except ValueError:
        return Response({'error': 'Wrong link format'})

    return Response({'link': short_link})
