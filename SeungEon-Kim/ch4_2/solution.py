# 1. 모스부호(1)
def solution1(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    return ''.join(morse[i] for i in letter.split(' ')) 
    # 여기서 i는 letter의 모스부호를 공백을 기준으로 스플릿한 값이다. 
    # i를 morse의 키 값으로 사용하여 morse의 value 값에 접근하고 그 값은 문자열 형태이므로 join 시켜주면 끝!

# 2. 연습문제 4번
def solution2():
    character = {
        'name' : '기사',
        'level' : '12',
        'items' : {
            'sword' : '불꽃의 검',
            'armor' : '플레이트',
        },
        'skill' : ['베기', '세게 베기', '아주 세게 베기']
    }

    for key in character:   # 여기서 변수 key는 character라는 딕셔너리의 키 값을 의미한다.
        if type(character[key]) is dict:    # 만약 위 딕셔너리의 value 값이 dict 타입이라면,
            for key_d in character[key]:    # dict 타입을 가진 키, 밸류 원소 출력. # (sword, armor)
                print(key_d, ":", character[key][key_d])
        elif type(character[key]) is list:  # 만약 원소가 list 타입이라면,
            for list_s in character[key]:   # list 타입 원소 출력. # (skill 3가지)
                print(key, ":", list_s)
        else:                               # 나머지(문자열 등) 타입
            print(key, ":", character[key]) # (name, level)

# 3. Countries
def solution3():
    countries = {"kr" : "대한민국", "us" : "미국", "jp" : "일본", "de" : "독일", "sk" : "슬로바키아", "hu" : "헝가리", "no" : "노르웨이"}
    for key in countries:
        print(key, ":", countries[key])

# 4. Date and Price
def solution4():
    date = ['04/01', '04/02', '04/03', '04/04', '04/05']
    close_price = [8000, 11200, 10200, 11100, 13200]

    dictionary = dict(zip(date, close_price)) # 파이썬의 내장함수인 zip()함수를 사용하여 iterable하고 길이가 같은 두 자료형을 하나로 묶어 준 후, 
    print(dictionary)                         # dict 타입으로 변환하였다.
