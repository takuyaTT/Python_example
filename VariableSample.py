# Pythonの場合は全てがオブジェクト
valA = 'aaa'
valB = 'aaa'

print(valA == valB) # True
print(valA is valB) # True
# id() -> メモリの番地を取得
print('valAのメモリアドレス = ' + str(id(valA)))
print('valBのメモリアドレス = ' + str(id(valB)))

valC = 100
valD = 100.0
print(valC == valD) # True
print(valC is valD) # False
print('valCのメモリアドレス = ' + str(id(valC)))
print('valDのメモリアドレス = ' + str(id(valD)))
# ==(!=)は値の比較を行う
# 違う型同士での比較の場合は、型を統一して比較を行う
# Javaでいうところのequalsメソッド
# is(is not)は参照先が同一か比較を行う
# Javaでいうところの==演算子

# 複数の単語からなる変数名はアンダースコアで区切る
total_price = 100
# 定数は大文字
TAX = 1.1
print('合計' + str(int(total_price * TAX))) # 110

# del -> 変数を削除する
del(valA)
# 以下はエラーになる
# print(valA)