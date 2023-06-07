#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
""" class that test the function that returns max integer"""

class TestMaxInteger:
    """definition of class tester"""
    def test_empty_list(self):
        """test empty list"""
        mylist = []
        self.assertEqual(max_integer(mylist), None)
    def test_only_one(self):
        """test if one passed"""
        mylist = [1]
        self.assertEqual(max_integer(mylist), 1)
    def test_ascending_order(self):
        """"test if ascending order list is passed"""
        mylist = [1, 2, 3]
        self.assertEqual(max_integer(mylist), 3)
    def test_descending_order(self):
        """test if descending order list is passed"""
        mylist = [3, 2, 1]
        self.assertEqual(max_integer(mylist), 3)
    def test_string_passed(self):
        """test if a string is passed"""
        mystr = "mymsg"
        self.assertEqual(max_integer(mystr), None)
    def test_nonType_value(self):
        """test non type passed"""
        self.assertEqual(max_integer(None), None)
    def test_arrayof_str(self):
        """lists of string passed"""
        mylist = ["eugene", "claude", "john"]
        self.assertEqual(max_integer(mylist), "john")
    def test_double_passed(self):
        """if float numbers are passed"""
        mylist = [1.4, 5.4, 6.2]
        self.assertEqual(max_integer(ylist), 6.2)

if __name__ == '__main__':
    unittest.main()
