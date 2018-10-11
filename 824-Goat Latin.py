class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')
        goat = 'ma'
        count = 1
        
        S = S.split(' ')
        res = []
        for word in S:
            if word[0] in vowels:
                res.append(word + goat + count * 'a')
            else:
                res.append(word[1:] + word[0] + goat + count * 'a')
            count += 1
        return ' '.join(res).rstrip()
