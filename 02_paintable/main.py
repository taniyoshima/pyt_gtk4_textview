import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk, GdkPixbuf


APPID = 'com.github.taniyoshima.pyt_gtk4_textview02'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"
    buffer = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file('./sample.png')
        texture = Gdk.Texture.new_for_pixbuf(pixbuf)
        self.buffer.insert_paintable(self.buffer.get_end_iter(), texture)

        self.buffer.insert(self.buffer.get_end_iter(), "こんにちは")



class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
