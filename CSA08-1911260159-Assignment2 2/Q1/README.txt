Q1 notes
Predictions:
H1 (100): Full subsidy
H2 (101, ration card): Partial subsidy
H3 (200, ration card): Partial subsidy
H4 (201, no senior member): No subsidy
H5 (201, senior member): Special subsidy
H6 (150, no ration card): No subsidy
H7 (80): Full subsidy
H8 (200, no ration card): No subsidy

The conditions in this exact rule do not overlap, so the separate-if and
if-elif-else versions should agree. Separate if statements can print more
than one result when a programmer writes overlapping conditions. An
if-elif-else chain stops after the first true branch.

Design choice: use if-elif-else for the main consumption ranges, then a
small nested if for the conditions within a range. For k slabs, a chained
decision takes O(k) worst-case time and O(1) extra space. A match-case
version could match a tuple or use guards, but guards are clearer for ranges.
A lookup list searched in order also takes O(k) time and O(k) space for
the stored rules. The fixed number of household fields uses O(1) space
per decision.
