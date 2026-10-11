from business_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)

# add sample inputs
price, gty = 450.00, 3

total = calculate_total(price, gty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)  # 10% discount

print(f"Total cost: ${total:.2f}")
print(f"Requires review: {review}")
print(f"Approval tier: {tier}")
print(f"10% discount: ${discounted_price:.2f}")
