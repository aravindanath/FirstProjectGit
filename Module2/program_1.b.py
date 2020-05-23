import re
class ReplaceOccurrence:
    def replace_occurrence(self):
        # replace all digits(0-9) with '#' pattern symbol
        # syntax :-  re.subn(regex, replacement, target_string)
        replace = re.subn("[0-9]", "#", "nm9k34lb12swe9k6pr5w")
        print(replace)
        print("Original string is : nm9k34lb12swe9k6pr5w")
        print("Result String is :", replace[0])
        print("Number of Replacements :", replace[1])


r = ReplaceOccurrence()
r.replace_occurrence()