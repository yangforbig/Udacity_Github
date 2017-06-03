result <- list()
result$gp1 <- c(2,4,21)
result$gp2 <- c(4,5,11)
result$gp3 <- c(5,7,24)
result$gp4 <- c(2,6,42)
result
unlist.result <- unlist(result)
maxtrix.result <- matrix(unlist.result, 4, 3, byrow=T)
maxtrix.result
df.result <- as.data.frame(maxtrix.result)
colnames(df.result) <- c('apple', 'orange', 'banana')
df.result
