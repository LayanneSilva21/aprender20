from decimal import Decimal

total = Deciaml ('0')

def dec(element, index):
    try:
        return Decimal(element[index])
    except:
        return Decimal('0')
