library(ggplot2)
library(plotly)
# get data ----------------------------------------------------------------
setwd("C:/Users/Елена/Desktop/Курсовая/Программа/russian/graphics_and_comparation/")
pair<-read.csv("vl_mo_result_0_cat2_d_comparation.csv", encoding="UTF-8", header = T)

y <- log10(pair$vlazhnyj)
x <- log10(pair$mokryj)

boxplot(y, las = 2)#это выбросы для влажный
boxplot(x, las = 2)#это выбросы для мокрый


boxplot.stats(y)$out
ind <- which(y %in% boxplot.stats(y)$out)
outler <- data.frame(x=x[ind], y=y[ind])
y <- y[-ind]#удаление выбросов у влажный
boxplot(y)