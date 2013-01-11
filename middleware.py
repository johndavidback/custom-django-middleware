# This is going to be great.
from django.conf import settings
from django.contrib.sites.models import Site


class MultisiteMiddleware(object):
    """
    This middleware allows you to run multiple sites from the same
    Django administration.  The simple premise being you need to have
    one site in your Sites admin section for every unique domain,
    for example:
    www.mysite.com/
    blog.mysite.com/
    old-music-videos-from-1980.mysite.com/
    """

    def process_request(self, request):
        """
        This middleware is run before the request is passed through
        """

        # Grab the current domain
        domain = request.META.get('HTTP_HOST', None)

        # Get the site from the domain name, if possible, otherwise
        # default to our main site (assumbed to be pk=1)
        try:
            site = Site.objects.get(domain=domain)
            settings.SITE_ID = site.id
        except:
            settings.SITE_ID = 1

        