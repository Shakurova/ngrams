library(ggplot2)
library(plotly)
# get data ----------------------------------------------------------------
setwd("C:/Users/≈лена/Desktop/ урсач/py3_version/russian/comparation")
pair<-read.csv("go_te_result_comparation.csv")
# G. Moroz's plot ---------------------------------------------------------
p <- ggplot(pair, aes(x=log10(goryachij), y=log10(teplyj)))+
  geom_point()+
  geom_smooth(method = "lm")+
  theme_bw()+ # hate that gray ggplot style
  xlab("гор€чий")+
  ylab("теплый")
p




