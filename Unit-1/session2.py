def convertTemp(celsius):
    ans = []
    k = round(celsius + 273.15, 2)
    f = round(celsius * 1.80 + 32.00, 2)
    ans.append(k)
    ans.append(f)
    return (ans)

temp = convertTemp(23.00)
print(temp)