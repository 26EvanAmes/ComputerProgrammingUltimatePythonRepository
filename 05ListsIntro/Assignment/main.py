def make_abc():
    return["a", "b", "c"]
print("Demonstrate make_abc:")
print(make_abc())

def equal_edges(list1):
    if list1[0] == list1[-1]:
        return True
    else:
        return False
print("Demonstrate equal_edges:")
print("[1, 2, 3, 4, 1] => ", equal_edges([1, 2, 3, 4, 1]))
print("[5, 6, 7, 8, 9] => ", equal_edges([5, 6, 7, 8, 9]))
print("[-1, 0, 1, 2, -1] => ", equal_edges([-1, 0, 1, 2, -1]))
print("[4, 4] => ", equal_edges([4, 4]))

def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[-1]
    last2 = list2[-1]
    if first1 == first2 or first1 == last2:
        return True
    if last1 == first2 or last1 == last2:
        return True
    else:
        return False
print("Demonstrate common_edge:")
print("[1, 2, 3, 4] & [5, 6, 7, 8] =>", common_edge([1, 2, 3, 4],[5, 6, 7, 8]))
print("[1, 2, 3] & [3, 4, 5] =>", common_edge([1, 2, 3],[3, 4, 5]))
print("[4, 5, 6] & [7, 8, 9] =>", common_edge([4, 5, 6],[7, 8, 9]))
print("[-1, 0, 1, 2, -1] & [2, 3, 4, 5] =>", common_edge([-1, 0, 1, 2, -1],[2, 3, 4, 5]))
print("[3, 3, 3] & [3, 3, 3] =>", common_edge([3, 3, 3],[3, 3, 3]))

def all_the_same(items):
    if items[0] == items[1] and items[1] == items[2] and items[0] == items[2]:
        return True
    else:
        return False
print("Demonstrate all_the_same:")
print("[1, 2, 3] =>", all_the_same([1, 2, 3]))
print("[5, 5, 5] =>", all_the_same([5, 5, 5]))
print("[-1, 0, 1] =>", all_the_same([-1, 0, 1]))
print("[3, 3, 3] =>", all_the_same([3, 3, 3]))
print("[4, 5, 6] =>", all_the_same([4, 5, 6]))

def all_unique(items):
    if items[0] == items[1] or items[0] == items[2] or items[1] == items[2]:
        return False
    else:
        return True
print("Demonstrate all_unique:")
print("[1, 2, 3] =>", all_unique([1, 2, 3]))
print("[5, 5, 5] =>", all_unique([5, 5, 5]))
print("[-1, 0, 1] =>", all_unique([-1, 0, 1]))
print("[3, 3, 3] =>", all_unique([3, 3, 3]))
print("[4, 5, 6] =>", all_unique([4, 5, 6]))

def increasing(items):
    if items[0] == items[1]+1 and items[1] == items[2]+1:
        return True
    else:
        return False
print("Demonstrate increasing:")
print("[1, 2, 3] =>", increasing([1, 2, 3]))
print("[5, 5, 5] =>", increasing([5, 5, 5]))
print("[-1, 0, 1] =>", increasing([-1, 0, 1]))
print("[3, 3, 3] =>", increasing([3, 3, 3]))
print("[4, 5, 6] =>", increasing([4, 5, 6]))

def all_true(items):
    if items[0] == True and items[0] == items[1] == items[2]:
        return True
    if items[1] == True and items[0] == items[1] == items[2]:
        return True
    if items[2] == True and items[0] == items[1] == items[2]:
        return True
    else:
        return False
print("demonstrate all_true:")
print("[True, False, True] =>", all_true([True, False, True]))
print("[False, False, False] =>", all_true([False, False, False]))
print("[True, True, True] =>", all_true([True, True, True]))
print("[False, True, False] =>", all_true([False, True, False]))
print("[True, False, False] =>", all_true([True, False, False]))