year = [82, 89, 88, 66, 85, 00, 99]
print('原列表', year)

for index, value in enumerate(year):
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))
year.sort()
print('新列表', year)
