from flic import FlickrAPI

FLICKR_PUBLIC = '466c4c31e82b8739e5b07b5798a19129'
FLICKR_SECRET = 'f854572f81ad7c8a'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
cats = flickr.photos.search(text='kitten', per_page=5, extras=extras)
photos = cats['photos']
from pprint import pprint
pprint(photos)