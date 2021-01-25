score = input("Enter score:")
try:
    sc = float(score)
except:
    print("Insert a numeric input between 0.0 and 1.0")
    quit()
if sc >= 0.9 and sc <= 1.0 :
    print("A")
elif sc >= 0.8 and sc <= 1.0 :
    print("B")
elif sc >= 0.7 and sc <= 1.0 :
    print("C")
elif sc >= 0.6 and sc <= 1.0 :
    print("D")
elif sc < 0.6 and sc >= 0.0 :
    print("F")
else :
    print("Insert a numeric input between 0.0 and 1.0")
