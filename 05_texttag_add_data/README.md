# 05_texttag_add_data

[戻る](../README.md)

<br>

## 内容 

Gtk.TextTagを継承した変数を追加可能にしたクラスにを作成して、それをGtk.TextTagTableに追加して使用する。
定義したタグを指定することで、タグ作成時に指定した変数の値を取得数rことができる。

```
        tag1 = TextTagAddData(data='main', size_points=16, name='tag1')
        table = Gtk.TextTagTable()
        table.add(tag1)
        buffer = Gtk.TextBuffer.new(table)
        buffer.insert_with_tags_by_name(
            buffer.get_end_iter(), 'テキスト', "tag1")
        self.textview.set_buffer(buffer)
```

<br>

## 参考にしたHP

[戻る](../README.md)
