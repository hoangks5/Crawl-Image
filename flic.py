from flickrapi import FlickrAPI

FLICKR_PUBLIC = '466c4c31e82b8739e5b07b5798a19129'
FLICKR_SECRET = 'f854572f81ad7c8a'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_o,url_c'
cats = flickr.photos.search(text='kitten', per_page=100, extras=extras)
photos = cats['photos']['photo']
list = []
for photo in photos:
    for i in range(0,len(extras),1):
        try:
            list.append(photo[extras[i]])
            break
        except:
            pass
string = '\n'.join(list)
with open('fick.txt','w',encoding='utf-8') as f:
    f.write(string)
    f.close()