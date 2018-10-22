import hashlib
class Codec:
    def __init__(self):
        self.urlmap = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        md5 = hashlib.md5()
        md5.update(longUrl.encode())
        slug = md5.hexdigest()
        self.urlmap[slug] = longUrl
        return "http://tinyurl.com/" + slug

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        if shortUrl[:19] != "http://tinyurl.com/":
            return ""

        slug = shortUrl[19:]
        try:
            return self.urlmap[slug]
        except KeyError:
            return ""
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
