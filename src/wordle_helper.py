# -*- coding:utf-8 -*-
import json
import math


# 字母数
LETTERS = 5


def get_status(guess, actual):
    """
    根据猜测的单词和实际单词，获取状态码
    :param guess: 猜测的单词
    :param actual: 实际的单词
    :return: 状态码
    """
    status = 0
    base = 1
    for i in range(len(guess)):
        c = guess[i]
        if c == actual[i]:
            status += 2 * base
        elif c in actual:
            status += base
        base *= 3
    return status


def get_socre(status_list):
    """
    根据状态码，获取信息量
    :param status_list:
    :return:
    """
    total = sum(status_list)
    score = 0
    for c in status_list:
        if c > 0:
            p = float(c) / total
            score -= p * math.log(p, 2)
    return score


def transform_status(status_str_list):
    """
    将字符串状态转为三进制状态
    :param status_str_list: 字符串状态
    :return: 三进制状态
    """
    status_list = list()
    for status_str in status_str_list:
        status = 0
        base = 1
        for c in status_str:
            status += int(c) * base
            base *= 3
        status_list.append(status)
    return status_list


def get_possible_words(word_list, guess_list, status_list):
    """
    获取可能的词汇
    :param word_list: 词汇列表
    :param guess_list: 猜测列表
    :param status_list: 状态结果
    :return: 可能的词汇列表
    """
    possible_word_list = list()
    for word in word_list:
        flag = True
        for i in range(len(guess_list)):
            if get_status(guess_list[i], word) != status_list[i]:
                flag = False
                break
        if flag:
            possible_word_list.append(word)
    return possible_word_list


# part1: 过滤词汇，仅执行一次
# word_map = dict()
# with open("en_50k.txt", "r") as f:
#     for line in f:
#         parts = line.strip().split(" ")
#         word = parts[0]
#         freq = int(parts[1])
#         available = True
#         if len(word) != LETTERS:
#             available = False
#         else:
#             for c in word:
#                 if c < 'a' or c > 'z':
#                     available = False
#                     break
#         if available:
#             word_map[word] = freq
# with open("words%d.txt" % LETTERS, "w") as f:
#     f.write(json.dumps(word_map))

# part2: 分析词汇
def main(guess_list, status_str_list):
    """
    猜词主函数
    :param guess_list: 猜词列表
    :param status_str_list: 猜词结果，每次以一个长度为5的纯数字字符串表示（0表示不存在，1表示存在但位置错，2表示位置对）
    :return:
    """
    status_list = transform_status(status_str_list)
    right_word_score = dict()
    all_word_score = dict()
    with open("words%d.txt" % LETTERS, "r") as f:
        word_map = json.loads(f.read())
        all_word_list = word_map.keys()
        possible_word_list = get_possible_words(word_map.keys(), guess_list, status_list)
        word_count = len(all_word_list)
        print("Calculating ...")
        for i in range(word_count):
            guess = all_word_list[i]
            status_list = [0] * (3 ** LETTERS)
            for actual in possible_word_list:
                # 给对应的状态码，添加freq
                freq = word_map[actual]
                status = get_status(guess, actual)
                status_list[status] += freq
            if guess in possible_word_list:
                right_word_score[guess] = [get_socre(status_list), word_map[guess]]
            all_word_score[guess] = get_socre(status_list)

        # 按信息量排序
        candidates = sorted(right_word_score.items(), key=lambda (k, v): v[1], reverse=True)[:10]
        candidates2 = sorted(all_word_score.items(), key=lambda (k, v): v, reverse=True)[:10]
        print("====== POSSIBLE ======")
        for item in candidates[:3]:
            print("Word = %s, Freq = %d, Score = %.2f" % (item[0], item[1][1], item[1][0]))
        print("====== BEST GUESS ======")
        for item in candidates2[:3]:
            print("Word = %s, Score = %.2f" % (item[0], item[1]))
        print("====== RESULT ======")
        if len(candidates) < 10:
            print("I would like to guess '%s'" % candidates[0][0])
        else:
            print("Still no idea, try '%s'" % candidates2[0][0])


if __name__ == "__main__":
    guess_list = list()
    status_str_list = list()
    FIRST_GUESS = ["", "i", "to", "ton", "tale", "tears", "tories", "cartons"]
    print("====== BEGIN ======")
    if LETTERS <= 7:
        print("Firstly, I'll try '%s'" % FIRST_GUESS[LETTERS])
    count = 0
    while True:
        if LETTERS <= 7 or count != 0:
            words = raw_input("=> Input your actual guess (%d letters, for example: %s): " % (LETTERS, 'a' * LETTERS))
            status_str = raw_input("=> Input your result (0-gray, 1-yellow, 2-green, for example: %s): " % ('0' * LETTERS,))
            if "0" not in status_str and "1" not in status_str:
                print("Success, total times = %d" % (count + 1, ))
                break
            guess_list.append(words)
            status_str_list.append(status_str)
        main(guess_list, status_str_list)
        count += 1

