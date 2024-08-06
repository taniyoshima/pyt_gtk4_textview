# pyt_gtk4_textview

<br>

## 内容 

Gtk.TextViewに文字を表示するサンプルプログラムです。文字の装飾は、Gtk.TextTagTableに登録したGtk.TextTagを選択することで指定しています。
Gtk.TextTagの設定などはuiファイル内でおこない、文字の挿入をPython側でしています。
uiの作成には、cambalacheを使用します。

<br>

### [01_texttag](./01_texttag/README.md)

Gtk.TextViewにGtk.TextTagで指定した装飾をした文字を表示するプログラム

<br>

### [02_paintable](./02_paintable/README.md)

Gtk.TextViewに画像を表示するプログラム

<br>

### [03_python_program](./03_python_program/README.md)

Gtk.TextTagを使用して、Gtk.TextView上のテキストの書式を指定する。

<br>

### 04_testtagtable

Gtk.TextTagTableにGtk.TextTagを追加する。

<br>

### [05_texttag_add_data](./05_texttag_add_data/README.md)

Gtk.TextBufferのTag情報(クラスを継承したものにデータを追加)を追加する。

<br>

### [06_get_texttag_from_buffer](./06_get_texttag_from_buffer/README.md)

Gtk.TextViewのGtk.TextBufferのTag情報(追加したデータ)を取得する。Gtk.TextTagを継承したものを作成して、それにデータを追加する。

<br>

### [07_get_texttag_from_testview_clicked](./07_get_texttag_from_textview_clicked/README.md)

Gtk.TextView上でマウスクリックした位置を取得する。Gtk.TextViewにリンクボタンを作成するのに使用。

<br>

### [testフォルダのプログラム](./test/README.md)

<br>

## 履歴

2024/6/12 Gtk.TextViewにTextTagで装飾した文字を表示するプログラム作成  
2024/6/12 Gtk.TextViewに画像を貼り付けるプログラム作成（02_paintable)  

<br>

## 参考にしたHP
