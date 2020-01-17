n = int(input('enter data :'))
d = int(input('enter data :'))


try:
    #div
    if d<0:
        er = ZeroDivisionError('divisor cannot be less than 0')
        raise er
    
    o =n/d
    print(o)

except ZeroDivisionError as e:
    print(e)

except NameError as e:
    print(e)

except:
    #pass
    print('there is technical error')
    
finally:
    print('end of code')

#add
o = n+d
print(o)





