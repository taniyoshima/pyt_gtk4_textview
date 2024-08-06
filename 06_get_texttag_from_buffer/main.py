import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.taniyoshima.pyt_gtk4_textview.test2'


class TextTagAddData(Gtk.TextTag):
    def __init__(self, data, *args, **argv):
        Gtk.TextTag.__init__(self, *args, **argv)
        self.data = data


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"
    textview = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        tag1 = TextTagAddData(data='main', size_points=16, name='tag1')
        table = Gtk.TextTagTable()
        table.add(tag1)
        buffer = Gtk.TextBuffer.new(table)
        buffer.insert_with_tags_by_name(
            buffer.get_end_iter(), 'テキスト', "tag1")
        self.textview.set_buffer(buffer)

        bool, iter = buffer.get_iter_at_line_offset(0, 2)
        print(iter.get_tags()[0].data)



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
