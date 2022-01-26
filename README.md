# wordle-helper
A bot for wordle

# how to start
``` bash
cd src && python wordle_helper.py
```

# run result example
```
====== BEGIN ======
Firstly, I'll try 'tears'
=> Input your actual guess (5 letters, for example: aaaaa): tears
=> Input your result (0-gray, 1-yellow, 2-green, for example: 00000): 00200
Calculating ...
====== POSSIBLE ======
Word = again, Freq = 590019, Score = 1.82
Word = black, Freq = 123718, Score = 1.71
Word = coach, Freq = 32471, Score = 1.58
====== BEST GUESS ======
Word = colin, Score = 2.28
Word = cling, Score = 2.25
Word = clink, Score = 2.23
====== RESULT ======
Still no idea, try 'colin'
=> Input your actual guess (5 letters, for example: aaaaa): colin
=> Input your result (0-gray, 1-yellow, 2-green, for example: 00000): 10000
Calculating ...
====== POSSIBLE ======
Word = whack, Freq = 4297, Score = 0.97
Word = quack, Freq = 2451, Score = 0.93
Word = aback, Freq = 341, Score = 0.28
====== BEST GUESS ======
Word = haber, Score = 1.18
Word = haben, Score = 1.18
Word = pubic, Score = 1.18
====== RESULT ======
I would like to guess 'whack'
=> Input your actual guess (5 letters, for example: aaaaa): whack
=> Input your result (0-gray, 1-yellow, 2-green, for example: 00000): 22222
Success, total times = 3
```

# 原理
基于已知词频表[https://github.com/dwyl/english-words]构建先验概率，并计算所有词汇的信息熵，选择最大的进行猜测。

当候选列表小于10时，优先猜测词频最高的单词。


