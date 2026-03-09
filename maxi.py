def maxi(a,b,c):
    if a>b and a>c:
        maxx=a
    elif b>a and b>c:
        maxx=b
    else:
        maxx=c
    return maxx
new=maxi(17,16,14)
print(f"{new} is larger")