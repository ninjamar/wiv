import requests
from urllib.parse import urlparse

def url(_url):
  p_url = urlparse(data)
  if p_url.scheme in ('https','http'):
      try:
          requests.get(f'{p_url.scheme}://{p_url.netloc}')
          self.webview.load_uri(data)
      except requests.exceptions.ConnectionError:
          self.webview.load_uri('https://ninjamar.github.io/wiv/invalid-page.html')
  else:
      self.webview.load_uri(f'https://google.com/search?q={data}')
