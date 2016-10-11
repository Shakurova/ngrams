#!/bin/Rscript

library(ggplot2)
library(plotly)

args<-commandArgs(trailingOnly=TRUE)

# get data ----------------------------------------------------------------
# setwd("/Users/elenashakurova/Desktop/ngrams/ngrams/russian/results")
pair<-read.csv(args[3], encoding="UTF-8", header = T)

jpeg(paste(args[1], args[2], 'rplot.jpg', sep = "_"))
# plot ---------------------------------------------------------
p <- ggplot(pair, aes(x=log10(get(args[1])), y=log10(get(args[2]))), z=noun)+
  geom_point(size = 3)+
  geom_smooth(method = "lm")+
  theme_bw()+ # hate that gray ggplot style
  xlab(args[1])+
  ylab(args[2])
p
dev.off()

ggp <- ggplotly(p, tooltip = c('z'))
htmlwidgets::saveWidget(as.widget(ggp), paste(args[1], args[2], 'index.html', sep = "_"))


cols <- c(args[1], args[2])
result <- pair[, cols]
print('Корреляция')
cor(result)

y <- pair[,args[1]]
x <- pair[,args[2]]
print('Корреляция')
cor(x,y)

boxplot(y, las = 2)
ind <- which(y %in% boxplot.stats(y)$out)
outler <- data.frame(x=x[ind], y=y[ind])
ind
x <- x[-ind]
y <- y[-ind]
boxplot(y)
plot(x,y,col='blue', pch=20, ylim=c(0,max(y)))



print('Корреляция')
cor(x,y)

boxplot(x, las = 2)
ind <- which(x %in% boxplot.stats(x)$out)
outler <- data.frame(x=x[ind], y=y[ind])
ind
x <- x[-ind]
y <- y[-ind]
boxplot(x)

print('Корреляция')
cor(x,y)
