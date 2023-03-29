## 함수 선언부(=메서드)
def add_func(n1,n2) :
    retValue = n1+n2
    return retValue

def sub_func(n1,n2) :
    return n1 - n2

def mul_func(n1,n2) :
    return n1 * n2
# 자바의 try-catch를 python에서는 try-except로 나타낼수 있다
def div_func(n1, n2):
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by 0")

## 전역 변수부
num1= int(input())
num2= int(input())

## 메인 코드부
hap = add_func(num1,num2)
print(num1, '+' , num2 , '=' , hap)

sub = sub_func(num1,num2)
print(num1, '-' , num2 , '=' , sub)

print(num1, '*' , num2 , '=' , mul_func(num1,num2))

div = div_func(num1,num2)
if div is not None:
    print(num1, '/', num2, '=', div)
