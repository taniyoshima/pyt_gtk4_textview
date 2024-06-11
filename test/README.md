# pyt_gtk4_textview/test

[戻る](../README.md)

<br>

## 内容 

01_python_program  
python側でTextBufferにTextTagTable、TextTagを追加するプログラム


02_texttagtable
Gtk.TextTagTableにGtk.TextTagを登録する方法を確認するのに使用したプログラム  
Gtk.TextTagを登録するには、LayoutのChild Typeをtagにする必要があった。

```
  <object class="GtkTextTagTable" id="tagtable">
    <child type="tag">
      <object class="GtkTextTag">
        <property name="font">HackGen Console Bold 16</property>
        <property name="foreground-rgba">rgb(245,194,17)</property>
        <property name="name">tag1</property>
      </object>
    </child>
```
<br>

## 参考にしたHP

[戻る](../README.md)
