def generateParenthesis(left, right, s, answer):
    if left == 0 and right == 0:
        answer.append(s)
    if left > right or left < 0 or right < 0:
        return
    s += '('
    generateParenthesis(left - 1, right, s, answer)
    s = s[:-1]
    s += ')'
    generateParenthesis(left, right - 1, s, answer)
    s = s[:-1]
n = int(input('enter the number of cobinations: '))
ans = []
s = ""
my_list = []
generateParenthesis(n, n, s, ans)
for k in ans:
        my_list.append(k)

print(my_list)
