def palindrome():
    reversedd=""
    for word in letter:
        reversedd=word+reversedd
    if reversedd==letter:
        name=reversedd
    else:
        continue
    return name
letter=input("Enter your letter: ")
new=palindrome()
print(f"{new} is a palindrome")