list1 = ["ыоар", "хзрпо", "фйкегнуй"]
list2 = [111, 456, 757]


def merge_list_to_dict(a=list1, b=list2):
    q = zip(a, b)
    di = dict(q)
    return di


print(merge_list_to_dict())
print(merge_list_to_dict(["dsfsd"], b=[112]))
