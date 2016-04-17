library(ggplot2)
library(plotly)
# get data ----------------------------------------------------------------
setwd("C:/Users/≈лена/Desktop/ урсач/py3_version/russian/comparation")
pair<-read.csv("go_te_result_comparation.csv")
# G. Moroz's plot ---------------------------------------------------------
p <- ggplot(pair, aes(x=goryachij, y=teplyj, z=noun))+
  geom_point()+
  theme_bw()+ # hate that gray ggplot style
  xlab("гор€чий")+
  ylab("теплый")+
  scale_x_log10()+
  scale_y_log10()
p
ggplotly(q, tooltip = c("z"))

# with the regression line -------------------------------------------------
p <- ggplot(pair, aes(x=goryachij, y = teplyj))+
  geom_point()+
  geom_smooth(method = "lm")+
  theme_bw()+ # hate that gray ggplot style
  xlab("гор€чий")+
  ylab("теплый")+
  scale_x_log10()+
  scale_y_log10()
p


