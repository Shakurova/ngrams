library(ggplot2)
library(plotly)
# get data ----------------------------------------------------------------
setwd("C:/Users/Елена/Desktop/Курсач/py3_version/russian/")
pair<-read.csv("sy_vl_result_comparation.csv")
# G. Moroz's plot ---------------------------------------------------------
p <- ggplot(pair, aes(x=log10(syroj), y=log10(vlazhnyj)))+
  geom_point(size = 3, col = pair$code)+
  geom_smooth(method = "lm")+
  theme_bw()+ # hate that gray ggplot style
  xlab("syroj")+
  ylab("vlazhnyj")
p
cor(pair$syroj,pair$vlazhnyj)




