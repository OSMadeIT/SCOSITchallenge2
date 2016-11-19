n = [10, 20, 20, 10, 10, 30, 50, 10, 20]
count = 0
for i in set(n):    # convert the list n to a set and loop over each value of the set
    if n.count(i) // 2 >= 1:     # count is an inbuilt function that counts the number of occurance of a value in a list
        count += n.count(i) // 2
print(count)
