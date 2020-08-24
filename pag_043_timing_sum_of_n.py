import time


def sum_of_n_2(n):
    start = time.time()
    
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
        
    end = time.time()
    
    return the_sum,end-start


for i in range(5):
    print("Sum is %d required %10.7f seconds with sum_of_n_2" % sum_of_n_2(10000))

for i in range(5):
    print("Sum is %d required %10.7f seconds with sum_of_n_2" % sum_of_n_2(1000000))
    
    
def sum_of_n_3(n):
    start = time.time()
    
    result = (n * (n + 1)) / 2
    
    end = time.time()
    
    return result,end-start

      
for i in range(5):
    print("Sum is %d required %10.7f seconds with sum_of_n_3" % sum_of_n_3(10000))

for i in range(5):
    print("Sum is %d required %10.7f seconds with sum_of_n_3" % sum_of_n_3(1000000))

for i in range(5):
    print("Sum is %d required %10.7f seconds with sum_of_n_3" % sum_of_n_3(10000000000))
