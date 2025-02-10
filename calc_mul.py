#!/usr/bin/python3

import re
                
def calc(A, B):
    ai = str(A)
    bi = str(B)
    p = re.compile(r'\d+(\.\d+)?')  # 修正: 正規表現を `r""` に変更

    # A, B が整数であるか確認
    if not (ai.isdigit() and bi.isdigit()):  
        return -1

    a = int(ai)  # 文字列から整数に変換
    b = int(bi)

    # 範囲チェック修正 (1 ～ 999 の整数のみ許可)
    if 1 <= a <= 999 and 1 <= b <= 999:
        return a * b
    else:
        return -1
        
                
def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')

        # "end" でループ終了
        if A == 'end' or B == 'end':
            break
        
        print('input A * input B = ', calc(A, B))

if __name__ == '__main__':
    main()
