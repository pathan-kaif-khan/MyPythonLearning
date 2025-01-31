
def rem(l,word):
    n =[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["kaihan","kabir","ayan"]

print(rem(l,"an"))
'''
Issue:
Understanding strip(word)

The strip() method removes all occurrences of the characters in word from both ends of the string, not just the exact substring.
In "ayan", strip("an") removes all occurrences of 'a' and 'n' from both ends.
"ayan" becomes "y" because:
'a' (from the beginning) is removed.
'n' (from the end) is removed.
The remaining "y" is left.
********************************************
"ayan".strip("an")  # Removes 'a' and 'n' from both ends, leaving 'y'
"kaihan".strip("an")  # Removes 'a' and 'n' from both ends, leaving 'kaih'


'''