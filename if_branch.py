
# mood_index = int(input("请输入您的情绪指数(1-100): "))
# if mood_index >= 90:
#     print("今天心情非常好,男朋友可以愉快的打游戏！")
# elif mood_index >= 80:
#     print("今天心情还好，男朋友也打游戏,但是莫嚣张")
# elif mood_index >= 70:
#     print("今天心情normal，男朋友的打游戏,但是请安静点")
# elif mood_index >= 60:
#     print("今天心情及格，男朋友这游戏就打吧。。")
# else:
#     print("想死就去打游戏")




print("-------------------------------------------------------")
# logic operator
mood_index = int(input("请输入您的情绪指数(1-100): "))
at_home = bool(input("是否在家(是/否): "))

if mood_index >= 90 and mood_index <= 100:
    print("今天心情非常好,男朋友可以愉快的打游戏！")
elif mood_index >= 80 and mood_index < 90:
    print("今天心情还好，男朋友也打游戏,但是莫嚣张")
elif mood_index >= 70 and mood_index < 80:
    print("今天心情normal，男朋友的打游戏,但是请安静点")
elif mood_index >= 60 and mood_index < 70:
    print("今天心情及格，男朋友这游戏就打吧。。")
elif at_home == True:
    print("想死就去打游戏")

