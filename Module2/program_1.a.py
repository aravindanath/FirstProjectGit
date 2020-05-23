import re
class FirstOccurrence:
    def first_occurrence(self):
        # search() function in 're' module will search for a specific pattern in a given text
        match = re.search("ba", "nfgfngbafdfbaqwaarbammzbapi")
        if match != None:
            print("Match Available")
            print("First occurrence(index) of a search pattern inside a given text is :", match.start(), "==>",
                  "searched pattern is:-", match.group())
        else:
            print("Match not available")


f = FirstOccurrence()
f.first_occurrence()
