# set the file address: 
#setwd("/Users//Documents/...") 

mydata <- read.csv("a.csv", header=TRUE, sep=",")

# putting the number of words per utterance into a list for Speaker1 and Speaker2
Speaker1Counts <- subset(mydata, Speaker==1)$Counts
Speaker2Counts <- subset(mydata, Speaker==2)$Counts


# Median value for Speaker1 and Speaker2
print(median(Speaker1Counts))
print(median(Speaker2Counts))

# Mode value for Speaker1 and Speaker2
mode <- print(names(sort(-table(Speaker1Counts)))[1])
print(mode)

# Standart deviation for Speaker1 and Speaker2
print(sd(Speaker1Counts))
print(sd(Speaker2Counts))

# Histogram. Still working on it

hist(Speaker1Counts, 
     main="Histogram", 
     xlab="Number", 
     ylab="Frequency", 
     border="blue", 
     col="green",
     ylim = c(0, 10.0),
     breaks=length(Speaker1Counts))

