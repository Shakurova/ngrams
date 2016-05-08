library(ggplot2)
library(plotly)
# get data ----------------------------------------------------------------
setwd("C:/Users/Елена/Desktop/Курсач/py3_version/russian/")
pair<-read.csv("hu_to_result_comparation.csv")
# G. Moroz's plot ---------------------------------------------------------
p <- ggplot(pair, aes(x=log10(hudoj), y=log10(toschij)))+
  geom_point(size = 3, col = pair$code)+
  geom_smooth(method = "lm")+
  theme_bw()+ # hate that gray ggplot style
  xlab("hudoj")+
  ylab("toschij")
p
cor(pair$hudoj,pair$toschij)

