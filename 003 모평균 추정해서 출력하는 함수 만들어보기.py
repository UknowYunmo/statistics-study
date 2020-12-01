"""
정리 :

모평균 u를 추정할 때

체크 리스트

1. 모분산을 아는가? -> z 검정
2. 모분산을 모르는가?
2-1 표본의 크기가 30보다 작은 경우 -> t 검정
2-2 표본의 크기가 30보다 큰 경우 -> z 검정

데이터를 입력받아서 모평균을 출력하는 함수를 만들어보자!

대신 t 검정의 경우는 신뢰도 뿐만 아니라 자유도에 따라서도 t 값이 변하기 때문에

변수가 너무 다양해서 미리 입력시켜두지 않았으니

t값은 스스로 표에서 찾아서 입력해야 한다는 한계점이 있다..

https://www.geogebra.org/m/Mmf3AX7y --> t 값 편하게 찾는 웹사이트 

"""
import math
flag='temp'
temp=True
std=0
n=0
z=0
sam_std=0
mo=False
def ask():
    global flag
    global std
    global n
    global mo
    while(True):
        n=int(input('표본의 크기를 입력하세요 : '))
        ans=input('모집단의 분산이나 표준 편차를 알고 있나요?\n맞으면 o 모르면 x를 입력 : ')
        if ans=='o':
            mo=True
            flag='Z'
            print('---z검정 실시---')
            std=float(input('모집단의 표준 편차를 입력하세요\n표준 편차는 분산의 제곱근입니다 '))
            break
        elif ans=='x':
            if n>=30:
                flag='Z'
                print('---z검정 실시---')
                break
            else:
                print('---t검정 실시---')
                flag='T'
                break
        else:print('-----다시 입력하세요-----')
def z_case():
    global n
    global temp
    global z
    global mo
    global std
    while(temp==True):
        per=int(input('몇 %의 신뢰구간? (90, 95, 99만 가능합니다) : ' ))
        if per==90:
            z=1.645
            temp=False
        elif per==95:
            z=1.96
            temp=False
        elif per==99:
            z=2.576
            temp=False
        else:
            print('-----다시 입력하세요-----')
    if mo==False:
        std=float(input('표본의 표준 편차를 입력하세요\n표준 편차는 분산의 제곱근입니다 '))
    sam_mean=float(input('표본의 평균을 입력하세요 '))
    u_range_A=sam_mean-z*std/math.sqrt(n)
    u_range_B=sam_mean+z*std/math.sqrt(n)
    print('모평균의 추정 구간은 %.3f 부터 %.3f 이며 신뢰 구간은 %s%%입니다.' %(u_range_A,u_range_B,per))
    
def t_case():
    global mo_std
    global n
    global sam_std
    per=input('몇 %의 신뢰구간? : ')
    f=float(input('신뢰구간에 따른 t 값을 입력하세요\n자유도를 표본의 수 -1로 하여 표에서 직접 찾아 입력해주세요 '))
    sam_std=float(input('표본의 표준 편차를 입력하세요\n표준 편차는 분산의 제곱근입니다 '))
    sam_mean=float(input('표본의 평균을 입력하세요 '))
    u_range_A=sam_mean-f*sam_std/math.sqrt(n)
    u_range_B=sam_mean+f*sam_std/math.sqrt(n)
    print('모평균의 추정 구간은 %.3f 부터 %.3f 이며 신뢰 구간은 %s%%입니다.' %(u_range_A,u_range_B,per))

def final():
    global flag
    ask()
    if flag=='Z':
        z_case()
    elif flag=='T':
        t_case()
    else:
        print('첨부터 다시 입력 해주세여')
        print(flag)

final()
    

