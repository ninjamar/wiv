import gi
gi.require_version('Gtk','3.0')
gi.require_version('WebKit2','4.0')
from gi.repository import Gtk
import window

win = window.Window()
Gtk.main()
