#this solves basic differentials in the form y=ab**x
#I need to add something for if a non-float is entered
while True:
    co=float(input('What is the coefficient? '))
    po=float(input('What is x to the power of? '))

    co2=co*po
    if co2==0:
        print('d/dx=0')
    elif po==0:
        print('d/dx = 0')
    elif po== 1:
        print('d/dx=',co2)
    else:
        print('d/dx=',co2,'x**',po-1)