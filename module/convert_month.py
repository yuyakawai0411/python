from month import monthname
from month.monthname_module import MonthOjbect # クラスも読み込める

print('月を入力してください')

# moduleも読み込む
month_number = int(input())
print('モジュールの結果')
print(monthname.japanese(month_number))

# クラスで囲われたmoduleを読み込む
monthObject = MonthOjbect(month_number)
print('クラスで囲われたモジュールの結果')
print(monthObject.japanese())
