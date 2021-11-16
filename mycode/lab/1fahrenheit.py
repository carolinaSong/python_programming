# 화씨온도 = (9/5)*섭씨온도 + 32

"""
섭씨온도를 입력 받아서 화씨로 변환하기
"""
#섭씨를 화씨로 변환하는 함수
def fah_convert(celsius):
    return((9/5)*float(celsius)) + 32

print("변환하고 싶은 섭씨 온도를 입력하세요~")
user_input = input()
print(type(user_input), user_input)
fah = fah_convert(user_input)

print('섭씨온도:', float(user_input))
#동적 변수와 같이 쓰고 싶을때 앞에 f를 쓰면 지원가능
print(f'섭씨온도: {user_input}')
#print('화씨온도 : {}'.format(fah))
#화씨온도를 소수점 두째짜리까지만 보여주고 싶을때
print('화씨온도 : {0:.2f}'.format(fah))
#소수점을 나타내는 다른 함수
print(f'화씨온도 : {round(fah,2)}')