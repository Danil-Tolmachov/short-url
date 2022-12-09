from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core import services


@api_view(http_method_names=(['post']))
def create_link(request) -> Response:
    try:
        source_link = request.POST['link']
        short_link = services.set_link(request, source_link)
    except MultiValueDictKeyError:
        return Response({'error': 'link not provided'})

    except ValueError:
        return Response({'error': 'Wrong link format'})

    return Response({'link': short_link})


@api_view(http_method_names=(['get']))
def get_source(request) -> Response:

    try:
        encrypted_pk = request.POST['link'].split('/')[-1]
        source_link = services.get_link(encrypted_pk)
    except MultiValueDictKeyError:
        return Response({'error': 'link not provided'})

    except ObjectDoesNotExist:
        return Response({'error': 'invalid link'})

    return Response({'source': source_link.source_link})
