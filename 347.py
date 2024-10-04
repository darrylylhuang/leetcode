# Top K Frequent Elements

# Worst Case O(nlogn) if every num in nums occurs once and we sort the top counts
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = dict()
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1

        # these are the counts for the most frequent numbers
        top_counts = nums_count.values()
        # sort them
        top_counts.sort()
        # take the top k counts
        top_counts = top_counts[-k:]

        top_k = []
        # go through the dictionary and find the keys (original numbers) that correspond to these highest counts
        for key in nums_count:
            if len(top_counts) == 0:
                break
            if nums_count[key] == top_counts[-1]:
                top_k.append(key)
                top_counts.pop()

        return top_k
