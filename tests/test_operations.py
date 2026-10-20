from src.introduction_to_git_hubactions.math_operations import add, substract

def test_add():
    assert add(2,3) == 5
    assert add(-1,1)==0


def test_substract():
    assert substract(5,3)==2
    assert substract(4,1)==3
    assert substract(3,3)==0
    assert substract(2,3)==-1
