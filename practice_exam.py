# Quiz1) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : 사당 신도림 인천공항 순서대로 입력
# 출력 문장 : XX행 열차가 들어오고 있습니다

# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")
print("(Quiz1)")
station = ['사당', '신도림', '인천공항']
# print(station)
# print(len(station))
# print(station[0])
for i in station:
 print(i + "행 열차가 들어오고 있습니다.")

# Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# 출력문 예제 : 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.

print("(Quiz2)")
import random

random_List = list(range(4,29))
random.shuffle(random_List)
print(random_List)

offline = random.choice(random_List)
random_List.remove(offline)
online = random.sample(random_List,3)
online.sort()
print(offline)
print(online)
print("오프라인 스터디 모임 날짜는 매월 {0}일로 선정되었습니다.".format(offline))
# print("오프라인 스터디 모임 날짜는 매월", offline, "일로 선정되었습니다.")
for i in online:
    print("온라인 스터디 모임 날짜는 매월",i,"일로 선정되었습니다.")

# Quiz3) 사이트 별로 비밀번호를 만들어주는프로그램을 작성하시오.
# 예) htttp://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자갯수 + 글자 내'e'의 갯수 +'!'로 구성

# 예) 생성된 비밀번호 : nav5!

print("(Quiz3)")
site = []
site.insert(0,"http://naver.com")
site.insert(1,"http://daum.net")
site.insert(2, "http://google.com")
site.insert(3, "http://youtube.com")

# find = site[0].find("/")
# find = site[0].find("/", find+1)
# print(find)
# print(site)
find_s = []
find_dot = []
for i in site:
    find = i.find("/")
    find_s.insert(site.index(i),i.find("/",find+1)) #마지막으로 /가 있는 인덱스
    find_dot.insert(site.index(i),i.find(".")) # .이 있는 인덱스
# print(find_s) # /가 있는 인덱스들의 모임
# print(find_dot) # .가 있는 인덱스들의 모임
find_dot = []
for i in site:
    find_dot.insert(site.index(i),i.find("."))
# print(find_dot) 

for i in site: # 처음 작성한 답
    a = find_s[site.index(i)] # a는 find_s에 있는 값들 (site의 순서대로) 
    b = find_dot[site.index(i)] # b는 find_dot에 있는 값들 (site의 순서대로)
    c = b-a-1
    #print(i[a+1:a+4] + str(c) + "!")

for i in site: # 새로 작성한 답
    i = i.replace("http://","")
    dot = i.find(".")
    string = i[:3]
    number = str(dot)
    pw = string + number + "!"
    print("{0}의 비밀번호는 {1}입니다.".format(i[:dot],pw))

# Quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 되빈다.
# 추천 프로그램을 작성하시오.

# 조건1. 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건2. 댓글 내용과 상관없이 무작위로 추첨하되 중복은 불가
# 조건3. random 모듈의 shuffle과 sample을활용

# 출력예제 ----- 당청자 발표 ---- 치킨 당첨자 :1 커피 당첨자: [2,3,4] --- 축하합니다.----

print("(Quiz4)") 

import random
user = list(range(1,21)) 
#random.shuffle(user)
random.shuffle(user)
print(user, type(user))
    
chicken = random.choice(user)
user.remove(chicken)

random.shuffle(user)
coffee = random.sample(user,3)
coffee.sort()
print("""--당첨자 발표--
치킨 당첨자 : {0}
커피 당첨자 : {1}
--축하합니다.--""".format(chicken,coffee))

# Quiz5) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1. 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2. 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [O] 1번째 손님(소요시간 : 15분)
# [] 2번째 손님(소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [] 50번째 손님 (소요시간 : 16분)

# 총 탑승승객 : 2분

print("(Quiz5)")

import random
def random_L(size):
    result = []

    for i in range(size):
        result.append(random.randint(5,50))
    return result
result = random_L(50)
print(result, len(result))

person = 0
for customer in result :
    if 5<= customer <= 15 in result:
       person += 1
       print("[O] {0}번째 손님 (소요시간 : {1}분".format(result.index(customer)+1,customer))
    else :
        print("[ ]{0}번째 손님 (소요시간 : {1}분".format(result.index(customer)+1,customer))
print("총 탑승승객 : {0}분".format(person))


# Quiz6) 표준 체중을 구하는 프로그램을 작성하시오.
# 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m)*키(m)*22
# 여자 : 키(m)*키(m)*21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# *함수명 : std_weight
# *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

#(출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

print("(Quiz6)")
def std_weight(height, gender):
    if gender == "남자":
        result = height*height*22
        return round(result, 2)
    else :
        result = height*height*21
        return round(result,2)

height = 175
gender = "남자"
weight = std_weight(height/100, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(175, "남자",std_weight(1.75,"남자")))
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(160, "여자",std_weight(1.60, "여자")))

# Quiz7)  당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# -X주차 주간보고-
# 부서 :
# 이름 :
# 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그랢을 작성하시오.
# 조건 : 파일명은 '1주차.txt','2주차.txt',...와 같이 만듭니다.

print("(Quiz7)")
for i in range(1,51):
    with open("{0}주차.txt".format(i), "w", encoding="utf8" ) as new_week_file:
        new_week_file.write("-{0}주차 주간보고-\n부서 : \n이름 : \n요약 :".format(i))