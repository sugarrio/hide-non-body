# Hide Selected Non-Body Objects

選択中のオブジェクトのうち、名前に `body` を含まないものを非表示にするBlenderアドオンです。

Releasesよりzipファイルをダウンロードしてご利用ください。

## 動作環境

- Blender 2.79
- Blender 4.2 / 5.1

他verでの動作は確認していません。

## 動作

`body` の判定では大文字・小文字を区別しません。

- `body`
- `Body`
- `BODY`
- `avatar_body`

上記の名前はすべて表示したまま残します。

## インストール

1. Blenderの「編集 → プリファレンス → アドオン」を開く
2. 「インストール」または「ディスクからインストール」を選ぶ
3. `hide_non_body.py` を選択する
4. `Hide Selected Non-Body Objects` を有効にする

## ボタンの場所

### Blender 2.79

3Dビューで `T` キーを押し、左側の `Tools` を開きます。

### Blender 4.2 / 5.1

3Dビューで `N` キーを押し、右側の `Hide Tools` タブを開きます。

## 注意

オブジェクトモードで使用してください。
