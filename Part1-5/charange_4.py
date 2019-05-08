me = {
    "身長": 162,
    "体重": 56,
    "好きな色": "Blue",
}

my_key = input("キーを入力してください(身長,体重,好きな色):")

if my_key in me:
    print(me[my_key])
else:
    print("そのキーはありません!")