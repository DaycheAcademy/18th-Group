print('=' * 40)
# ======================================

for num in range(2, 50):
    for i in range(2, num // 2 + 1):
        if not num % i:
            break
    else:
        print(num)