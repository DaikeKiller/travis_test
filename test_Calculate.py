import pytest

@pytest.mark.parametrize("a,b,expected",[
                          (2,3,5),
						  (3,7,10),
						  (-2,5,3),
						  (0.1,0.2,0.3)
						  ])
def test_add(a,b,expected):
    from Calculate import add
    result = add(a,b)
    assert result == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected",[
                          (2,3,-1),
						  (3,7,-4),
						  (-2,5,-7)
						  ])
def test_sub(a,b,expected):
    from Calculate import sub
    result = sub(a,b)
    assert result == expected

