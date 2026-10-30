Q2 notes
The while version is natural when the number of counted attempts is controlled
by a condition and blank entries must not consume an attempt. The for version
is convenient when there is a fixed maximum of three attempts.

The counter is increased only after a non-blank entry. If it is increased
before checking for a blank entry, blank input incorrectly uses an attempt.
If it is never increased after a wrong answer, the loop may continue forever.

break exits after a correct OTP. continue skips the rest of the current
iteration for a blank entry. pass is a no-operation placeholder shown in the
security-question branch. The loop-else runs only when the loop finishes
without break, so it displays the lock message after all attempts fail.

For the changed rule, use 5 attempts when the security answer is correct,
otherwise 3. A recursive version calls itself for the next counted attempt.
For a attempts, both loops and recursion take O(a) time. A loop uses O(1)
extra space; recursion uses O(a) call-stack space.
