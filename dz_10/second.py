lst1 = [(1, 2), 5, 5.5, {1}]
lst2 = ["1", 2, 3, 4, 5, 7, 6]
lst3 = [0, 2, "8", 9, True, 66]

def check(x):
    try:
        for i in x:
            i / 2
        unique_list = []
        for i in x:
            if i not in unique_list:
                unique_list.append(i)
        if not isinstance(i, (int, float)) in unique_list or len(x) != len(unique_list):
            print(f"There are some doubling figures in the list {x}")
        else:
            print(f'You always get what you want! {x} list contains unique elements')
    except TypeError:
        unique_list = []
        for i in x:
            if i not in unique_list:
                unique_list.append(i)
        for i in unique_list:
            if isinstance(i, (tuple, set, list, bool, str)):
                print(f"\"{i}\" IS NON-DIGIT TYPE IN THE LIST {x}")
            if isinstance(i, str):
                print(f"WARNING! The string type element \"{i}\" has been converted to integer \"{i}\" in the list {x}")
                index = unique_list.index(i)
                unique_list[index] = int(unique_list[index])
        try:
            i / 2
            if len(x) != len(unique_list):
                print(f"There are some doubling figures in the list {x}, or the list contains other than integer data type")
            else:
                print(f'You always get what you want! {unique_list} list contains unique elements')
        except TypeError:
            if not isinstance(i, (int, float)) in unique_list:
                print(f"Failure to verify the list {unique_list} due to non-digit type of it's elements")
            else:
                print(f'You always get what you want! {x} list contains unique elements')

check(lst1)
check(lst2)
check(lst3)