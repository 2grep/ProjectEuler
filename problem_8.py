num = 7316717

n = 4

# gp = [0 for i in range(1,n+1)]

def is_bigger(index,n,num,gp):
    product = 1
    for i in range(index,index+n):
        if num[i] == 0:
            break
        product = product * num[i]
        if product > gp:
            gp = product
    return gp

# is_bigger(2,n,num,1)

def find_biggest_n_prod(num,n):
    digit_list = [int(digit) for digit in str(num)]
    gp = 1
    for i in range(0,len(digit_list)):
        gp = is_bigger(i,n,digit_list,gp)
    return gp