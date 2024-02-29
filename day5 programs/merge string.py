def mergeString(s1:str, s2: str):
    result = []
    len1 = len(s1)
    len2 = len(s2)
    for i in range(max(len1,len2)):
                   if i < len1:
                       result.append(s1[i])
                   if i < len2:
                       result.append(s2[i])
    return "".join(result)
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

s1 = input("enter a string: ")
s2 = input("enter a string: ")
merged = mergeString(s1,s2)
vowels = count_vowels(merged)

print(merged)
print(vowels)
