# remove-duplicates-from-sorted-array
Removes duplicates from a sorted array in-place using the two-pointer technique, achieving O(n) time and O(1) space complexity.

Approach:
Maintain two pointers:
i → position of last unique element
j → traversal pointer
When a new unique element is found, move i forward and update it.

Time Complexity:
O(n)

Space Complexity:
O(1) (in-place modification)
