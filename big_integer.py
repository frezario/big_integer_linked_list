"""
A BigInteger implementation.
"""
from copy import deepcopy

from node import TwoWayNode


class BigInteger:
    """
    A BigInteger class.
    """

    def __init__(self, init_value="0"):
        self.sign = init_value[0] != '-'
        init_value = init_value.strip('-+')
        if init_value != "0":
            init_value = init_value.lstrip('0')
        assert init_value != '', "Incorrect number"
        self.head = TwoWayNode(init_value[0], None, None)
        node = self.head
        for symbol in init_value[1:]:
            node.next = TwoWayNode(symbol, node, None)
            node = node.next
        self.tail = node

    def __repr__(self):
        result = "BigInteger("
        result += '-' if not self.sign else ''
        node = self.head
        while node:
            result += node.data
            node = node.next
        result += ')'
        return result

    def __eq__(self, other):
        assert isinstance(other, BigInteger)
        return self.to_string() == other.to_string()

    def __abs__(self):
        result = deepcopy(self)
        result.sign = True
        return result

    def __gt__(self, other):
        assert isinstance(other, BigInteger)
        if self.sign != other.sign:
            return True if self.sign is True else False
        if len(self.to_string()) != len(other.to_string()):
            return True if len(self.to_string()) > len(other.to_string()) else False
        node1, node2 = self.head, other.head
        while node1 is not None and node1.data == node2.data:
            node1 = node1.next
            node2 = node2.next
        if node1 is None:
            return False
        return True if node1.data > node2.data else False

    def __ge__(self, other):
        assert isinstance(other, BigInteger)
        return self > other or self == other

    def to_string(self):
        """
        Converts a big integer into string.
        """
        return repr(self).replace('(', '').replace(')', '').replace("BigInteger", '')

    def simple_add(self, other):
        """
        Adds two Bigintegers and returns a result.
        other must be less than self.
        """
        assert isinstance(other, BigInteger), "Bad type"
        assert self >= other
        result = deepcopy(self)
        node1 = self.tail
        node2 = other.tail
        res_node = result.tail
        to_add_or_not_to_add = False
        while node1 is not None:
            term = int(node2.data) if node2 is not None else 0
            temp = int(node1.data) + term + int(to_add_or_not_to_add)
            to_add_or_not_to_add = temp >= 10
            res_node.data = str(temp % 10)
            node1 = node1.previous
            node2 = node2.previous if node2 is not None else node2
            res_node = res_node.previous
        # Special case: one more digit to add
        if to_add_or_not_to_add:
            tmp = result.head
            result.head.previous = TwoWayNode("1", None, tmp)
            result.head = result.head.previous
        return result

    def simple_sub(self, other):
        assert isinstance(other, BigInteger), "Bad type"
        assert self >= other

    def __add__(self, other):
        min_num = other
        max_num = self
        if abs(self) < abs(other):
            min_num = self
            max_num = other
        # print(f"min: {min_num}, max {max_num}")
        if max_num.sign == min_num.sign:
            return max_num.simple_add(min_num)
        else:
            # TODO: SIMPLE SUBTRACTING
            pass