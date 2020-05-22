def main():
    user = int(input("Input: "))
    user_list = []
    initialize_list(user_list, user)
    address_list(user_list)
    print("Output: " + str(len(user_list)))

def address_list(a_list):
    copy_of_a_list = a_list[:] # must copy the content of a_list to another variable, otherwise the for loop will do something error.
    for i in copy_of_a_list:
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0 and i % 5 == 0:
                continue
            a_list.remove(i)
        
def initialize_list(a_list, n): # a_list is user_list, and n is length of user_list 
    for i in range(1, n + 1):
        a_list.append(i)

main()