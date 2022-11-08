# Import API class from pexels_api package
from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = '563492ad6f91700001000001c6decedb146c4053a03e0b07bee17e8b'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('kitten', page=1, results_per_page=1000)
# Get photo entries
photos = api.get_entries()
# Loop the five photos
for photo in photos:
  print('Photo original size: ', photo.original)