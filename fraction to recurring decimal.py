class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            result = "-"

        dvd, dvs = abs(numerator), abs(denominator)
        result += str(dvd / dvs)
        dvd %= dvs

        if dvd > 0:
            result += "."
        
        remainder = {}
        while dvd and dvd not in remainder:
            remainder[dvd] = len(result)
            dvd *= 10
            result += str(dvd / dvs)
            dvd %= dvs

        if dvd in remainder:
            result = result[:remainder[dvd]] + "(" + result[remainder[dvd]:] + ")"

        return result
