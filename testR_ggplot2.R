install.packages("RColorBrewer")
library(RColorBrewer)
library(ggplot2)

data = data.frame(키워드 = c("외국인","서비스","브랜드","글로벌","일자리",
                          "목표주가","투자의견","아파트","영업이익","중소기업"),
                     빈도수 = c(2995, 2976, 2469, 2439, 2225,
                             2028, 2009, 1945, 1928, 1750))

#ggplot(data, aes(x=키워드, y=빈도수)) + geom_bar(stat = "identity")

ggplot(data, 
       aes(x=reorder(키워드, -빈도수), 
           y=빈도수)) + geom_bar(stat = "identity",
                              fill=rainbow(10)) + geom_text(aes(x=키워드, label=빈도수),
                                                            vjust=1.5, color = "white")
