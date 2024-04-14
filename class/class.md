## クラス

### クラス定義

- イニシャライザの定義
- メンバ変数の定義
- インスタンスメソッドの定義

```python
class Staff: # 大文字はじまりでなくてもOK
   def __init__(self, bonus):
        self.bonus =  bonus # メンバ変数の定義
   def salary(self): # インスタンスメソッドの定義、第一引数にselfを指定することは必須
        salary = self.bonus + 1000
        return salary
```

### インスタンスメソッドを呼び出す

- インスタンス化
- 呼び出し

```python
yuya = Staff(5000)
yuya.bonus # メンバ変数の呼び出し
=> 5000
yuya.salary() # メソッドの呼び出し
=>6000
```

### クラス継承

class の引数に継承する親クラスを記述する。継承後の挙動は、基本的には Ruby と同じ

```python
class KitchenStaff(staff):
   def salary(self):
        salary = self.bonus + 3000
        return salary
```

## あとで知りたい

- Ruby のクラスメソッド、スタティックメソッドが python だとどうなるか？
- Ruby の Module が python だとどうなるか？
