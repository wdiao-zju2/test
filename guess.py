import random
import sys
import time

# 参数
try:
    guess_limit = int(sys.argv[1])
except ValueError:
    guess_limit = 4
    print("input argument value is error, default value is 4")
except IndexError:
    guess_limit = 4
    print("input argument value is required, default value is 4")

score = []
cycle = 0
while (True):
    cycle += 1
    answer = random.randint(1, 10)
    is_right = False

    start_time = time.time()
    # 循环体判断
    for i in range(guess_limit):
        try:
            guess = int(input("--> please give a number: "))
        except ValueError:
            print("--> number is required")
            continue
        if (guess == answer):
            is_right = True
            break
        elif (guess > answer):
            print(f"{guess} is too large", end=", ")
        else:
            print(f"{guess} is too small", end=", ")

        if (i < guess_limit - 1):
            print("please go on guessing \n")

    # 处理结果
    if (is_right):
        print("you are right")
    else:
        print(f"your try have been more than {guess_limit} times")

    end_time = time.time()
    used_time = round(end_time - start_time, 2)
    print(f"\n~~~ the total used time is {used_time} second ~~~")

    # 保存战绩
    score.append((cycle, is_right, used_time))
    best_score = min(score, key=lambda x: x[2] if x[1] else 9999)
    print("\n=========战绩=========")
    for _cycle, _is_right, _used_time in score:
        label = "胜利" if (_is_right) else "失败"
        best_label = "<--" if _cycle == best_score[0] else ""
        print(f"{_cycle}轮, {label}, {_used_time}s {best_label}")
    print("====================== \n")

    # 结束判断
    con = input("if go on, please input 'y', else please input any key: ")
    if (con != "y"):
        print("\n~~~ game is over ~~~")
        break
    else:
        print()


# answer = random.randint(1, 10)
# guess_limit = 3  # permitted max guess number of times
# guess_count = 0  # completed guessed number of times


# while True:
#     guess = int(input("--> please guess a number: "))
#     if guess == answer:
#         print("you are right, game is over")
#         break
#     elif guess < answer:
#         print(f"{guess} is too small", end=", ")
#     else:
#         print(f"{guess} is too large", end=", ")

#     guess_count += 1
#     if (guess_count == guess_limit):
#         print("you used up all number if times, game is over")
#         break
#     else:
#         print("please go on \n")
