def tip_amt(amt , tip):
    tips = amt * tip /100
    total_amt = amt+tips
    print("your total amt  bill is",total_amt)
    print("your tip is",tips)
tip_amt(2000,6)