#1
row1=c(21,14,6)
row2=c(18,16,8)
row3=c(16,17,15)
row4=c(12,14,21)
row5=c(6,6,10)
data.table=rbind(row1,row2,row3,row4,row5)
chisq.test(data.table)
1. 귀무가설 : 여행 거리와 좌석 등급은 관계가 없다
2. 두 변수 간의 관계를 보고 싶은거니 독립성 검정
3. 자유도 : 2*4=8
4. (합*합)/총합
5. 15.923
6. 15.5보다 크므로 귀무가설을 기각할 수 있다!

#2
row1=c(15,25,10,5)
row2=c(20,40,70,30)
row3=c(10,20,40,55)
row4=c(5,10,20,60)
row5=c(0,5,10,150)
data.table=rbind(row1,row2,row3,row4,row5)
chisq.test(data.table)
1. 255.77>21.03 이므로 귀무가설을 기각할 수 있다!

#3
row1=c(16,40,38,6)
row2=c(8,44,59,39)
data.table=rbind(row1,row2)
chisq.test(data.table)
1. 개인병원과 종합병원의 근무시간은 차이가 없다.
2. (합*합)/총합
3. 22.504
4. 9.488보다 크므로 귀무가설을 기각할 수 있다!
5. 13.277보다 크므로 귀무가설을 기각할 수 있다!

#4
row1=c(20,35,40,35)
row2=c(20,50,70,80)
row3=c(20,50,100,90)
row4=c(20,50,100,90)
data.table=rbind(row1,row2,row3,row4)
chisq.test(data.table)
1. 15.154는 16.918보다 작으므로 귀무가설을 기각할 수 없다 ㅠ
2. 14.683보다 크므로 귀무가설을 기각할 수 있다!

#5
row1=c(47,35,28,53)
row2=c(65,59,55,60)
data.table=rbind(row1,row2)
chisq.test(data.table)
1. 4.01은 13.277보다 작으므로 귀무가설을 기각할 수 없다 ㅠ

#6
row1=c(15,15,10,20)
row2=c(25,25,25,25)
row3=c(25,25,15,15)
row4=c(20,10,5,5)
data.table=rbind(row1,row2,row3,row4)
chisq.test(data.table)
3. 15.703은 16.918보다 작으므로 귀무가설을 기각할 수 없다 ㅠ

#7
row1=c(3413,7164)
row2=c(3302,7057)
row3=c(3505,7488)
row4=c(3537,7758)
row5=c(3595,7697)
row6=c(3613,7847)
data.table=rbind(row1,row2,row3,row4,row5,row6)
chisq.test(data.table)
1. 2.74는 11.07보다 작으므로 귀무가설을 기각할 수 없다 ㅠ

#8
row1=c(41,52,46,61,58)
row2=c(72,75,63,80,65)
data.table=rbind(row1,row2)
chisq.test(data.table)
1. 3은 9.48보다 작으므로 귀무가설을 기각할 수 없다 ㅠ
