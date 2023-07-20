#try ,except


def name(num1,num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("На ноль делить нельзя")

def calculator(num1,num2,a):
    try: 
        if a == "+":
            print(num1+num2)
        elif a == "-":
            print(num1-num2)
        elif a == "*":
            print(num1*num2)
        elif a == "/":
            try:
                print(num1/num2)
            except ZeroDivisionError:
                print("На ноль делить нельзя")
        else:
            print("Ошибка")
    except TypeError:
        print("Введите число!")

#args ,kwargs
# def lister(obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10):
#     list1=[]
#     list1.append(obj1)
#     list1.append(obj2)
#     list1.append(obj3)
#     list1.append(obj4)
#     list1.append(obj5)
#     list1.append(obj6)
#     list1.append(obj7)
#     list1.append(obj8)
#     list1.append(obj9)
#     list1.append(obj10)
#     print(list1)
# lister("NUrbolot","MIrgul","Aliya","Cudbuhon","Rahmattulo","Hicmatulloh","Urmat","Imron","Aziz","Adina")

# def lister(*name):
#     list1=[]
#     for result in name:
#         list1.append(result)
#     print(list1)
# lister("NUrbolot","MIrgul","Aliya","Cudbuhon","Rahmattulo","Hicmatulloh","Urmat","Imron","Aziz","Adina")

# def pizza(*ing):
#     for i in ing:
#         print(f"Вы добавили :{ing}")
# pizza("Грибы","Соус","Помидоры","Болгарский перец","Пипирони","Сыр","Оливки")

def make_pizza(**kwargs):
    for key,value in kwargs.items():
        print(f"Размер -  {value}. Адрес:{value}")
        
make_pizza(size = "Большой",adddress = "Geeks")
