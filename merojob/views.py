from django.views import generic


class IndexView(generic.RedirectView):
    pattern_name = 'bills:list'
