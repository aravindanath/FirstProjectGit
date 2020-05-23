class RemoveDuplicates:
    def  remove_dupicates(self, string):
        a = string.split()
        # print(s)
        # x = set(s)
        # print(x)
        b = set()
        unique = []
        for x in a:
            if x not in b:
                unique.append(x)
                b.add(x)
        print("Original Items were: ", a)
        print("After removing duplicate items, Unique items were :", unique)
        # print(unique)


input_data = "you are in you super easy are done are super you"
rd = RemoveDuplicates()
rd.remove_dupicates(input_data)
