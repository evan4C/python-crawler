# -*- coding: utf-8 -*-

## Pythonによるプログラミング

## #はコメントを表します

#---------------------------------------------------------------
# 分析ツールとしてPythonを使う場合は、作法を気にしすぎる必要はないでしょう。  
# 作法に沿っていなくても、プログラムの実行は可能です。
#---------------------------------------------------------------

#作法に沿っていないが実行できる例

A = 123.45       #数値を格納
B = "apple"      #文字列を格納

import sys      #拡張ライブラリsysの読み込み
C = sys.version  #sysが持つ.versionという機能(Pythonのバージョンを取得)

def test(a):    #自作の関数の定義（引数としてaを受け取る）
    print("これは ", a, " です")   #aの前後に文字列を加えて表示する
    
test(A)          #自作の関数を実行
test(B)
test(C)
