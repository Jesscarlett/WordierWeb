from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'chat', 'hchat', 'match', 'read', 'fivehundredwords', 'fivehundredgame', 'sixhundredwords', 'sixhundredgame',
                'sevenhundredwords', 'sevenhundredgame', 'onethousandadj', 'aboutai', 'pswords', 'seniorwords', 'quotes', 'conversations',
                'choice_helper', 'thesaurus', 'fill_sentence', 'paragraph', 'hangman_junior', 'privacy']

    def location(self, item):
        return reverse(item)



