import metadata_parser
import os
from bs4 import BeautifulSoup

from django.conf import settings
from django.core.management.base import BaseCommand

from portfolio.models import PortfolioEntry


class Command(BaseCommand):
    help = 'Load portfolio entries'

    def wrap_soup(self, inner, outer):
        replaced_content = inner.replace_with(outer)
        outer.append(replaced_content)

    def wrap_html_tags(self, soup):
        # Wrap img tags
        for img in soup.find_all('img'):
            div_class = ''
            if 'big' not in img.attrs:
                div_class = 'col-xs-12 col-md-6'
            img_div = soup.new_tag('div', **{'class': div_class})
            self.wrap_soup(img, img_div)
            caption = img.attrs.pop('caption', None)
            if caption:
                caption_div = soup.new_tag('div', **{'class': 'img-caption'})
                caption_div.append(caption)
                img.insert_after(caption_div)

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
            self.wrap_html_tags(soup)
            self.stdout.write('Adding entry %s' % metadata.get('title'))
            pe = PortfolioEntry.objects.create(
                head=str(soup.head), body=str(soup.body), **metadata)
            pe.save()
