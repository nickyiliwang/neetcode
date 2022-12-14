from collections import defaultdict
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Solution TimeComplexity: O(m * n * 26) => O(m * n)
# m is the number of items in the list, n is the letters in each string

def groupAnagrams(strs):
    # res = {}  # mapping chatCount to list of anagrams
    # it is initialized with a function (“default factory”) that:
    # takes no arguments and provides the default value for a nonexistent key.
    # Defining a dictionary with key pair as a list => defaultdict(list)
    res = defaultdict(list)

    for s in strs:
        # only works for List ds, not dicts
        count = [0] * 26  # a ... z
        for c in s:
            # a 97 97 0 => find the index 0
            print(c, ord(c), ord("a"), ord(c) - ord("a"))

            # e 101 97 4 => find the index 4 and tune it to 1
            count[ord(c) - ord("a")] += 1

        # tuple is immutable sequence so we can use it as a key in dic
        # we are grouping all of the values belonging to the same character count group
        # (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate']
        res[tuple(count)].append(s)

    return res.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Notes
# 1. Tried to use ana = [] to get all occurence during the first pass
# 2. realized I might need an hashMap { x: [0,1,2] } a record of each repeated word: [index]
# 3. with this hashMap I'm still using a nested for loop, relative O(n^2) which is slow

# Leetcode cheating solution with sorted():
# def groupAnagrams(strs):
#     # res = {}  # mapping chatCount to list of anagrams
#     # it is initialized with a function (“default factory”) that:
#     # takes no arguments and provides the default value for a nonexistent key.
#     # Defining a dictionary with key pair as a list => defaultdict(list)
#     res = defaultdict(list)
#     for s in strs:
#         print(sorted(s))
#         # tuple is immutable sequence so we can use it as a key in dic
#         # we are grouping all of the values belonging to the same character count group
#         # ('a', 'e', 't'): ['eat', 'tea', 'ate']
#         res[tuple(sorted(s))].append(s)
#         print(res)
#     return res.values()

# My solution with sorting
# nlogn is the sorting
# O(m * nlogn)
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     # sort first
#     # one pass get val:index in hashMap
#     # compare string
#     hashMap = {}
#     res = []

#     for i, s in enumerate(strs):
#         s = ''.join(sorted(s))
#         if s in hashMap:
#             hashMap[s] += [i]
#         else:
#             hashMap[s] = [i]

#     print(hashMap)

#     for x in hashMap:
#         ana = []
#         for y in hashMap[x]:
#             ana.append(strs[y])
#         res.append(ana)

#     print(res)
#     return res

# Frozen Set

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     res = defaultdict(list)
#     for word in strs:
#         res[frozenset(Counter(word))].append(word)
#     return list(res.values())

# The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.

# Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

# Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).
