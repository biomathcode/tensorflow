
def toString(List):
    return ''.join(List)
def permute(a, l, r):

    # a = list of the string letters
    # l = Starting index of the string
    # r = ending index of the string
    if l==r:
        print(toString(a))
    else:

        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)

            a[l], a[i] = a[i], a[l] #backtracking
string = input("please write the string here: ")


n = len(string)
Count = str.count(string, '')
a = list(string)
print(Count)
permute(a, 0, n-1)