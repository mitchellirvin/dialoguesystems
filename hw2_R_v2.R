# set the file address: 
setwd("/Users/obadiah/dialoguesystems") 

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

# Max count for each speaker (to size the histogram)
print(max(Speaker1Counts))
print(max(Speaker2Counts))

# what data type are our two speaker count sets stored as?
print(attributes(Speaker1Counts))

# Histogram. Still working on it

# hist(Speaker1Counts, 
#     main="Histogram", 
#     xlab="Number", 
#     ylab="Frequency", 
#     border="blue", 
#     col="green",
#     ylim = c(0, 10.0),
#    breaks=length(Speaker1Counts))

Words_in_Utterance <- Speaker2Counts
p2 <- hist(Words_in_Utterance,
           xlab="Number",
           ylab="Frequency",
           breaks=10)
p1 <- hist(Speaker1Counts, main="Histogram of Word Counts by Both Speakers", breaks=10)
plot( p2, col=rgb(1,0,0,1/4), ylim=c(0,30))  # second
plot( p1, col=rgb(0,0,1,1/4), add=T)  # first histogram

moredata <- read.csv("b.csv", header=TRUE, sep=",")

tbl = table(moredata$Speaker,moredata$ContainsMoney)
chisq.test(tbl, correct = FALSE)

