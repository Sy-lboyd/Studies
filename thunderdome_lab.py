def prime_check(num):
    if num == 1:
        return False
    elif num == 2:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                print(i)
                return False
        return True
                    
print(prime_check(33))