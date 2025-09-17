def helloWorld():
    msg = "Hello, World!"
    print(msg)
    return msg

def test_answer():
    assert helloWorld() == "Hello, World!"