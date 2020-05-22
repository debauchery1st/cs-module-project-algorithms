'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(lst):
    single = None
    listed = {}
    for i in lst:
        j = listed.get(str(i)) or 0
        listed[str(i)] = j + 1
    for k in listed.keys():
        if listed[k] == 1:
            single = int(k)
            break
    return single


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
