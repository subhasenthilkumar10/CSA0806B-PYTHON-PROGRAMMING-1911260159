# Assignment 2 Report Guide

For every question, include:
1. Prediction before execution.
2. Program design and explanation.
3. Code and actual output.
4. Analysis of the result.
5. Alternative concept and Big-O time/space comparison.

## Q1
Include the eight-household prediction table and compare the two decisions.
Explain why overlapping independent `if` conditions can produce multiple results.
For this exact set of rules, the unit ranges do not overlap.

## Q2
Run the interactive OTP program with blank, wrong and correct entries.
For the `for` version, uncomment `check_otp_for()` and comment out the while call.
Record how blank entries do not use an attempt.

## Q3
Include all six test inputs, valid/invalid results, and receipt formatting.
Explain immutability and the slices `s[-4:]` and `s[4:-4]`.

## Q4
Run the benchmark three times per method at 1,000, 10,000 and 200,000 items.
The script prints three raw measurements and an average for each method.
Copy your Mac's actual values into the report.

## Q5
Include the output showing the shared buggy default list and the corrected
independent customer lists. In Python the attribute is `__defaults__`
(two underscores on each side), not `.defaults`.

## Q6
Include function-call counts for n=10,20,25,30 and the n=1..6 answers.
Explain why the memoised recursive version may hit the recursion limit at 1000.
Use the loop for a reliable n=1000 result.

## Q7
Use the original and redesigned counts and timings printed by `q7_redesign.py`.
Discuss the operation-count improvement, time, and space trade-off.
