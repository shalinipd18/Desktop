
def total_calc(bill_amount, tip_perc):
    tip = bill_amount * tip_perc / 100
    total = bill_amount + tip
    total = round(total, 2)
    print(f"Please pay ${total}")

total_calc(150, 20)
