meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ" : "шутка",
            "ТРЕШ" :"творящийся ужас",
            "КРИПОВЫЙ": "страшный, пугающий",
            "АГРИТЬСЯ" : "злиться",
            "ЖИЗА": "жизненная ситуация"
            }
word = input("Введите непонятное слово (большими буквами!): ").upper()
if word in meme_dict.keys():
   print(meme_dict[word])
else:
    print("Такого слова нет в нашем словаре")
