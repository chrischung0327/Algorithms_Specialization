def strMultiply(str1: str, str2:str) -> int:
    ret = 0
    a, b = len(str1), len(str2)
    if a > 0 and b > 0:
        ret = int(str1[0]) * int(str2[0]) * 10**(len(str1)+len(str2)-1-1) + strMultiply(str1[1:], str2[1:]) + 10**(len(str1)-1)*strMultiply(str1[0], str2[1:]) + 10**(len(str2)-1)*strMultiply(str1[1:], str2[0])
    return ret


print(strMultiply('123', '456'))
print(123*456)

print(strMultiply('3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627'))
print(3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627)
