#Program sorts numbers from smallest to biggest
#First create the numbers1.txt file, append it then use input to write numbers in it
list_1 = [3, 6, 12, 21]
list_2 = [4, 11, 18, 34]
both_lists = []

with open('numbers1.txt', 'a') as first_nums:
        first_nums.write(str(list_1))
        print(list_1)

with open('numbers2.txt', 'a') as second_nums:
        second_nums.write(str(list_2))
        print(str(list_2))

with open('all_numbers.txt', 'a') as combined:
    both_lists = list_1 + list_2
    both_lists.sort()
    combined.write(str(both_lists))
    print(str(both_lists))
