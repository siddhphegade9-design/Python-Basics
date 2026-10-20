import re
text = "The quick brown fox jumps over the lazy dog. Hello"
# This module is used to search a particular string or pattern
match = re.search("brown", text)
print(match)
if match:
    print("Match Found!")
    print("Start index:", match.start())
    print("End index:", match.end())

