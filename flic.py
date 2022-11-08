from flickrapi import FlickrAPI

FLICKR_PUBLIC = '466c4c31e82b8739e5b07b5798a19129'
FLICKR_SECRET = 'f854572f81ad7c8a'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_l'
cats = flickr.photos.search(text='kitten', per_page=1, extras=extras)
photos = cats['photos']
for photo in photos:
    print(photo['page'])