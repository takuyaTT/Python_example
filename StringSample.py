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

# upper
str_upper = "upp"
print(str_upper.upper()) # UPP

# lower
str_lower = "LOWER"
print(str_lower.lower()) # lower

# startswith
# 指定した文字から始まる場合はTrueを返す
str_start = "python"
print(str_start.startswith('py')) # True

# endswith
# 指定した文字で終了する場合はTrueを返す
str_end = "python_end"
print(str_end.endswith('end')) # True

# 複合例
txt_file = "Sample.MD"
print(txt_file.lower().endswith('.md')) # True

# replace
# 文字列置換。個数を指定できる
rep_samp = "Java,JavaScript,Python"
rep_res = rep_samp.replace('J', 'j')
print(rep_res) # java,javaScript,Python
rep_res = rep_samp.replace('J', 'j', 1)
print(rep_res) # java,JavaScript,Python

# 文字列検索
# find -> 先頭から検索。該当なしの場合は-1を返す
find_samp = "Java Python Ruby"
print(find_samp.find('Python')) # 5
# 先頭から空白までを抜き出して出力
print(find_samp[:find_samp.find(' ')]) # Java
# 先頭から空白の開始位置を取得し、末尾から空白までの開始位置を取得して、開始:終了を指定して出力
print(find_samp[find_samp.find(' ')+1:find_samp.rfind(' ')]) # Python
# 最後の空白開始位置を取得し、以降を抜き出して出力
print(find_samp[find_samp.rfind(' ')+1:]) # Ruby
