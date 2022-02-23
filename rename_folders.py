from pathlib import Path

path = Path.cwd()
print(path)
len_parent = len(str(path).split('\\'))
string_name_for_dirs = digit_locate = index_of_digit = ""
path_prefix = ""

for dirs_ in path.iterdir():
    if dirs_.is_dir():
        string_name_for_dirs = str(dirs_).split('\\')
        digit_locate = string_name_for_dirs[len_parent]
        digit_locate = digit_locate[-5::]

        for i in digit_locate:
            if i in [v for v in "!@#$%^^&*([{"]:
                index_of_digit = digit_locate.index(i)
        if digit_locate[index_of_digit] == "(" or digit_locate[index_of_digit] == "{" or digit_locate[index_of_digit] == "[":
            path_prefix = digit_locate[index_of_digit+1:-1]
        else:
            path_prefix =  digit_locate[index_of_digit+1:]

        dirs_.rename(path_prefix + "." + string_name_for_dirs[len_parent][:-3:])
