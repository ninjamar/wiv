#!/usr/bin/env python3
import gi
gi.require_version('Gtk','3.0')
gi.require_version('WebKit2','4.0')
from gi.repository import Gtk,WebKit2
class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Viw")
        self.connect('destroy',Gtk.main_quit)
        self.webview = WebKit2.WebView()
        self.head = Gtk.HeaderBar()
        self.entry = Gtk.Entry()
        self.head.set_show_close_button(True)
        self.entry.connect('activate',self.enter)
        self.head.set_custom_title(self.entry)
        self.set_titlebar(self.head)
        self.add(self.webview)
        self.show_all()
    def enter(self,entry):
        url = entry.get_text()
        self.webview.load_uri(url)

win = Window()
Gtk.main()
