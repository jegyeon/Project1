##메서드 선언부
def add_func(n1,n2) :
    res = n1+ n2
    return res

def sub_func(n1,n2) :
    return n1- n2

def dev_func(n1,n2) :
    return n1/n2

def svl_func(n1,n2) :
    return n1*n2


## 전역 변수부(클래스변수, 인스턴스변수)
num1, num2,result = 100, 200, 0


##메인 코드부 ( static void main(String args[]){}
result = add_func(num1,num2)
print(num1, '+',num2,'=',result)

result = sub_func(num1,num2)
print(num1, '-',num2,'=',result)

result = dev_func(num1,num2)
print(num1, '/',num2,'=',result)

result = svl_func(num1,num2)
print(num1, '*',num2,'=',result)
