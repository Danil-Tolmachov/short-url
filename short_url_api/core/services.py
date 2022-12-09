from core.models import Link
from core.utils import encode_link, validate_link, decode_link


# receives source link
# returns short link
def set_link(request, link: str) -> str:

    if not validate_link(link):
        raise ValueError

    link_obj = Link.objects.create(source_link=link)

    host = request.build_absolute_uri('/')
    short_link = host + encode_link(link_obj.pk)

    return short_link


# receives cyphered(base64) pk
# returns redirect link
def get_link(encoded_pk: str) -> str:
    decoded_pk = decode_link(encoded_pk)
    source = Link.objects.get(pk=decoded_pk)
    return source
