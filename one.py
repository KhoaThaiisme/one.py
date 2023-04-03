def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name('john')


def first_odds():
    for i in range(1, 101, 2):
        print i


def max_num_in_list(a_list):
    max_num = a_list[0];
    for num in a_list:
      if num > max_num:
        max_num = num
    return max_num
mylist = [1,2,3,6,8,4]
max = max_num_in_list(mylist)
print(max)


def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2024))


def is_consecutive(a_list):
    for i in range(1, len(a_list)):
        if a_list[i] - a_list[i-1] != 1:
            return False
    return True
num=[1,2,3,4,5,6,7,8]
is_consec = is_consecutive(num)
print(is_consec)

