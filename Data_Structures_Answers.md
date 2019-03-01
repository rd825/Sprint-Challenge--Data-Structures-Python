Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method? <br/>
   My solution will take O(n) time as it uses a single while loop to manage BST traversal.

4. What is the space complexity of your `breadth_first_for_each` method? <br/>
   My solution adds at most 2 nodes to the queue at each step and pops off 1 node at each step. This leads me to believe that the maximum space my solution could take is 0.5n. Dropping the constant, we should expect this solution to take O(n) space.

5) What is the runtime complexity of the provided code in `names.py`?<br/>
   In the provided algorithm, there are two lists containing 10k names each. We are nesting one for loop inside of the other, iterating over both lists. Thus, the runtime complexity of the provided algorithm is O(n^2) where n = 10000. <br/><br/>

6) What is the space complexity of the provided code in `names.py`?<br/>
   If we consider the inputs as part of this calculation, we know we will always have 2 lists of length 10000. This yields O(20000), which we can reduce to constant space complexity O(1). The output of this function is an list `duplicates` which can contain anywhere from 1 duplicate to n duplicates. So we can say that space complexity is O(n) where n can go up to 10000.

7) What is the runtime complexity of your optimized code in `names.py`?<br/>
   For optimization, I decided to use the Python datatype `set` which is optimized for membership and duplication testing via mathematical operations such as union, intersection, and difference. The intersection method will enable us to grab common values (i.e. dupes) between our two input lists. The time complexity for this operation is, on average, O(min(len(a), len(b)). For us, that min value is 10000, enabling us to reduce our time complexity to constant time.

8. What is the space complexity of your optimized code in `names.py`?<br/>
   The space complexity is similar to the provided code. However, there will now be Set with length 10000 in memory because of the explicit type conversion on line 13. Because this is a fixed value, we can reduce it to O(1). The output `duplicates` will be the same `O(n)` as the above, though the output will be a set rather than a list.
