from django.db.models import F

from website.models import ViewCounter


class CountView(object):
    def process_request(self, request):
        url_path = request.path
        if not url_path.startswith('/admin'):
            vc, _ = ViewCounter.objects.get_or_create(url=request.path)
            vc.views = F('views') + 1
            vc.save()
