# 組み込み関数や標準ライブラリを確認する

以下の URL で確認できる。
https://docs.python.org/3/library/index.html

# オブジェクトを調べる

## type() オブジェクトが何かを確認

type メソッドを使えば、何のオブジェクトかを把握することができる

```terminal
$ python
>>> name = 'test'
>>> print(type(name))
<class 'str'>
>>> number = 1
>>> print(type(number))
<class 'int'>
```

## hasattr() オブジェクトが特定の要素を持っているかを確認

以下のように hasattr を使って、オブジェクトがその要素を持っているか確認できる。

```
>>> name = 'test'
>>> number = 1
>>> print(hasattr(name, 'is_integer'))
False
>>> print(hasattr(number, 'is_integer'))
True
```

## dir() オブジェクトが持っている要素の一覧を確認

dir を使うと要素一覧を出してくれる。引数を指定しないと、現状のスコープで使える要素(メソッド、変数 etc)の一覧を出してくれる。

```
# 引数を指定する
>>> name = 'test'
>>> print(dir(name))
=> [lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 引数を指定しない
>>> print(dir())
=> [key', 'key_array', 'limited_cd', 'list', 'name', 'normal_cd', 'test', 'tuple', 'weight']
```

# デバック

## pdb ruby の binding.pry と同じ

```
import pdb
...
pdb.set_trace() # プログラムが一時停止し、インタラクティブモードになる
...
```

# ライブラリ

## **file** ライブラリのファイルの path を表示する

```python
import calendar

print(calendar.__file__)
=> ファイルの場所が表示される
```

# ファイルを操作する

## open() ファイルを読み取り、ファイルオブジェクトを生成する

ファイルの path を指定して、ファイルを読み込み、ファイルオブジェクトを生成する

```python
# 第一引数にはファイルのpathを記述する
# 第二引数にはモードを指定する。r(読み取り)、w(書き込み)、r+(読み取り+書き込み)を主に使う
file_object = open('python.txt', 'r+') # ファイルオブジェクトの生成
file_object.write('text') # ファイルに書き込み
file_object.read() # ファイルの中身を表示(read()を使うたびにファイルの読み取り位置が変更される。seek()等で読み取り位置を戻せる)
file_object.close() # ファイルオブジェクトを修了し、ファイルに書き込んだ結果を反映させる。
```

**open とよく使う with ブロック**
with を使うことで with 以下の処理が終了した時に、close()が呼ばれる。これにより、close()の呼び忘れを防げる。

```python
with open('python.txt', 'r+') as file_object
   file_object.write('withオプジョンを使った')
```

# webbrowser を開く

url を指定して、ブラウザを別タブで開くことができる

```python
import webbrowser
url = "https://ja.wikipedia.org/w/api.php"
webbrowser.open(url)
=> 別タブでブラウザーが開く
```
