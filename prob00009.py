for a in range(1000):
    for b in range(1000):
        if a+b+(a*a+b*b)**0.5==1000:
            print(a*b*((a*a+b*b)**0.5))
            break