# 9-1 
wt = c(43.5,39.4,41.3,46.0,38.2,47.0,40.5,38.9,46.3,44.2,51.2,40.9,37.9,45.0,48.6)
feed = c(rep("A",5), rep("B",5), rep("C",5))
rat = data.frame(wt,feed)
rat
results = aov(wt ~ feed, data=rat)
anova(results)

# (1) - 귀무가설 : 음식에 따른 쥐의 무게의 유미의한 차이는 없다, 대립 가설 : 유의미한 차이가 있다
# (2) - 분자 자유도 : 2 분모 자유도 : 12
# (3) - F 분포
# (4) - SST : 23.212 SSE : 208.324
# (5) - 0.6685
# (6) - F값이 2.80 보다 작으므로 귀무가설을 기각할 수 없다

# 9-2
page = c(172,286,163,205,197,87, 94,123,106,101, 82, 153,87,103, 96,104,136,98,207,146)
genre = c(rep("A",5), rep("B",5), rep("C",5), rep("D",5))
book = data.frame(page,genre)
book
results = aov(page ~ genre, data=book)
anova(results)

# (1) - 8.6885, 3.23보다 크므로 귀무가설을 기각한다.
page = c(87, 94,123,106,101, 82, 153,87,103, 96,104,136,98,207,146)
genre = c(rep("A",5), rep("B",5), rep("C",5))
book = data.frame(page,genre)
book
results = aov(page ~ genre, data=book)
anova(results)

# (2) - 2.1227, 3.85보다 작으므로 귀무가설을 기각할 수 없다.

# 9-3
jump = c(36,42,51, 32,35, 38,48,50, 39, 38,44,46, 41,39, 40)
team = c(rep("A",3), rep("B",3), rep("C",3), rep("D",3),rep("E",3))
bas = data.frame(jump,team)
bas
results = aov(jump ~ team, data=bas)
anova(results)

# (ㄱ) - 4
# (ㄴ) - 10
# (ㄷ) - 237.33
# (ㄹ) - 48.9
# (ㅁ) - 2.0604

# 9-4
eat=c(6,8,2,4,6,4,1,5,2,7,3,5,4,6,8,3,5,1,7)
loc=c(rep("A",5), rep("B",4), rep("C",5), rep("D",5))
result=data.frame(eat,loc)
result
results=aov(eat~loc,data=result)
anova(results)

#           Df Sum Sq Mean Sq F value Pr(>F)
# loc        3 13.032  4.3439  0.8853 0.4711
# Residuals 15 73.600  4.9067

# 9-5
score=c(72,84,77,80,81,83,73,84,81,80,78,84,81,86,79,82)
class=c(rep("A",5), rep("B",4), rep("C",7))
result=data.frame(score,class)
result
results=aov(score~class,data=result)
anova(results)

# F값이 0.6388로 3.805보다 작기 때문에 귀무가설을 기각할 수 없다.

# 9-6
race=c(19.3,19.1,19.4,19.5,19.9,19.5,19.4,19.2,19.4,19.5,19.6,19.1,19.2,19.6,19.5,19.4,20.1,20.2,19.6,19.8)
loc=c(rep("A",4), rep("B",4), rep("C",4), rep("D",4),rep("E",4))
result=data.frame(race,loc)
result
results=aov(race~loc,data=result)
anova(results)

# F값이 4.22로 4.893보다 작기 때문에 귀무가설을 기각할 수 없다.

# 9-7
cus=c(1210,1080,1537,941,2107,1149,862,1870,1528,1382,2846,1638,2019,1178,2233)
snow=c(rep("A",4), rep("B",6), rep("C",5))
result=data.frame(cus,snow)
result
results=aov(cus~snow,data=result)
anova(results)

#(1)
#           Df  Sum Sq Mean Sq F value  Pr(>F)  
#snow       2 1468909  734455  3.1264 0.08075 .
#Residuals 12 2819077  234923  

# (2) - 3.13으로 3.89보다 작기 때문에 귀무가설을 기각할 수 없다.
# (3) - 3.13으로 2.81보다 크기 때문에 귀무가설을 기각할 수 있다.

# 9-8
watch=c(45,12,18,38,23,35,15,43,68,50,31,22,72,37,56,60,51)
chn=c(rep("A",6), rep("B",6), rep("C",5))
result=data.frame(watch,chn)
result
results=aov(watch~chn,data=result)
anova(results)

# 4.08로 3.74보다 크기 때문에 귀무가설을 기각할 수 있다.