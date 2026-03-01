dwwadwd = int(input("enter integer: "))

wradd = dwwadwd * 67 * 67
pag = wradd - 612 * 190

def opr(value):
    if value >= 100:
        return wradd
    else:
        return value % (wradd + pag)

print(opr(dwwadwd))