import os

def test_01():

    assert os.path.exists("submission/file1.txt")
    assert os.path.exists("submission/file2.txt")
    assert os.path.exists("submission/file3.txt")
