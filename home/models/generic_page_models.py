from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class GenericPage(Page):
    body = RichTextField(blank=True)

    class Meta:
        verbose_name = "Generic Page"

GenericPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body'),
]
