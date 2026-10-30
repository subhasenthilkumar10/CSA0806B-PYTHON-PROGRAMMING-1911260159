Q3 notes
Predictions:
tn 09 ab 1234 -> TN09AB1234, valid
KA-01-M-0007 -> KA01M0007, valid
Tn09Ab1234 -> TN09AB1234, valid
TN9AB1234 -> TN9AB1234, invalid
TN 22 1234 AB -> TN221234AB, invalid
KL 07 C 4567 -> KL07C4567, valid

Strings are immutable, which means their characters cannot be changed in
place. text.upper() returns a new uppercase string; it does not change text.
For a 9-character registration, s[-4:] returns the final four characters
and s[4:-4] returns one character. For a 10-character registration,
s[-4:] still returns the final four characters and s[4:-4] returns two
characters. Validation takes O(L) time and O(L) extra space for the
normalised string. A regular expression fullmatch also scans O(L) characters
and is compact, but slicing makes each required field visible to beginners.
