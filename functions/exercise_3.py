def make_full_name(first,last, middle=""):
    if (middle==""):
        return(first+last)
    else:
        return(first+middle+last)
first_last = make_full_name("Yashus ", "Rao")
first_middle_last = make_full_name("Yashus ","Sham ","Rao")
first_last_middle = make_full_name("Yashus ","Rao ","Sham")
print(first_last)
print(first_middle_last)
print(first_last_middle)