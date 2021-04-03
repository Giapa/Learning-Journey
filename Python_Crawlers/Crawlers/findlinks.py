from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    
    def __init__(self,homepage,page_url):
        super().__init__()
        self.homepage = homepage
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.homepage, value)
                    self.links.add(url)
    
    def page_links(self):
        return self.links