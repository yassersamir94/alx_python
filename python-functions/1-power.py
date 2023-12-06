def pow(a, b):
    if b == 0:
        return 1
    neg_exponent = False
    
    if b < 0:
        neg_exponent = True
        b = -b
    result = 1
    
    for _ in range(b):
        result *= a
        
    if neg_exponent:
        result = 1 / result
    return result