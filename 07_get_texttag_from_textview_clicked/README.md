# 07_get_texttag_from_buffer

[戻る](../README.md)

<br>

## 内容 

### テキスト位置によるカーソル形状の変更

テキスト位置によるカーソル形状の変更は、以下のようにおこなう

1. Gtk.textviewへのGtk.EventControllerMotionの追加及び、シグナル'motion'と関数との紐付け

    1. Gtk.EventControllerMotionを定義する。
    2. Gtk.EventControllerMotionに対して、シグナル'motion'と関数motion_cbを紐付ける。
    3. Gtk.TextView（動作を監視する対象）にGtk.EventControllerMotionを追加する。

```
        controller = Gtk.EventControllerMotion.new()
        controller.connect("motion", self.motion_cb)
        self.textview.add_controller(controller)
```

2. カーソルの変更処理

    1. Window上のカーソル位置より指定Widget上でのカーソル位置を取得する。
    2. カーソル位置が判定可能かとカーソル位置のGtk.TextIterを取得する。
    3. カーソル位置のタグ(Gtk.TextTag)を取得して、任意のタグが存在しているか評価する。
    4. 評価結果をもとにカーソルを変更する。

```
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
```

<br>

### マウスのクリックイベントによる表示の変更

1. イベント・関数の定義
    1. Gtk.GestureClickを定義する
    2. Gtk.GestureClickで、シグナル"released"と関数とを紐付ける。
    3. Gtk.TextViewにGtk.GestureClickを追加する。

```
        controller = Gtk.GestureClick.new()
        controller.connect("released", self.released_cb)
        self.textview.add_controller(controller)
```

2. 関数での処理
    1. マウスのボタンを判定する。
    2. Window上のカーソル位置より指定Widget上でのカーソル位置を取得する。
    3. Gtk.TextView上での選択幅を確認する。
    4. Gtk.TextView上での位置より、Gtk.TextIterを取得して、そのTagを調べる。
    5. 所定のタグが存在した場合に処理する。

```
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
```

<br>

## 参考にしたHP

[戻る](../README.md)
