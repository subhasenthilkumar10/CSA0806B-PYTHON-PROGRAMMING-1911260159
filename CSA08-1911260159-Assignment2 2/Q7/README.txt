Q7 redesign plan
Selected program: Q6 plain recursive staircase counter.

A. Diagnosis: the original function calls itself twice for most inputs and
repeats the same subproblems. The number of calls grows exponentially.
B. Objective: calculate the same answer for n=30 with far fewer operations.
C. Redesign: keep only the previous two answers and update them in a loop.
This uses the recurrence but avoids repeated subproblems. It needs O(1)
extra variables and has O(n) time.
D. Prediction: the redesigned version will use n-1 loop iterations rather
than hundreds of thousands of recursive calls for n=30.
E. Validation: run q7_redesign.py; it prints both answers, counts and times.
F. Defence: the loop is preferable for larger n because it is efficient
and avoids recursion depth. The recursive version is shorter and useful
for learning the recurrence, but not suitable for large inputs.
Use the actual times printed on your computer in the final report.
