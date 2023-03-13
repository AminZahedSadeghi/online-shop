number = '12356789'

result = ''
count = 0
for num in reversed(number):
    if count % 3 == 0:
        result += ','
    result += num
    count += 1

print(result)