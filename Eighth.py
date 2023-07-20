# def name():
#     print("Hello world!")
# name()

#1 пример

# name = lambda:print("Hello world")
# name()

# num = [4,2,5,1,5]
# num2 = 2

# print (num*num2)

# number = [4,2,5,1,5]
# sum_num = 2
# for i in number:
#     sum_num *=number
# print(f"Сумма : {sum_num}")


# numbers = [4,2,5,1,5]
# def num(numbers):
#     for i in numbers:
#         print(num-2)


#2 пример

# my_list = [4,2,5,1,5]
# number = list(map(lambda numbers:numbers*2,my_list))
# print(number)

#3 пример
# def multiply(x,y):
#     print(x*y)

# multiply(6,9)

#4 пример
# multiply = lambda x,y:x*y
# print(multiply(6,9))

#456,72

# multiply = lambda x,y:x-y
# print(multiply(456,72))

# >>> L = [1, 2, 3, 4]
# >>> list(map(lambda x: x**2, L))
# [1, 4, 9, 16]

# multiply = lambda x,y:[x+y,x-y,x*y,x/y]
# print(multiply(456,72))

#работа с файлами 1
# txt = open('lesson.py','w')
# txt.write("print(5+5)")
# txt.close

# 3 пример
# txt = open('qwerty.txt','r')
# result = txt.read()
# print(result)

# with open('geeks.txt','w') as txt:
#     txt.write("Hello geeks")

# #4 пример
# with open("geeks.txt","r") as txt:
#     content = txt.read()
#     print(content)