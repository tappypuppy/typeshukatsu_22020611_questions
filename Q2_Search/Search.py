def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    #探索する範囲の一番左のインデックスをleft_idx
    #　　　　　　　一番右のインデックスをright_idxとする

    #初期値
    left_idx = 0
    right_idx = len(sorted_array) - 1


    while left_idx <= right_idx:

        #真ん中のインデックスと値
        middle_idx = (left_idx + right_idx) // 2
        middle_num = sorted_array[middle_idx]

        #探索範囲の更新
        if target_number < middle_num:
            right_idx = middle_idx - 1
            continue

        if target_number > middle_num:
            left_idx = middle_idx + 1
            continue

        #target_number == middle_num なので、インデックスを返す
        return middle_idx


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
