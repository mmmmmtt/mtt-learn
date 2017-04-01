temp = input("猜一下我心里想的什么数字:")
guess = int(temp)
i = 0
while guess != 8 and i < 2:
    temp = input("猜错了，请重新猜一个:")
    guess = int(temp)
    if guess == 8:
        print ("被你猜中了") 
    else:
        if guess > 8:
            print("很接近了哦")
        else:
            print("很接近了哦")
    i = i + 1
print("嗨呀，不玩了呢。")
