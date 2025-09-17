def helloWorld():
    msg = "Hello, World!"
    print(msg)
    return msg


#########################TESTS###############################
def test_answer():
    assert helloWorld() == "Hello, World!"