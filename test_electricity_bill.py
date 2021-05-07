from electricity_bill import total
def test_total():
    assert total(2, 3, 1)  ==0
    assert total (2, 3, 2) == 10
    assert total (3,2,2) == 20
    assert total (2, 2, 2 ) == 14
    

