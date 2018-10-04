class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + ":" + s
        return encoded_str

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            strs.append(s[i+1:i+1+length])
            s = s[i+1+length:]
        return strs
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
