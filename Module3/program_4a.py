import urllib.request
global text


class RemoveHtmlTags:
    # We make a method static, when we need some functionality not w.r.t an Object but w.r.t the complete class,
    # Static method is bound to a class rather than the objects for that class
    # In a static method, we don’t need the 'self' to be passed as the first argument.
    @staticmethod
    def get_data_from_url():
        # fetching data from web page (using google website here)
        u = urllib.request.urlopen("https://www.google.co.in/")
        global text
        text = u.read()
        # This is of type 'bytes', so we cannot apply string functions on this { ex- replace(), strip() }
        print(type(text))
        print("Original data with HTML tags: ", text)

    @staticmethod
    def remove_tags_from_url_data():
        print("===================")
        # Converting 'bytes' into 'string' type
        string_data = str(text)
        print(type(string_data))
        # Removing left angle bracket and replacing it with empty strings
        left_angle_bracket = string_data.replace('<', " ")
        # Removing right angle bracket and replacing it with empty strings
        right_angle_bracket = left_angle_bracket.replace('>', " ")
        final_data = right_angle_bracket
        print("Data after removing HTML tags: ", final_data)


# Calling directly with class name, no need to create object of that class
RemoveHtmlTags.get_data_from_url()
RemoveHtmlTags.remove_tags_from_url_data()