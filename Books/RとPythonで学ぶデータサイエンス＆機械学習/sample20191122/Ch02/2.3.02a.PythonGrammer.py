# -*- coding: utf-8 -*-

#上記は、このスクリプトの文字コードがUTF-8であることを示す記述
#プログラムの実行上は、記述の必要はありません

## Pythonの文法

## #はコメントを表します

#---------------------------------------------------------------
### 四則演算と代入

# 四則演算と累乗の例を示します。  
# 累乗はエクセルやRで使われる ^ ではなく、** で表します。
#---------------------------------------------------------------

#算術演算

print(3 + 2)       #和
print(3 - 2)       #差
print(3 * 2)       #積
print(3 / 2)       #商
print(3 ** 2)      #累乗

print(3**2)        #スペースはなくてもよい

#---------------------------------------------------------------
# 代入操作は = で行います。  
# 値を表示する場合は print() 関数を使います。  
#---------------------------------------------------------------

#オブジェクトへの格納（代入操作）

a = 1       #1をAに格納
A = 2       #2をAに格納
b = a + A   #a+Aをbに格納

print( b )  #bを表示

a   #print()を書かないと値が表示されない
A   #ただし、ブロックの最後に書かれたオブジェクトの値は表示される

#---------------------------------------------------------------
### print()文

# 引数をカンマで区切れば、複数のオブジェクトの値を表示できます。  
# 引用符の中で、バックスラッシュを使うと改行やタブを加えられます。  

# >バックスラッシュは￥記号か／のいずれかです。
#---------------------------------------------------------------
  
#print()の使い方

print( "hello!")
print( a, A )
print( "a =", a, ", A =", A, "\n --- and a+A =", a+A )

# "\n" で改行を挿入
# "\t" でタブを挿入

# "%s" 後の%で指定された文字列を表示する
# "%f" 後の%で指定された数値を表示する
#   --- "%05.2"のように、桁数を指定することが可能
price = 2.25 ;  fruit = "orange"
print( "\nSale! %s\t --> $%05.2f" %(fruit, price) )

#---------------------------------------------------------------
### リスト

# リストは複数の要素を格納する箱のようなものです。  

# >Rのベクトルとの違いに注意してください。  
#　　一括で計算の対象とすることはできません。  
#---------------------------------------------------------------

#list
# listはただの「箱」で直接計算はできない

a = [1, 2, 3]    #(1, 2, 3)をaに格納
print("a is ", a)       #aはリスト

x = [1.5, "abc", 2]     #型が異なる要素が含まれていてもよい  
print("x is ", x)

A = range(4, 7)  #(4, 5, 6)をAに格納
print("A is ", A)       #aはrange object

A = list(A)             #Aをリストに変換
print("A is ", A)       #Aはリスト

print("a+A is ", a+A)   #"+"でリストを結合（足し算ではない）

#---------------------------------------------------------------

#リスト型のオブジェクトに対する操作
fr1 = "apple"                   #文字列
fr2 = ["orange", "lemon"]       #文字列を要素とするリスト

fr2.insert(0, fr1)              #0はリストの先頭を示す
print("inserted -> ", fr2)

fr2.append(fr1)                 #.append()は最後に要素を追加する
print("appended -> ", fr2)

#---------------------------------------------------------------

#リストの扱いに関する注意
fr3 = fr2                       #fr2をfr3に代入（割り当て）
fr2[3] = "kiwi"                 #fr2の最後の要素をkiwiに変更

print("\nfr2 is ", fr2)         #変更後のfr2
print("fr3 is ",   fr3)         #fr2の変更がfr3に反映されている

fr4 = fr1                       #fr1をfr4に代入（コピー）
fr1 = "melon"                   #fr1をmelonに変更
print("\nfr1 is ", fr1)         #変更後のfr1
print("fr4 is "  , fr4)         #fr1の変更はfr4に反映されない

#---------------------------------------------------------------
### 論理式

# 比較演算子を使うと結果は論理値として返されます。  

# >比較演算子として >, >=, <, <=, ==, != などを使うことができます。  
#  結果はTrueかFalseのいずれかとなります。
#---------------------------------------------------------------

#比較演算

bool_list = [ 2 >= 0.5,       2 < 1+1,
             "pen"=="apple", "pen"!="apple"] 
print(bool_list)

#---------------------------------------------------------------
### 型の確認

# オブジェクトの型は、関数type()で確認できます。
#---------------------------------------------------------------

#オブジェクトの型

print( "fr1 : ", type(fr1) )    #type()で型を表示  文字列
print( "fr2 : ", type(fr2) )                      #リスト
print( "3   : ", type(3)   )                      #整数
print( "3.3 : ", type(3.3) )                      #実数(浮動小数点)
print( "True: ", type(True))                      #論理

#---------------------------------------------------------------
### 添字

# リストから要素を取り出す場合は添字を指定します。
#---------------------------------------------------------------

#添え字（インデクス）
# -- Pythonでは1ではなく0から数える

print( fr2 )  

print("\n")  
print(" 0, 2:", fr2[0],  fr2[2] )  #頭から数える
print("-1,-2:", fr2[-1], fr2[-2])  #最後から数える

print("\n")
print("from 0 to 3:", fr2[0:3])     #0から3の前まで（つまり2まで）
print("the 1st ...:", fr2[0:3][1] ) #そのうちの1つめの要素
