import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.taniyoshima.pyt_gtk4_textview.test'


class Gtk4TestTest(Gtk.Window):

    def __init__(self, app):
        Gtk.Window.__init__(
            self, application=app, title='Test')

        tag = Gtk.TextTag(name='name')
        tag_table = Gtk.TextTagTable()
        tag_table.add(tag)
        buffer = Gtk.TextBuffer.new(tag_table)
        textview = Gtk.TextView()
        textview.set_buffer(buffer)
        buffer.insert_with_tags_by_name(
            buffer.get_end_iter(), 'テキスト', 'name')

        self.set_child(textview)


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
