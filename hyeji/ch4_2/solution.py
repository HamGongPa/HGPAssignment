# 1. 모스부호(1)
def solution1(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    answer = ''
    for m in letter.split():
        answer += morse[m]
    return answer


# 2. 연습문제 4번 다시 풀이 후 주석 설명
def solution2():
    character = {
        'name' : '기사',
        'level' : '12'
        'items' : {
            'sword' : '불꽃의 검',
            'armor' : '플레이트'
        }
        'skill : ['베기', '세게 베기', '아주 세게 베기']
    }

for key in character:
    if type(character[key]) is dict:    # 만일 key의 type이 dict일 경우 반복문 필요
        for key2 in character[key]:     # 결과 값 : 'sword' 'armor'
            print(f"{key2}" : {character[key][key2]}") #key : key, key2 출력
    elif type(character[key]) is list:  # 만일 key의 type이 list 일 경우 반복문 필요
        for list_value in character[key]: # 결과 값 : '베기' '세게 베기' '아주 세게 베기'
            print(f"{key} : {list_value}")
    else:
        print(f"{key} : {character[key]}") # 일반 문자열일경우 key : character[key] 출력


# 3. countries key-value 출력
def solution3():
        countries = {
            "kr":"대한민국", "us":"미국", "jp":"일본", "de":"독일", "sk":"슬로바키아", "hu":"헝가리", "no":"노르웨이"
        }
    for country in countries:
        print(f"{country} : {countries[country]}")


# 4. date, close_price 딕셔너리 출력
def solution4():
    date = ['04/01', '04/02', '04/03', '04/04', '04/05']
    close_price = [8000, 11200, 10200, 11100, 13200]

dictionary = dict(zip(date, close_price))
print(dictionary)


