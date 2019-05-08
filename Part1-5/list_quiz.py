colors = ["purple", "orange", "green"]

guess = input("リストの中身は何色でしょう?(英語半角小文字で入力してください):")

if guess in colors:
    print("正解!")
else:
    print("残念!また挑戦してね")