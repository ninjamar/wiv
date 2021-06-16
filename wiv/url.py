import requests
from urllib.parse import urlparse

def url(_url):
  p_url = urlparse(data)
  if p_url.scheme in ('https','http'):
      try:
          requests.get(f'{p_url.scheme}://{p_url.netloc}')
          return data
      except requests.exceptions.ConnectionError:
          return 'https://ninjamar.github.io/wiv/invalid-page.html'
  else:
      return f'https://google.com/search?q={data}')
