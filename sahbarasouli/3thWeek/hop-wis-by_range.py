for num in range(0,101):
    result='hopwis' if num in range(0,101,15) else ('hop'if num in range(0,101,5) else ('wis'if num in range(0,101,3) else num))
    print(result)

