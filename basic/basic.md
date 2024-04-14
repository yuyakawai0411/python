## 条件分岐

Ruby と基本的には同じで、以下のように if を使う。

```python
# 条件分岐
if (18 <= age):
    print('大人料金です')
elif (65 <= age):
    print('シニア料金です')
else
   print('子供料金です')
```

### Ruby との違い

1. Ruby の`&&`は`and`、Ruby の`||`は`or`になる。

```python
# and
if ((18 <= age) and (65 <= age)):
    print('シニア料金です')
else
   print('子供料金です')
```

## 繰り返し

Ruby と基本的には同じで、for 文でデータから要素を 1 づつ取り出し、定義した変数に格納して処理を実行する。データには主に、リスト型、辞書型、range 型が使われる。

```python
for 変数 in データ:
  処理
```

### Ruby との違い

1. データに辞書型を渡した時は、key の値が変数に格納される。

```python
# 辞書型
dict = { 'name': 'yuya', 'age': 29, 'weight': 60 }

for element in dict:
    print(element)
    print(dict[element])
=>
name
yuya
age
29
weight
60
```

2. Ruby の`next`は`continue`、Ruby の`break`は`break`のまま

```python
# 処理のスキップ
for i in [10, 20, 30]:
    if i == 10:
        continue
    print(i)
```

## 関数定義

Ruby と基本的には同じ。

```python
# 定義
def calculate():
    print('計算中です')

# 呼び出し
calculate()
=> '計算中です'
```

### Ruby との違い

戻り値が必要な場合は、return が必須
