class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key, val in self.dic.items():
            if value - key in self.dic: 
                if value - key != key:
                    return True
                else:
                    if val >= 2:
                        return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
