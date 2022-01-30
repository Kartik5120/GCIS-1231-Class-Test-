#calculator program

def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def test_add():
    #Arrange/Setup 
    a = 10 
    b = 15 
    #Act /Call
    sum = add(a, b)
    #Assert 
    return sum == 25 

def test_subtract():
    #Arrange/Setup 
    a = 10
    b = 15
    #Act/Call 
    sub = subtract(a, b)
    #Assert
    assert sub == -5

def test_multiply():
    #Arrange/Setup 
    a = 2
    b = 4
    #Act/Call
    mul = multiply(a, b)
    #Assert
    assert mul == 8