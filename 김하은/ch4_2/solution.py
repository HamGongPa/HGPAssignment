#문제1
def solution1(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    answer = ''
    for i in letter.split(' '):
        answer += morse[i]
    return answer

#문제2
character = {
    “name” : “기사“,
    “level“ : 12,
    “items“ : {
        “sword“ : “불꽃의 검“,
        “armor“ : “플레이트“
    },
    “skill“ : [“베기“, “세게 베기“, “아주 세게 베기“]
}

for key in character:
    if type(character[key]) is dict: #dictionary 값이 dict 타입일 경우
        for key2 in character[key]: 
            print(f"{key2} : {character[key][key2]}") #dict 타입을 가진 값들 출력
    elif type(character[key]) is list: #하지만 dictionary 값이 list일 경우
        for list_value in character[key]: 
            print(f"{key} : {list_value}") # list 값들 출력
    else:
        print(f"{key} : {character[key]}") # 그 외 나머지 일반 문자열 출력


#문제3
countries = {"kr": "대한민국", "us": "미국", "jp": "일본", "de": "독일", "sk": "슬로바키아", "hu": "헝가리", "no": "노르웨이" }

for country in countries:
    print(f"{country} : {countries[country]}")

#문제4
date = ['04/01', '04/02', '04/03', '04/04', '04/05']
close_price = [8000, 11200, 10200, 11100, 13200]
newdict = dict(zip(date, close_price))
print(newdict)
