"""
저번에 만든 모평균 추정해서 출력하는 함수 만들어보기를 조금 바꿔서 만들어봤다

표본수에 따라 z 검정, t 검정으로 나눌 필요가 없기 때문에

저번보다 간단한 형태로 가능!

대신 확률을 입력받을 때

0.3 또는 4/5 같은 형식을 편하게 입력할 수 있도록

조금 유연성을 줘봤다

그리고 표본 오차까지 추가해서 출력하는 걸로 수정

"""

def final():
    import math
    n=int(input('표본의 크기를 입력하세요 : '))
    p=input('표집된 표본의 확률을 입력하세요\nex) 295/400, 0.4       : ')
    temp=True
    flag=False
    percent=0
    z=0
    for i in range(len(p)):
        if p[i]=='/':
            percent=int(p[:i])/int(p[i+1:])
            flag=True
            break
    if flag==False:
        percent=float(p)
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
    p_range_a=percent-z*math.sqrt(percent*(1-percent)/n)
    p_range_b=percent+z*math.sqrt(percent*(1-percent)/n)
    p_mistake=math.sqrt(percent*(1-percent)/n)
    print('모비율의 추정 구간은 %.3f 부터 %.3f 이며 신뢰 구간은 %s%%, 오차 구간은 %.3f 입니다.' %(p_range_a,p_range_b,per,p_mistake))
    
final()