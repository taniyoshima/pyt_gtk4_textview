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
    hovering_over_link = False

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        tag1 = TextTagAddData(data='main', size_points=16, name='tag1')
        tag2 = TextTagAddData(data='main', size_points=14, name='tag2')
        table = Gtk.TextTagTable()
        table.add(tag1)
        table.add(tag2)
        buffer = Gtk.TextBuffer.new(table)
        buffer.insert_with_tags_by_name(
            buffer.get_end_iter(), 'tag2', "tag2")
        buffer.insert_with_tags_by_name(
            buffer.get_end_iter(), ' tag1 ', "tag1")
        buffer.insert_with_tags_by_name(
            buffer.get_end_iter(), 'tag2', "tag2")

        self.textview.set_buffer(buffer)

        controller = Gtk.GestureClick.new()
        controller.connect("released", self.released_cb)
        self.textview.add_controller(controller)

        controller = Gtk.EventControllerMotion.new()
        controller.connect("motion", self.motion_cb)
        self.textview.add_controller(controller)

    def motion_cb(self, controller, x, y):
        x1, y1 = self.textview.window_to_buffer_coords(
            Gtk.TextWindowType.WIDGET, x, y)

        hantei, iter = self.textview.get_iter_at_location(x1, y1)
        if hantei:
            tags = iter.get_tags()

            for tag in tags:
                if tag.props.name == "tag1":
                    hovering = True
                    break
                else:
                    hovering = False
        else:
            hovering = False

        try:
            if hovering != self.hovering_over_link:
                self.hovering_over_link = hovering
                if self.hovering_over_link:
                    self.textview.set_cursor_from_name('pointer')
                else:
                    self.textview.set_cursor_from_name('text')

        except UnboundLocalError:
            return

    def released_cb(self, gesture_click, n_press, x, y):
        if gesture_click.get_button() > 1:
            return

        x1, y1 = self.textview.window_to_buffer_coords(
            Gtk.TextWindowType.WIDGET, x, y)
        buffer = self.textview.get_buffer()
        taple = buffer.get_selection_bounds()
        if taple == ():
            hantei, iter = self.textview.get_iter_at_location(x1, y1)

            if hantei:
                tags = iter.get_tags()

                for tag in tags:
                    if tag.props.name == "tag1":
                        print(tag.data)
                        break


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
