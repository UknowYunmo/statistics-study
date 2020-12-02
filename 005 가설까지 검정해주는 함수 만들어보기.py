import math
def user():
    say=0
    temp=True
    flag=''
    while(temp==True):
        say=input('어떤 주장을 하고 싶은가요?\n1. ~보다 작다 2. ~와 차이가 있다 3. ~보다 크다     : ')
        if say=='1' or say=='3':
            print()
            print('---단측 검정을 실시합니다---')
            temp=False
        elif say=='2':
            print()
            print('---양측 검정을 실시합니다---')
            temp=False
        else:
            print()
            print('---다시 입력하세요---')
    n=int(input('표본의 크기를 입력하세요 : '))
    if n>=30:
        flag='Z'
        print()
        print('---z검정 통계량을 사용합니다---')
    else:
        print()
        print('---t검정 통계량을 사용합니다---')
        flag='T'
    tong2=tong(flag,temp,say)
    comp=ask(n)
    if say=='1':
        tong2*=-1
    elif say=='2':
        tong2=abs(tong2)
    print('검정 통계량은 : ',tong2, '이고,')
    print('표본에 따른 통계량은 : ',comp, '이기 때문에,')
    if say=='1':
        if comp<=tong2:
            print('와~ 표본의 검정값이 더 작으므로 귀무가설을 기각할 수 있습니다!!')
        else:
            print('표본의 검정값이 더 작지 않으므로 귀무가설을 기각할 수 없습니다 ㅠ')
    elif say=='2':
        if comp>=tong2:
            print('와~ 표본의 검정값이 검정 통계량의 절대값보다 크므로 귀무가설을 기각할 수 있습니다!!')
        else:
            print('표본의 검정값이 검정 통계량의 절대값보다 크지 않으므로 귀무가설을 기각할 수 없습니다 ㅠ')
    elif say=='3':
        if comp>tong2:
            print('와~ 표본의 검정값이 더 크므로 귀무가설을 기각할 수 있습니다!!')
        else:
            print('표본의 검정값이 더 크지 않으므로 귀무가설을 기각할 수 없습니다 ㅠ')
            
def tong(flag,temp,say):
    if flag=='Z' and say=='2':
        while(temp==False):
            per=float(input('몇 %의 유의 확률? (0.1, 0.05, 0.01 만 가능합니다) : ' ))
            if per==0.1:
                z=1.645
                return z
            elif per==0.05:
                z=1.96
                return z
            elif per==0.01:
                z=2.576
                return z
            else:
                print()
                print('-----다시 입력하세요-----')
    elif flag=='Z' and (say=='1' or say=='3') :
        while(temp==False):
            per=float(input('몇 %의 유의 확률? (0.1, 0.05, 0.01 만 가능합니다) : ' ))
            if per==0.1:
                z=1.23
                return z
            elif per==0.05:
                z=1.64
                return z
            elif per==0.01:
                z=2.33
                return z
            else:
                print()
                print('-----다시 입력하세요-----')
    elif flag=='T':
        f=float(input('유의 확률에 따른 t 값을 입력하세요\n자유도를 표본의 수 -1로 하여 표에서 직접 찾아 입력해주세요 : '))
        return f
    else:
        print('tong 함수에서 오류 발생')

def ask(n):
    sam_mean=float(input('표본의 평균을 입력하세요 : '))
    mean=float(input('귀무 가설의 평균을 입력하세요 : '))
    std=float(input('모표준편차 또는 표본표준편차를 입력하세요 \n(둘 다 알고 있을 경우는, 모표준편차를 입력해주세요) : '))
    compare=(sam_mean-mean)/(std/math.sqrt(n))
    return compare
    
user()