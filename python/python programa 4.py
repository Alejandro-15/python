def array_diff(a,b):
        for i in range(len(b)):
            while b[i] in a:
                a.remove(b[i])
        return a
def array_diff1(a,b):
        return [i for i in a if i not in b]

print(array_diff([1,2,3,4,5],[3]))
print(array_diff1([1,2,3,4],[2]))


 
