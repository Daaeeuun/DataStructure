def name():

    # s = input("Y / N : ")
    # if s=="Y":
    #     print("반갑습니다, ", user_name, "님.")
    # else:
    #     print("이름을 다시 한 번 입력해주세요.")
    #     name()
    

    while True:
        user_name = input("이름을 입력하세요: ")
        print("당신의 이름은 ", user_name,"이 맞습니까?")
        is_correct = input("Y / N : ")
        if is_correct == "Y" or is_correct == "y":
            print("반갑습니다, ", user_name, "님.")
            break
        else:
            print("이름을 다시 한 번 입력해주세요.")





map = {1:'피겨', 2:'야구', 3:'축구'}    #키:값
print(map)
print('나는 어떤 종목 선수게?', map[3])
map[4] = '테니스'
map.update({5: '핸드볼', 6:'태권도'})
print(map)
print('3: ', 3 in map)   #키
print(map.keys())
print(map.values())

name()