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


p2 <- hist(Speaker2Counts,
           main="Histogram of Word Counts by Both Speakers",
           xlab="Number",
           ylab="Frequency",
           breaks=6)
p1 <- hist(Speaker1Counts, breaks=6)
# print(p1)
# print(p2)
plot( p2, col=rgb(1,0,0,1/4), ylim=c(0,20))  # second
plot( p1, col=rgb(0,0,1,1/4), add=T)  # first histogram
print(p1.$breaks)
print(p2.$breaks)


