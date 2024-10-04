# Top K Frequent Elements

# Worst Case O(nlogn) if every num in nums occurs once and we sort the top counts
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # of the form {key:count} where key is the original number
        nums_count = dict()
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1

        # take the top k counts by sorting and add the corresponding keys to the list
        return [x for x, y in sorted(
            nums_count.items(), key=lambda item: item[1])][-k:]
