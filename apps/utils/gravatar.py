import urllib, hashlib

GRAVATAR_HTTP_URL = 'http://www.gravatar.com/avatar/'
GRAVATAR_HTTPS_URL = 'https://secure.gravatar.com/avatar/'

DEFAULT_IMAGES = ['mm', 'identicon', 'monsterid', 'wavatar', 'retro']

def get_gravatar_link(email, size=40, default_image_index=0, is_https=False):
    if email:
        email_hash = hashlib.md5(email.lower()).hexdigest()
    else:
        email_hash = '00000000000000000000000000000000'
    if is_https:
        base_url = GRAVATAR_HTTPS_URL
    else:
        base_url = GRAVATAR_HTTP_URL
    gravatar_url = base_url + email_hash + '?'
    gravatar_url += urllib.urlencode(
        {'d':DEFAULT_IMAGES[default_image_index], 's':str(size)}
    )
    return gravatar_url
