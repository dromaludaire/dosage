# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter
from ..util import tagre


class xkcd(_BasicScraper):
    url = 'http://xkcd.com/'
    starter = bounceStarter(url, compile(tagre("a", "href", r'(/\d+/)', before="next")))
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://imgs\.xkcd\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+/)', before="prev"))
    help = 'Index format: n (unpadded)'
    description = u'A webcomic of romance, sarcasm, math, and language.'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').rsplit('/', 1)[-1])
        name = imageUrl.rsplit('/', 1)[-1].split('.')[0]
        return '%03d-%s' % (index, name)
