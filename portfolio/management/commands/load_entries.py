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
        entries_with_file = set()
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
            title = metadata.get('title')
            head = str(soup.head)
            body = str(soup.body)
            entry, created = PortfolioEntry.objects.get_or_create(title=title)
            entries_with_file.add(entry)
            entry.head = head
            entry.body = body
            entry.__dict__.update(**metadata)
            entry.save()
            if created:
                self.stdout.write('Added new entry %s' % title)
            else:
                self.stdout.write('Updated existing entry %s' % title)
        # Clean up entries without a corresponding .html file
        entries_without_file = (set(PortfolioEntry.objects.all()) -
                                entries_with_file)
        for old_entry in entries_without_file:
            self.stdout.write('Deleting old entry %s' % old_entry.title)
            old_entry.delete()
