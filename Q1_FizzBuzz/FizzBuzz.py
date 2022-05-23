for num in range(1, 101):
    string = ''

    # ここから記述
    
    #あまりによって倍数判定

    #numが3*5の倍数のとき
    if num % (3*5) == 0:
        string = 'FizzBuzz'

    #それ以外でnumが3の倍数のとき
    elif num % 3 == 0:
        string = 'Fizz'

    #さらにそれ以外でnumが5の倍数のとき
    elif num % 5 == 0:

        string = 'Buzz'
    
    #どれでもないとき
    else:
        string = str(num)


    # ここまで記述

    print(string)
