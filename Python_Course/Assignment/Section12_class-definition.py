class Human:
    def __init__(self, age, name, gender):
        self.__age = age
        self.__name = name
        self.__gender = gender
    
    #プロパティを作成(値の更新の場面がないため、セッターは省略)
    @property
    def call_age(self):
        return self.__age
    
    @property
    def call_name(self):
        return self.__name
    
    @property
    def call_gender(self):
        return self.__gender
        
members = []

#入力を受けて仮に3人分のリストを作成
for i in range(1,4):
    name_input = input(f"{i}番目人の名前を入れてください。")
    age_input = float(input(f"{i}番目人の年齢を入れてください。"))
    gender_input = input(f"{i}番目人の性別を入れてください。")
    members.append(Human(age_input, name_input, gender_input))

#リストをageが高い順に並び替える
members.sort(key = lambda item : item.call_age, reverse = True)

for member in members:
    print(f"{member.call_name}さんは{member.call_age}歳で性別が{member.call_gender}です。")