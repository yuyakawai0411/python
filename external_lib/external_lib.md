## pyenv

### これ何？

python のバージョンを管理するパッケージ

### コマンド

1. python のバージョン一覧

```
$pyenv versions
```

2. python のバージョン切り替え

```
$pyenv local <バージョン>
```

## pip

### これ何？

パッケージを管理するツール

### コマンド

1. インストール済みのパッケージの一覧

```
$pip list
```

2. パッケージのインストール

```
$pip install <パッケージ名>
```

3. パッケージのアップデート

```
$pip install --upgrade <パッケージ名>
```

4. パッケージのアンインストール

```
$pip uninstall  <パッケージ名>
```

## ipython

### これ何？

python のインタラクティブ shell

### コマンド

1. 対話 shell の起動

```
$ ipython
```

2. コードに埋め込み、binding.pry のように使うことも可能

```python
from IPython.core.debugger import set_trace
...
set_trace()
...
```

## request

### これ何？

python で API リクエストができる

### コマンド

```python
import requests
url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=160002"
response = requests.get(url).json()
=> json形式でパラメータが表示

# request bodyを使う時は、第二引数に辞書型のbodyを入れる
import requests
url = "https://ja.wikipedia.org/w/api.php"
params = { 'format' :  'json', 'action': 'query', 'titles': '日本の歴史', 'prop': 'revisions', 'rvprop': 'content' }
response = requests.get(url).json()
=> json形式でパラメータが表示
```
