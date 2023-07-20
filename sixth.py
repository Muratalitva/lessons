#встроенные функции 
# print("hello world")

#не встроенные
# def geeks():
#     b = 2+2
#     print(b)
# geeks()

# def hi():
#     name = "Nurbolot"
#     print(f"Hello {name}.How are you?")
# hi()

# def welcom():
#     name = input("Введите своё имя:")
#     print(f"Добро пожаловать {name}")
# welcom()

def calculator():
    num = int(input("Введите первое число: "))
    num2 = int(input("Второе чилсо: "))
    summa = input("Выберите символ '+','-','/','*'")
    if summa == '+':
        print (num+num2)
    elif summa == '-':
        print (num-num2)
    elif summa == '*':
        print (num*num2)
    elif summa == '/':
        print (num/num2)
    else:
        print('Error')
calculator()

# def welcome(name,surname):
#     print(f"Hello {name}")

# welcome("Nurbolot" ,"Erkinbaev")

def calculator(num1 ,num2,a ):
    if a == '+':
        print (num1+num2)
    elif a == '-':
        print (num1-num2)
    elif a == '*':
        print (num1*num2)
    elif a == '/':
        print (num1/num2)
    else:
        print('Error')
num1 = int(input("Первое чилсо: "))
num2 = int(input("Второе чилсо: "))
summa = input("Выберите символ '+','-','/','*'")
calculator(num1,num2, summa)

