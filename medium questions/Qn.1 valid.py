strr=input("Enter the String :")
stack=[]
flag=0
for char in strr:
    if char in ['(','{','[']:
        stack.append(char)
    elif char==')' and len(stack)!=0 and stack[-1]=='(':
        stack.pop()
    elif char=='}' and len(stack)!=0 and stack[-1]=='{':
        stack.pop()
    elif char==']' and len(stack)!=0 and stack[-1]=='[':
        stack.pop()
    else:
        flag=1
if(flag==0):
    print("Valid String...")
else:
    print("Invalid String...")
