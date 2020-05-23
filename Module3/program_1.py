class IteratorReverse:
    def my_reverse_list(self, list_items):
        print("Original List Items in Normal direction:")
        for x in list_items:
            print(x)
        print("=====================")
        rev_list = list_items[::-1]
        iter_object = iter(rev_list)
        print(iter_object)
        print("Iterator List Items in Reverse direction:")
        for item in iter_object:
            print(item)


list_items = [2, 4, 6, 8, 10]
it = IteratorReverse()
it.my_reverse_list(list_items)