# Encode and Decode Strings
class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        # include a buffer string at the beginning that will be stripped
        encoded = str(len(strs))
        for i in range(len(strs)):
            encoded += "\0" + strs[i]
        return encoded

    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        decoded = str.split("\0")
        return decoded[1:]
