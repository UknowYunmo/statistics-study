"""
1. 코끼리의 체중에 대한 모표준편차가 15 파운드라고 알려져 있다.
임의로 선택된 코끼리 50마리의 체중을 측정한 결과
표본평균은 244 파운드이고, 표본표준편차는 11파운드이다.
모평균에 대한 95% 신뢰구간을 구하라.
"""
import math
z=1.96
mo_std=15
n=50
sam_mean=244
sam_std=11

u_range1=sam_mean-z*mo_std/math.sqrt(n)
u_range2=sam_mean+z*mo_std/math.sqrt(n)
print(u_range1)
print(u_range2)

#%%
"""
2. 캘리포니아의 성인 506명을 대상으로 캘리포니아가 직면한 가장 큰 문제점을 조사한 결과,
그 중 400명이 ‘교육’이라고 답했다.
실제 교육이 가장 큰 문제라고 생각하는 캘리포니아의 성인의 비율에 관심이 있다.
(1) 모비율의 추정치와 표준오차를 구하라.
(2) 모비율 p에 대한 90% 신뢰구간을 구하라.
"""
import math
n=506
p=400/506
print(p)
print(math.sqrt(p*(1-p)/n))
z=1.645
mo_p_range1=p-z*math.sqrt(p*(1-p)/n)
mo_p_range2=p+z*math.sqrt(p*(1-p)/n)
print(mo_p_range1)
print(mo_p_range2)

#%%
"""
3. 유럽 남성의 평균 체중에 대한 95% 신뢰구간을 구하기 위하여
스웨덴 남성 48명을 대상으로 조사한 결과,표본평균은 71kg, 표본표준편차는 2.8kg이었다.
유럽 남성의 체중은 정규분포를 따른다고 가정하자.
(1) 모평균에 대한 95% 신뢰구간을 구하라.
(2) 모분산이 9kg이라고 알려져 있다면, 모평균에 대한 95% 신뢰구간은 어떻게 달라지는가?
"""
import math
n=48
sam_mean=71
sam_std=2.8
z=1.96
u_range1=sam_mean-z*sam_std/math.sqrt(n)
u_range2=sam_mean+z*sam_std/math.sqrt(n)
print(u_range1)
print(u_range2)
mo_std=3
u_range1a=sam_mean-z*mo_std/math.sqrt(n)
u_range2b=sam_mean+z*mo_std/math.sqrt(n)
print(u_range1a)
print(u_range2b)

#%%
"""
4. 한 제약회사에서 만드는 정신 안정제의 약효가 지속되는 시간은 정규분포를 따른다.
9명의 환자에게 이 약을 투여하고 약효가 지속되는 시간을 측정한 결과는 다음과 같다.
"""
list=[ 2.7, 2.8, 3.0, 2.3, 2.3 , 2.2 , 2.8 , 2.1 , 2.4]
# (1) 모평균의 추정치와 표준오차를 구하라
import numpy as np
print('표본평균(추정치) :',np.mean(list))
print('표본분산 :',np.var(list))
print('표준편차 :',np.std(list))
print('표준오차 :',np.std(list)/math.sqrt(len(list)))
# (2) 모평균에 대한 95% 신뢰구간을 구하라.
t=2.306
print(np.mean(list)-t*np.std(list)/math.sqrt(len(list)))
print(np.mean(list)+t*np.std(list)/math.sqrt(len(list)))
print('-------------')
# (6-5) 연습문제 6.4에서 표본평균과 표본표준편차는 동일하고, 표본의 크기가 49명으로 늘어난다면,
# 모평균에 대한 95% 신뢰구간은 어떻게 달라지는가?
z=1.96
print(np.mean(list)-z*np.std(list)/math.sqrt(49))
print(np.mean(list)+z*np.std(list)/math.sqrt(49))
print('-----------')
# (6-6) 연습문제 6.4에서 모분산이 0.3시간으로 알려져 있다면, 모평균에 대한 95% 신뢰구간은 어떻게 달라지는가?

print(np.mean(list)-t*math.sqrt(0.3)/math.sqrt(len(list)))
print(np.mean(list)+t*math.sqrt(0.3)/math.sqrt(len(list)))

#%%
"""
7. 마케팅 회사에서 주부 200명을 대상으로 조사한 결과,
그 중 120명이 물건을 구매할 때 제조회사를 가장 중요시 여긴다고 답했다.
실제 물건을 구매할 때 제조회사를 가장 중요시 여기는 주부의 비율에 관심이 있다.
모비율에 대한 95% 신뢰구간을 구하라.
"""
n=200
p=120/200
z=1.96

print(p-z*math.sqrt(p*(1-p)/n))
print(p+z*math.sqrt(p*(1-p)/n))

#%%
"""
8. 동일 브랜드에서 판매되고 있는 여행용 가방 16개의 무게를 측정하였다.
여행용 가방의 무게는 정규분포를 따른다고 가정하자.
측정된 여행용 가방 무게의 표본평균은 2kg이고, 표본표준편차는 0.12kg이다.
모표준편차는 0.1kg으로 알려져 있다.
모평균에 대한 90% 신뢰구간을 구하라.
"""

n=16
sam_mean=2
sam_std=0.12
mo_std=0.1
z=1.645

print(sam_mean-z*sam_std/math.sqrt(n))
print(sam_mean+z*sam_std/math.sqrt(n))

#%%
"""
9.부산대학교 학생 200명을 대상으로 조사한 결과에 따르면
일주일 동안 영어 공부를 하는 시간의 표본평균은 8.2시간, 표본표준편차는 2.2시간이었다.
모표준편차는 알려져 있지않으며, 모집단은 정규분포를 따른다고 가정하자.
모평균에 대한 90% 신뢰구간을 구하라
"""

n=200
sam_mean=8.2
sam_std=2.2
z=1.645

print(sam_mean-z*sam_std/math.sqrt(n))
print(sam_mean+z*sam_std/math.sqrt(n))

#%%
"""
10. 두발 자전거를 배운 어린이 14명을 대상으로 두발 자전거를 배우기까지 걸린 기간을 조사하였다.
조사 결과, 표본평균은 6개월이고, 표본표준편차는 3개월이었다.
모집단은 정규분포를 따른다고 가정하자.
"""
n=14
sam_mean=6
sam_std=3
# (1) 90% 신뢰구간 모평균 추정
t=1.77
print(sam_mean-t*sam_std/math.sqrt(n))
print(sam_mean+t*sam_std/math.sqrt(n))
print('----------------------')
# (2) 95% 신뢰구간 모평균 추정
t=2.16
print(sam_mean-t*sam_std/math.sqrt(n))
print(sam_mean+t*sam_std/math.sqrt(n))
print('----------------------')
# (3) 99% 신뢰구간 모평균 추정
t=3.012
print(sam_mean-t*sam_std/math.sqrt(n))
print(sam_mean+t*sam_std/math.sqrt(n))
