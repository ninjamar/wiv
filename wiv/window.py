from gi.repository import Gtk,WebKit2
import url
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
        self.search_bar.connect('activate',lambda entry:self.webview.load_uri(url.url(entry.get_text())))
        self.head.set_custom_title(self.search_bar)
        self.connect('check-resize',self.reposition)
    def reposition(self,window):
        self.search_bar.set_size_request(self.get_size()[0]/1.3,30)
