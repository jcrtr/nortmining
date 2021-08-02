import os
import timeit

farm = ['1', '2', '3', '4', '5', '6']
darm = ('1', '2', '3', '4', '5', '6')

# while True:
#     try:
#         print(farm[0])
#         farm.remove(f'{farm[0]}')
#     except IndexError:
#         print(f"Выполнение-1: {format(os.getpid())} мс")
#         break


code_to_test = """
farm = ['1', '2', '3', '4', '5', '6']
while True:
    if farm:
        print(farm[0])
        farm.remove(f'{farm[0]}')
    else:
        break
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)

# while True:
#     if farm:
#         print(farm[0])
#         farm.remove(f'{farm[0]}')
#     else:
#         break