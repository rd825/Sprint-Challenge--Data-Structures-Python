Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?

5) What is the runtime complexity of the provided code in `names.py`?<br/>
   In the provided algorithm, there are two arrays containing 10k names each. We are nesting one for loop inside of the other, iterating over both arrays. Thus, the runtime complexity of the provided algorithm is O(n^2) where n = 10000. <br/><br/>

6) What is the space complexity of the provided code in `names.py`?<br/>
   If we consider the inputs as part of this calculation, we know we will always have 2 arrays of length 10000. This yields O(20000), which we can reduce to constant space complexity O(1). The output of this function is an array `duplicates` which can contain anywhere from 1 duplicate to n duplicates. So we can say that space complexity is O(n) where n can go up to 10000.

7) What is the runtime complexity of your optimized code in `names.py`?<br/>

8) What is the space complexity of your optimized code in `names.py`?<br/>
