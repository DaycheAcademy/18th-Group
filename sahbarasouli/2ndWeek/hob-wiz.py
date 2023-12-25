
for number1 in range(1,101):
    # res='hobviz'if not number1 %15 else ('hob'if not number1 %5 else ('viz'if not number1 %3 else number1) )
    res='hopviz'if not number1 %15 else 'hob'if not number1 %3 else 'viz'if not number1 %5 else number1
    print(res)
