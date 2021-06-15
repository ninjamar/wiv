import gi
gi.require_version('Gtk','3.0')
gi.require_version('Webit2','4.0')
from gi.repository import Gtk,Webkit2
from urllib.parse import urlparse
import requests
class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Wiv")
        self.connect('destroy',Gtk.main_quit)
        self.set_default_size(800,600)
        self.webview = WebKit2.WebView()
        self.head = Gtk.HeaderBar()
        self.head.set_show_close_button(True)
        self.make_search_bar()
        self.set_titlebar(self.head)
        self.add(self.webview)
        self.show_all()
    def make_search_bar(self):
        self.search_bar = Gtk.Entry()
        self.search_bar.set_size_request(self.get_size()[0]/1.3,30)
        self.search_bar.connect('activate',self.enter_page)
        self.head.set_custom_title(self.search_bar)
        self.connect('check-resize',self.reposition)
    def enter_page(self,entry):
        data = entry.get_text()
        p_url = urlparse(data)
        if p_url.scheme in ('https','http'):
            try:
                requests.get(f'{p_url.scheme}://{p_url.netloc}')
                self.webview.load_uri(data)
            except requests.exceptions.ConnectionError:
                self.webview.load_uri('https://ninjamar.github.io/wiv/invalid-page.html')
        else:
             self.webview.load_uri(f'https://google.com/search?q={data}')
        #self.webview.load_uri(url)
    def reposition(self,window):
        self.search_bar.set_size_request(self.get_size()[0]/1.3,30)

win = Window()
Gtk.main()
