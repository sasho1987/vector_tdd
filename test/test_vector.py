from src.vector import Vector

def test_make_vector():
    v = Vector( [1,2,3])
    assert len(v.nums) == 3 #passes if true, flags if false


def test_dimensions():
    v = Vector( [6,7,8,9] )
    assert v.dims == 4 
    
def test_norm():
    v = Vector( [3,4] )
    assert v._length == 5



