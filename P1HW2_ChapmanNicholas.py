#Calculates Travel Budget
#9-25-2022
#CTI-11 P1HW2 -Travel Expense
#Nicholas Chapman
#

print('This program calculates and displays travel expenses')
b = int(input('Enter Budget:'))
l = input('Enter your travel destination:')
g = int(input('How much do you think you wil spend on gas?'))
h = int(input('Approximately, how much will you need for accomidation/hotel?'))
f = int(input('Last, how much do you need for food?'))
e = g + h + f
v = b - e
print('------------Travel Expenses------------')
print('Location:', l)
print('Initial Budget:', b)
print()
print('Fuel:', g)
print('Accomidation:', h)
print('Food:', f)
print()
print('Remaining Balance:', v)
input('\n')