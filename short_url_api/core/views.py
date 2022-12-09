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
        if not source_link:
            raise MultiValueDictKeyError

        short_link = services.set_link(request, source_link)

    except MultiValueDictKeyError:
        return Response({'error': 'link not provided'}, status=404)

    except ValueError:
        return Response({'error': 'Wrong link format'}, status=400)

    return Response({'link': short_link})


@api_view(http_method_names=(['get']))
def get_source(request, link_pk: str) -> Response:
    if not link_pk:
        return Response({'error': 'link is not provided'}, status=400)

    try:
        encrypted_pk = link_pk
        source_link = services.get_link(encrypted_pk)

    except ObjectDoesNotExist:
        return Response({'error': 'link does not exist'}, status=400)

    except ValueError:
        return Response({'error': 'Wrong link format'}, status=400)

    return Response({'source': source_link.source_link})
