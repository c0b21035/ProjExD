import random
import time

num_of_alphabet = 26  
num_of_all_chars = 10 
num_of_abs_chars = 2  
num_of_trials = 2 

def shutudai(alphabet):
    
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字：", end="")
    for c in sorted(all_chars): 
        print(c, end=" ")
    print()


    abs_chars = random.sample(all_chars, num_of_abs_chars)
    print("表示文字：", end="")
    for c in all_chars: 
        if c not in abs_chars: 
            print(c, end=" ")
    print()
    return abs_chars


def kaito(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num != num_of_abs_chars:
        print("不正解です．")
    else:
        print("正解です.では.具体的に欠損文字を1つずつ入力してください.")
        for i in range(num):
            c = input(f"{i+1}文字目を入力してください：")
            if c not in seikai:
                print("不正解です．またチャレンジしてください．")
                return False
            else:
                seikai.remove(c) # 正解した場合，その文字を正解リストから削除する（重複回答を防ぐため）
        else:
            print("欠損文字も含めて完全正解です！！！")
            return True
    return False


if __name__ == "__main__":
    st = time.time()
    alphabet = [chr(i+65) for i in range(num_of_alphabet)]
    #print(alphabet)
    for _ in range(num_of_trials):
        abs_chars = shutudai(alphabet)  
        ret = kaito(abs_chars)
        if ret:
            break
        else:
            print("-"*20)
    ed = time.time()
    print(f"所要時間：{(ed-st):.2f}秒")



