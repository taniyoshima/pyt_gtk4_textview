# 06_get_texttag_from_buffer

[戻る](../README.md)

<br>

## 内容 

### Gtk.TextView上のテキストのTag情報の取得について

Gtk.TextView上に配置したテキストで、所定の位置の文字のtag(Gtk.TextTag)を取得するには、以下の作業をおこなう。

1. Gtk.TextBufferに対して位置の指定をおこないその場所のGtk.TextIterを取得する。
2. 取得したGtk.TextIterに対してget_tags()をおこなうことでGtk.TextTagをリストにしたものを取得する。
3. リスト内のGtk.TextTagを取得する。

```
        bool, iter = buffer.get_iter_at_line_offset(0, 2)
        print(iter.get_tags()[0].data)
```

<br>

## 参考にしたHP

[戻る](../README.md)
