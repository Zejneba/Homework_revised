ht=int  # high tariff
lt=int	# low tariff
cat=int	# category social group or comercial
def total(ht,lt,cat):
    if (cat == 1):
            amount = 0
            surcharge = 0	# if it is socal group, no charge
    elif (cat == 2):		# if it is comercial, different surcharges apply
            a = 5
            if(ht < lt):
                amount = ht+lt+a
                surcharge = 0
            elif(ht > lt):
                amount = ht + lt+ a
                surcharge = 10
            else :
                amount = ht+lt+a
                surcharge = 5
    total = amount + surcharge
    return total
    
