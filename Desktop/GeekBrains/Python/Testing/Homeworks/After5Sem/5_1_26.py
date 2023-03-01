# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

# pow(base, exp, mod) - pow(возводимое число, число, являющееся степенью, необязательно, число, на которое требуется произвести деление по модулю)

def pow(a, b): 
    if b == 0: 
        return 1
    elif b % 2 == 0: 
        return pow(a * a, b / 2) 
    else: 
        return a * pow(a * a, b // 2)

print(pow(2, 0)) #1
print(pow(2, 1)) #2
print(pow(2, 3)) #8
print(pow(2, 4)) #16