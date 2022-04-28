from time import perf_counter_ns as p
iter = 0
n = 0

def select_Number():
    n = int(input("Select the number for calculation?"))
    if (n == 0):
        print ("Select the other number.")
        print ()
        print ()
        select_Number();
    else:
        calculate(n);

def calculate(n):
    global iter
    iter = 0
    start = p()
    while n != 1:
        if (n % 2):
            n = (n*3+1)
            print (n) 
            iter += 1
        else:
            n = (n//2)
            print (n) 
            iter += 1

    end = p()
    print ("The number has reached " + str(n) + " and have only " + str(iter) + " iterations and with time: "
     + format(end-start) + " nano seconds.")
    print()
    select_Number();

select_Number();
