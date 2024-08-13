# *を使うと指定数分の連結(繰り返し)が可能
strA = '-+-'
delim_str = strA * 10
strA *= 10
print(strA)      # -+--+--+--+--+--+--+--+--+--+-
print(delim_str) # -+--+--+--+--+--+--+--+--+--+-

# 負数のインデックス指定も可能
# 末尾は-1からスタート
# 通常のインデックス - 文字数 が負数のインデックスとなる
strB = 'ABCDEFG'
print('対象文字列:' + strB + ' 文字数:' + str(len(strB)))
print('3文字目:' + strB[2]) # C
# 2(通常のインデックス) - 7(文字数) = -5(負数のインデックス)
print('-5指定(3文字目):' + strB[-5])

# slice機能
# 文字列切り出し。開始インデックス、終了インデックスを指定
# 開始インデックスから終了インデックスまでの数値を指定するが、終了インデックスに対応する要素は除外される
# for i in range(終了インデックス) i < 終了インデックス で処理しているから？
strC = 'hello.txt'
# 開始インデックスも終了インデックスも省略 -> 全部取得
print(strC[:]) # hello.txt
# 開始インデックスを省略すると、先頭から終了インデックスまでを取得
print(strC[0:5]) # hello
print(strC[:5])  # hello
# 終了インデックスを省略すると、開始インデックスから終了インデックスまで取得
print(strC[6:9]) # txt
print(strC[6:])  # txt

for i in range(24):
    print(i)

str_a = 'abcdefghijklmnopqrstu'
print()
print(len(str_a))
print(21 - 6)
print(str_a[-6]) 
print(str_a[-6:-4])