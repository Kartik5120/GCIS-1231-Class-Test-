import question1

def test_smallest_number_1():
    num1 = 10
    num2 = 20
    num3 = 30
    small_num = question1.smallest_number(num1, num2, num3)
    assert (small_num == 10)


#Testing that words

def test_smallest_number_2():
    num = 10, 20, 30
    small_num = question1.smallest_number(num)
    assert (small_num == 10)
    