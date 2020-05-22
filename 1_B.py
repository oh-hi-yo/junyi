def main():
    user = "flipped class room is important"
    user_list = user.split(' ')
    f2(user_list)
    user = f3(user_list)
    print(user)

def f1(str): # str is a string which user input
    answer = ''
    for ch in str:
        answer = ch + answer  # appending char in reverse order
    return answer
def f2(list_a): # reverse single string in list
    for i in range(len(list_a)):
        list_a[i] = f1(list_a[i])
def f3(list_a): # combine every single string in list
    answer = ''
    for str in list_a:
        if str == list_a[0]:
            answer = answer + str
        else:
            answer = answer + ' '+ str 
    return answer
main()