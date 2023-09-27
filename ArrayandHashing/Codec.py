# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# problem:
# - input a long url => encode => tiny url
# - input a tiny url => decode => long url

# tinyurl = base url + code
# - how to encode :
#   + generate code
#   + hash table store code => long url
# - how to decode:
#   + get code
#   + look up code in a hash table : code : long url


class Codec():

  def __init__(self):
    self.url_to_code = {}
    self.code_to_url = {}
    self.base_url = "http://tinyurl.com/"

  # create a unique key for long url
  def generate_code(self):
    return str(len(self.url_to_code))

  def encode(self, longUrl):
    if longUrl in self.url_to_code:
      print(self.base_url + self.url_to_code[longUrl])
      return self.base_url + self.url_to_code[longUrl]

    code = self.generate_code()
    # add to hash table 1 long url -> code
    self.url_to_code[longUrl] = code
    # add to hash table 2 code => long url
    self.code_to_url[code] = longUrl
    return self.base_url + code

  def decode(self, shortUrl):
    code = shortUrl[len(self.base_url):]
    return self.code_to_url.get(code, "")


url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
tiny_url = codec.encode(url)
print("Encoded URL:", tiny_url)  # Output: Encoded URL
decoded_url = codec.decode(tiny_url)
print("Decoded URL:", decoded_url)  # Output: Original URL
