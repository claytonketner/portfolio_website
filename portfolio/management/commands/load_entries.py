import metadata_parser
import os
from bs4 import BeautifulSoup

from django.conf import settings
from django.core.management.base import BaseCommand

from portfolio.models import PortfolioEntry


class Command(BaseCommand):
    help = 'Load portfolio entries'

    def handle(self, *args, **kwargs):
        PortfolioEntry.objects.all().delete()
        file_base = settings.PORTFOLIO_FILES_DIR
        for filename in os.listdir(file_base):
            if '.html' not in filename:
                continue
            full_path = os.path.join(file_base, filename)
            if os.path.isdir(full_path):
                continue
            contents = open(full_path, 'r').read()
            md_parser = metadata_parser.MetadataParser(
                html=contents, strategy='meta')
            metadata = md_parser.metadata['meta']
            soup = BeautifulSoup(contents, 'html.parser')
            self.stdout.write('Adding entry %s' % metadata.get('title'))
            pe = PortfolioEntry.objects.create(
                head=str(soup.head), body=str(soup.body), **metadata)
            pe.save()
