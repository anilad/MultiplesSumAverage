# # print "Multiples, Sum, Average"

# #Part 1 Write code that prints all the odd numbers from 1-1000 using a for loop but not using a list
# count = 0
# for count in range(0,1000):
#     if count & 1:
#         print count
#     else:
#         continue


# #Part 2 Create another program that prints all multiples of 5 from 5-1,000,000
# for x in range(0, 1000000):
#     if x % 5 == 0:
#         print x
#     else:
#         continue

# #Sum List: Create a Program that prints the sum of all values in the list: a= [1,2,5,10,255,3]
a= [1,2,5,10,255,3]
# sum= 0
# for element in a:
#     sum+= element
# print sum

#Average List: Create a program that prints the average of the values in the list: a=[1,2,5,10,255,3]
def avg(list):
    sum= 0
    avg=0
    for element in list:
        sum+= element
    avg=sum/len(list)
    return avg
print avg(a)