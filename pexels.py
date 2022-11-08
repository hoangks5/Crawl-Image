# Import API class from pexels_api package
from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = '563492ad6f91700001000001c6decedb146c4053a03e0b07bee17e8b'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('kitten', page=1, results_per_page=100)
# Get photo entries
photos = api.get_entries()
# Loop the five photos
list = []
for photo in photos:
  list.append(photo.original)
string = '\n'.join(list)
with open('pexels.txt','w',encoding='utf-8') as f:
    f.write(string)
    f.close()