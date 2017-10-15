class Codec:
    source = string.ascii_letters + '0123456789'
    def __init__(self):
        self.urlMap = {}
        self.codeMap = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.urlMap:
            return self.urlMap[longUrl]
        code = ''.join(random.choice(Codec.source) for _ in range(6))
        while code in self.codeMap:
            code = ''.join(random.choice(Codec.source) for _ in range(6))
        self.codeMap[code] = longUrl
        self.urlMap[longUrl] = 'http://tinyurl.com/' + code
        return self.urlMap[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.codeMap[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))