def test_1():
    test_3()
    print("A")
    
def test_2():
    print("B")
    test_1()
    
def test_3():    
    print("C")
    
print(test_1())
