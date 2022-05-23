from distutils.util import change_root


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    left_idx = 0
    right_idx = len(array)-1

    #値を交換した回数
    change_count= 0

    #左から順にpivot以上の値を探していく。
    while left_idx < right_idx:
        if array[left_idx] >= pivot:

            #交換先を見つけるために、右から順にpivot未満の値を探す
            while left_idx < right_idx:

                #見つけたら、値を交換し、交換した回数+1する
                #そして、while文を抜け、新たに左からpivot以上の値を探す。
                if array[right_idx] < pivot:
                    tmp_value = array[left_idx]
                    array[left_idx] = array[right_idx]
                    array[right_idx] = tmp_value
                    change_count += 1
                    break                
                

                #右と左のインデックスが隣接したら、これ以上探せないので終了
                if left_idx + 1 == right_idx:
                    break
                else:
                    right_idx -=1
        
        #右と左のインデックスが隣接したら終了
        if right_idx == left_idx+1:
            break
        
        left_idx += 1

    #ここまでで、交換作業終了

    #pivot未満とpivot以上をleft,rightに分ける
    left = []
    right = []


    #交換回数が0の場合

    #pivotをleft、それ以外をrightにし、それぞれsortにかける
    if change_count == 0:
        left = array[:1]
        right = array[1:]
        left = sort(left)
        right = sort(right)
        return left+right

    
    #交換回数が1回以上の場合
    #array[left_idx]によってpivot以上と未満にグループ分け
    if array[left_idx] < pivot:
        left = array[:left_idx+1]
        right = array[right_idx:]
    else:
        left = array[:left_idx]
        right = array[right_idx-1:]

    #listが空でないとき、sortにかける
    if left:
        left = sort(left)
    if right:
        right = sort(right)


    return left + right


    # ここまで記述

if __name__ == '__main__':
    main()
