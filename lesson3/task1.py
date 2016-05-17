# Write a program to generate list with all numbers divisible by 2 and 3 between 1 and 10000 using two approaches:
if __name__ == "__main__":
    # using list comprehension
    b=[i for i in range(1,10000) if (i%2==0 or i%3==0)]
    print b
    #  using filter
    list=range(1,10000)
    result=filter(lambda x:(x%2==0 or x%3==0),list)
    print result
