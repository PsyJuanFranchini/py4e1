text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(":")
number = text[ipos + 5:]
#print(number)
value = float(number)
print(value)
