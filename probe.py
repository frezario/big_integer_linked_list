from big_integer import BigInteger


def test_init():
    a = BigInteger("1250")
    print(a)
    b = BigInteger("-12")
    print(b)
    tst = a.head.next.next
    print(tst.previous.data)
    print(a.head.previous)
    d = BigInteger('+10')
    print(d)


def test_output():
    a = BigInteger()
    print(a.to_string())
    a = BigInteger('-0100')
    print(a)
    print(a.to_string())


def test_equality():
    a = BigInteger("10")
    b = BigInteger("-10")
    assert a != b
    # b.sign = True
    assert a == abs(b)
    print("Equality passed...")


def test_more_less_than():
    a = BigInteger("100")
    b = BigInteger("5050")
    assert b > a
    assert a <= b
    b.sign = False
    assert a > b
    b = BigInteger("-100")
    assert a > b
    b.sign = True
    assert a == b
    assert not a > b
    assert a >= b
    assert b <= a
    b = BigInteger("50")
    assert a >= b
    assert b <= a
    b.sign = False
    b = BigInteger("-5000")
    assert a >= b
    a = BigInteger("1075")
    b = BigInteger("828")
    assert not (b >= a)
    assert not (b > a)
    assert not (a <= b)
    assert not (a < b)
    print("More and less passed...")


def test_simple_add():
    a = BigInteger("1075")
    b = BigInteger("828")
    assert a.simple_add(b) == BigInteger("1903")
    a = BigInteger("19998")
    b = BigInteger("112")
    assert a.simple_add(b) == BigInteger("20110")
    a = BigInteger("59789")
    b = BigInteger("47738")
    assert a.simple_add(b) == BigInteger("107527")
    print("Simple add passed...")

def test_add():
    a = BigInteger("1075")
    b = BigInteger("828")
    assert b + a == BigInteger("1903")
    a = BigInteger("-9939")
    b = BigInteger("-84545")
    assert a + b == BigInteger("-94484")
    a = BigInteger("0")
    b = BigInteger("0")
    assert a + b == BigInteger("0")
    # TODO: ADD
    print("Add passed...")

test_equality()
test_more_less_than()
test_simple_add()
test_add()

