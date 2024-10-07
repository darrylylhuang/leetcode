# Encode and Decode Strings
class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        encoded = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                encoded += strs[i]
            else:
                encoded += strs[i] + "\0"
        return encoded.strip()

    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        return str.split("\0")
