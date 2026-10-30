Q6 notes
Base case: n <= 1 returns 1. Recursive case: ways(n) = ways(n-1) +
ways(n-2). The plain recursive version recalculates the same smaller
staircase values many times. For n=5, the call tree begins:
ways(5)
  ways(4) -> ways(3), ways(2)
  ways(3) -> ways(2), ways(1)
and repeated ways(3), ways(2), and ways(1) calls occur.

Memoisation stores a result the first time a value is calculated. The
expected answers for n=1..6 are 1, 2, 3, 5, 8, 13. Plain recursion takes
O(phi^n) time and O(n) stack space. Memoisation takes O(n) time and O(n)
cache plus stack space. The loop takes O(n) time and O(1) extra space.
A recursive memoised call for n=1000 may exceed Python's recursion limit
(usually around 1000); the loop is safer for this input. Do not raise the
limit without care because very deep recursion can exhaust the call stack.
