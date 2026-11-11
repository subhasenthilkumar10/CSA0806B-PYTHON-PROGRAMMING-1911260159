"""A separate script showing how the milkrate module is imported."""
import milkrate as mr

print("Imported module test:")
print("Rate:", mr.rate_per_litre(4.2, 8.7))
print("Payment:", mr.payout(8.5, 4.2, 8.7))
