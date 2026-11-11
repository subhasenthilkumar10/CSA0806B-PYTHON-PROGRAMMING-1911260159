import math

fat = 4.2
snf = 8.7
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = 30.00 + fat_steps * 0.40 + snf_steps * 0.30

print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("round step count =", fat_steps)
print("rate =", round(rate, 2))
print("round(-2.5) =", round(-2.5))
print("int(-2.5) =", int(-2.5))
print("floor(-2.5) =", math.floor(-2.5))
print("Chained check:", 2.0 <= fat <= 7.0)
print("Unexpected: 0.1 + 0.2 =", 0.1 + 0.2)
print("Unexpected: 0.3 == 0.1 + 0.2 =", 0.3 == 0.1 + 0.2)
print("Unexpected: 4.2 - 3.5 =", 4.2 - 3.5)
