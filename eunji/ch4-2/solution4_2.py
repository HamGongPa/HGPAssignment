# 1. 모스부호(1)

def solution(letter):
    answer = '' # 빈 문자열 선언
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    letter = letter.split() # 매개변수 letter를 split으로 자르기
    
    for i in letter:
        answer += morse[i] # morse에 해당되는 매개변수를 빈 문자열에 추가
        
    return answer





# 2. 연습문제 4번 다시 풀고 주석으로 설명

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게베기", "아주세게베기"]
}

for key in character:    # character를 반복시킵니다 / 결과 값: name level items skill
    if type(character[key]) is list:    # character[key] 의 type 이 list 일 경우 이중 리스트를 해제 시키기 위해 반복시킵니다.  
        for list_key in character[key]:    # 결과 값: 베기 세게베기 아주세게베기
            print(f"{key} : {list_key}")    # key : list_key를 출력합니다.
    elif type(character[key]) is dict:    # character[key] 의 type 이 dict 일 경우 이중 딕셔너리를 해제 시키기 위해 반복시킵니다. 
        for dic_key in character[key]:    # 결과 값: sword armor
            print(f"{dic_key} : {character[key][dic_key]}")    # dic_key : character[key][dic_key]를 출력합니다. (character[key] = {'sword':'불꽃의 검', 'armor':'풀플레이트'}, character[key][dic_key] = 불꽃의 검, 풀플레이트)
    else:
        print(f"{key} : {character[key]}") # 일반 문자열일때 key : character[key]를 출력합니다. 





# 3. contries 딕셔너리 출력
contries = {
    'kr': '대한민국', 'us': '미국', 'jp': '일본', 'de': '독일', 'sk': '슬로바키아', 'hu': '헝가리', 'no': '노르웨이'
}

for contrie in contries:
    print(f"{contrie} : {contries[contrie]}")





# 4. date, close_price 딕셔너리 형태로 출력

date = ['04/01', '04/02', '04.03', '04/04', '04/05']
close_price = [8000, 11200, 10200, 11100, 13200]

dict_a = {}

for i, j in zip(date, close_price):
    dict_a[i] = j

print(dict_a)
