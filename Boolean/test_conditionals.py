import conditionals

def test_max_A_grade():
    #Arrange
    mark = 100
    #Act 
    grade = conditionals.convert_mark_to_grade(mark)
    #Assert
    assert(grade == "A")

def test_min_A_grade():
    #Arrange
    mark = 90
    #Act 
    grade = conditionals.convert_mark_to_grade(mark)
    #Assert
    assert(grade == "A")

def test_mark_min_range():
    mark = -1

    #  Act/Call 
    grade = conditionals.convert_mark_to_grade(mark)

    #Assert 
    assert(grade == None)

def test_mark_max_range():
    mark = 101

    #  Act/Call 
    grade = conditionals.convert_mark_to_grade(mark)

    #Assert 
    assert(grade == None)