# mark => grouping of the test cases
# fixture
# confest.py
# parametrize => to execute same test method with different input and output , we will use parametrize
# xskip => to skip the particular test case from execution
# xfail => to not consider even the test case is failed
import pytest


def add(a, b):
    return a + b

def sub(a,b):
    pass

@pytest.mark.smoke
def test_basic_add():
    result = add(5,6)
    assert result == 11

@pytest.mark.parametrize("input1,input2,output", [(3, 4, 7), (-2, -3, -5), (-2, 3, 1),(0,0,0)])
def test_add(input1, input2, output):
    result = add(input1, input2)
    assert result == output

@pytest.mark.skip
def test_sub():
    result = sub(3,4)
    assert result == -1

@pytest.mark.xfail
def test_sub():
    result = sub(5,4)
    assert result == 1

# fixture => it's nothing but combination of setup and tear down
# setup => defining a functionality which need to be executed before executing of  test method
# tear down => this will execute after completion of test method execution
# in fixture we will segregate setup and tear down by using yield keyword



