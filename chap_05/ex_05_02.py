total = 0
count = 0

while True:
    sval = input("Enter a number: ")
    if sval == 'Done' or sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Code')
        continue
    # print(fval)
    count = count + 1
    total = total + fval

# print('ALL DONE')
print(total, count, total / count)
