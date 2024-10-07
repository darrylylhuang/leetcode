# Encode and Decode Strings
class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        encoded = str(len(strs))
        for i in range(len(strs)):
            encoded += strs[i] + "\0"
        return encoded

    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        decoded = str.split("\0")
        if decoded[0] > len(decoded) - 1:
            return decoded[1:-1]
        return decoded[1:]
