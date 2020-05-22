def main():
    user = "junyiacademy"
    user = f(user)
    print(user)
def f(str): # str is a string which user input
    answer = ''
    for ch in str:
        answer = ch + answer  # appending char in reverse order
    return answer
main()