install.packages("RColorBrewer")
install.packages("wordcloud2")
install.packages("plotrix")
library(RColorBrewer)
library(wordcloud2)
library(plotrix)

carCrush = read.csv("./data/carCrush_dead.csv", header=T)
carCrush[4] # 주야
carCrush[5] # 요일
carCrush[11] # 발생시지도
carCrush[17] # 법규위반
carCrush[20] # 차종
carCrush[21] # 차량크기

# 주야 사망교통사고 빈도
wordcount1 = table(carCrush[4])
head(sort(wordcount1, decreasing = T),2)

bchart = head(sort(wordcount1, decreasing = T),2)
pct = round(bchart/sum(bchart) * 100,1)
names = names(bchart)

lab = paste(names,"\n", "(", pct,"%)")
pie3D(bchart, main="주야 사망교통사고 빈도", col=c("red","blue"),
      labels = lab, explode = 0.05)


# 요일별 사망교통사고 현황 
wordcount2 = table(carCrush[5])
bchart = head(sort(wordcount2, decreasing = T),7)

bp = barplot(bchart, main="요일별 사망교통사고 현황", col=rainbow(7), 
             las=1, ylim = c(0,700),cex.names = 2, cex.axis = 2)

pct = round(bchart/sum(bchart) * 100,1)

text(x=bp, y=bchart*1.03, labels = paste("(", pct, "%)"),
     col="black", cex = 2)
text(x=bp, y=bchart*0.95, labels = paste(bchart,"건"),
     col="black", cex = 2)

# 사망교통사고 발생한 시도 현황
wordcount3 = table(carCrush[11])
head(sort(wordcount3, decreasing = T),17)

wordcloud2(wordcount3)

# 법규위반 Top 5
wordcount4 = table(carCrush[17])
head(sort(wordcount4, decreasing = T),14)

bchart = head(sort(wordcount4, decreasing = T),5)
pct = round(bchart/sum(bchart) * 100,1)
names = names(bchart)

lab = paste(names,"\n", "(", pct,"%)")
pie3D(bchart, main="법규위반 Top 5", col=rainbow(5),
      labels = lab, explode = 0.05)

# 차종 Top 5
wordcount5 = table(carCrush[20])
head(sort(wordcount5, decreasing = T),10)

bchart = head(sort(wordcount5, decreasing = T),5)
pct = round(bchart/sum(bchart) * 100,1)
names = names(bchart)

lab = paste(names,"\n", "(", pct,"%)")
pie3D(bchart, main="차종 Top 5", col=rainbow(5),
      labels = lab, explode = 0.05)

# 차량크기
wordcount6 = table(carCrush[21])
head(sort(wordcount6, decreasing = T),10)

bchart = head(sort(wordcount6, decreasing = T),5)
pct = round(bchart/sum(bchart) * 100,1)
names = names(bchart)

lab = paste(names,"\n", "(", pct,"%)")
pie3D(bchart, main="차량크기 Top 5", col=rainbow(5),
      labels = lab, explode = 0.05)