Q4 notes
The script measures repeated +=, list/join, and f-string line creation at
1,000, 10,000 and 200,000 lines. It runs each method three times and prints
the raw times and averages. Use the results from your own computer in the
report because timings depend on the machine and Python version.

Strings are immutable, so repeated concatenation can require new string
objects and copying of earlier characters. In the worst case this can copy
O(n^2) total characters. join first calculates the combined result and
builds it efficiently in O(total characters), with O(total characters)
memory for the final string plus the parts list. Writing to a file or using
io.StringIO avoids keeping one giant final string in memory; it is useful
when output can be streamed or written incrementally.
