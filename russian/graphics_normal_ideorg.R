library(ggplot2)
library(plotly)
# get data ----------------------------------------------------------------
setwd("C:/Users/Елена/Desktop/Курсовая/Программа/russian/graphics_and_comparation/old_comparation")
pair<-read.csv("hu_to_result_comparation.csv", encoding="UTF-8", header = T)
# G. Moroz's plot ---------------------------------------------------------
p <- ggplot(pair, aes(x=log10(hudoj), y=log10(toschij)))+
  geom_point(size = 3,
             col = pair$colour)+
  geom_smooth(method = "lm")+
  theme_bw()+ # hate that gray ggplot style
  xlab("hudoj")+
  ylab("toschij")
p

cor(pair$hudoj,pair$toschij)
#shapiro.test(pair$hudoj)

#boxplot(hudoj ~ noun, data = pair)

y <- pair$hudoj
x <- pair$toschij
cor(x,y)

boxplot(y, las = 2)
#boxplot.stats(y)$out
ind <- which(y %in% boxplot.stats(y)$out)
outler <- data.frame(x=x[ind], y=y[ind])
ind
#plot(x,y,col='blue', pch=20, ylim=c(0,max(y)))
#points(outler$x, outler$y, col='red',pch=19)
x <- x[-ind]
y <- y[-ind]
boxplot(y)
plot(x,y,col='blue', pch=20, ylim=c(0,max(y)))
cor(x,y)

boxplot(x, las = 2)
#boxplot.stats(x)$out
ind <- which(x %in% boxplot.stats(x)$out)
outler <- data.frame(x=x[ind], y=y[ind])
ind
x <- x[-ind]
y <- y[-ind]
boxplot(x)

cor(x,y)


#p <- ggplot(pair, aes(x=log10(hudoj), y=log10(hudoj), z=noun))+
  #geom_point(size = 2, 
             #col = pair$colour)+
  #theme_bw()+ # hate that gray ggplot style
  #xlab("hudoj")+
  #ylab("hudoj")
#p
#ggplotly(tooltip = c("z"))
