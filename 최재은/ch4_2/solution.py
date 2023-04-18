#모스 부호
def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    letter_new = letter.split()
    for i in letter_new:
        answer += morse[i]
    return answer


#연습 문제 4번
character = {
    'name' : '기사',
    'level' : 12,
    'items' : {
        'sword' : '불꽃의 검',
        'armor' : '플레이트'
    },
    'skill' : ['베기', '세게 베기', '아주 세게 베기']
}

for key in character:
    if type(character[key]) is dict: #character[key] 타입이 딕셔너리일 경우
        for key_dic in character[key]: #charcter[key] 이중 딕셔너리 안의 요소를 꺼내기 위해서 반복
            print(key_dic, ':', character[key][key_dic]) # (이중 딕셔너리 안의) key : key_dic 값의 형태로 프린트
    elif type(character[key]) is list: #character[key] 타입이 리스트일 경우
        for key_list in character[key]: #리스트 안의 요소를 꺼내기 위해서 반복
            print(key, ':', key_list) #key : key_list(리스트 안의 요소들)의 형태로 프린트
    else: #나머지일 경우
        print(key, ':'. character[key]) #key : character[key] 형태로 프린트


#countries를 key-value 형태로 출력
countries = {"kr": "대한민국", "us": "미국", "jp": "일본", "de":"독일", "sk":"슬로바키아", "hu":"헝가리", "no":"노르웨이"}

for key in countries:
    print(key, ":", countries[key])


#두 개의 리스트를 딕셔너리 형태로 출력
date = ['04/01', '04/02', '04/03', '04/04', '04/05']
close_price = [8000, 11200, 10200, 11100, 13200]
        
dictionary = dict(zip(date, close_price))
print(dictionary)
        