from urllib.parse import urlparse

#get domain
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
#getting subname 
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc #network location
    except:
        return ''
