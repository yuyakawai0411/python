# モジュール、パッケージ、ライブラリの違い

## モジュール

xxx.py という 1 つのファイルにまとまった機能群を指す。
class の有無に関係なく、下記に示す 2 つのファイルはどちらもモジュールである。

**monthname.py**

```python
def japanese(month):
  month_name = {
    1: '睦月', 2: '如月', 3: '弥生', 4: '卯月', 5: '皐月', 6: '水無月', 7: '文月', 8: '葉月', 9: '長月', 10: '神奈月', 11: '霜月', 12: '師走'
  }

  try:
    response = month_name[month]
  except:
    response = 'その月は存在しません'

  return response

if __name__ == '__main__':
  print('importして使ってください')
```

**monthname_module.py**

```python
class MonthOjbect:
  def __init__(self, month):
    self.month = month

  def japanese(self):
    month_name = {
      1: '睦月', 2: '如月', 3: '弥生', 4: '卯月', 5: '皐月', 6: '水無月', 7: '文月', 8: '葉月', 9: '長月', 10: '神奈月', 11: '霜月', 12: '師走'
    }

    try:
      response = month_name[self.month]
    except:
      response = 'その月は存在しません'

    return response

if __name__ == '__main__':
  print('importして使ってください')

```

## パッケージ

複数のモジュールを 1 つのフォルダに入れたもの
以下のようなディレクトリ構造の場合、month ディレクトリがパッケージとなる。

- month
  - monthname
  - monthname_module

## ライブラリ

モジュールやパッケージの総称を示す。

# インポート

パッケージ、モジュール、関数のレベルでインポートすることができる。パッケージレベルだと名前衝突する可能性があるため、基本的にはモジュール以下のレベルでインポートする

## モジュール

```python
import calendar as cal
print(cal.month(2024, 4))
=> カレンダーが表示

# モジュールから特定の関数をインポートする
from calendar import month
month(2024, 4)
=> カレンダーが表示
```

## パッケージ

```python
# パッケージから特定のモジュールをインポートする
from datetime import date
date.today()
=> datetime.date(2024, 4, 8)

type(date.today())
=> <class 'datetime.date'>
```

## 疑問

- パッケージはどうやって作っているのか？ class の中に class をネストしているのか？
  - => パッケージはモジュールを集めたディレクトリを指すため、class は関係ない
- 自作した class をどうやって他のクラスから使うのか？ まずは file を import しないといけないと思う
  - => class を定義したモジュールを from して、その class を import したのち、インスタンス化すれば良い
- class 名で大文字から始まる場合と、小文字から始まる場合の違いは何？
  - => 命名規則では、class 名は大文字スタートの camel ケース
