from client import fetch


def test_answer():
    if 'code' in fetch():
      assert true
    else:
        assert false