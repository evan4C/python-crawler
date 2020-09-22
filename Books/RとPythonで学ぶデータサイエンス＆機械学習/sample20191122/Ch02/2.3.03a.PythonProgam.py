# -*- coding: utf-8 -*-

#上記は、このスクリプトの文字コードがUTF-8であることを示す記述
#プログラムの実行上は、記述の必要はありません

## Pythonによるプログラミング

## #はコメントを表します

#---------------------------------------------------------------
### プログラムの作法  

# Pythonは汎用のプログラミング言語です。  
# このため、一定の作法に沿った記述が求められます。
#---------------------------------------------------------------

#一般的な記法
#ただしこのような順番で書かなくても実行は可能（作法の問題）

#宣言
import sys      #拡張ライブラリsysの読み込み

#関数やクラスなどの定義
def test(a):    #自作の関数の定義（引数としてaを受け取る）
    print("これは ", a, " です")   #aの前後に文字列を加えて表示する

#処理の本体
if __name__ == '__main__':  #メインのプログラムであるときに以下を実行する
    A = 123.45       #数値を格納
    B = "apple"      #文字列を格納
    C = sys.version  #sysが持つ.versionという機能(Pythonのバージョンを取得)
    test(A)          #自作の関数を実行
    test(B)
    test(C)
