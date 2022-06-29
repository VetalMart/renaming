"""Script with functions."""

def get_text(source):
    """Save text data in list."""

    #filling_file = []
    with open(source, "r") as txt_file:
        filling_file = txt_file.readlines()
    return filling_file

def text_in_dict(raw_list):
    """ Make pretty dict, from raw data."""
    # Delete '-' signs
    raw_1 = []
    for i in raw_list:
        # Delete forward and trailing whitespace
        raw_1.append(i.replace("-","").strip().replace(" ",""))
    # Remove empty sells ([...,'',..]) - means. 
    raw_2 = []
    for i in raw_1:
        if i != '':
            raw_2.append(i)
    return raw_2

def remove_prohibited_signs(raw_list):
    # Delete sighs which can't be use in file/folder naming.
    raw_1 = []
    for i in raw_list:
        raw_1.append(
            i.replace("/","_").
            replace("\\","_").
            replace("-","").
            replace(":","_").
            replace("*","_").
            replace("?","_").
            replace('"',"_").
            replace("<","_").
            replace(">","_").
            replace(" ","").
            lstrip()
        )
    return raw_1

def split_sublist(raw_list):
    # Split by sublist
    list_1 = []
    for i in raw_list:
        list_1.append(i.split("|"))
    return list_1

def line_in_dict(work_dict, raw_list):
    """Get item form list and put it in dict."""
    work_dict[raw_list[1]] = "{}_{}_{}_{}_{}_{}_{}".format(
                                raw_list[2], 
                                raw_list[3], 
                                raw_list[4], 
                                raw_list[5], 
                                raw_list[6], 
                                raw_list[7],
                                raw_list[8]
                            )

def rename_file(src_file_folder_list, pure_dict):
    # Rename file in requred way
    excessive_file = []             # list with excessive file
    for i in src_file_folder_list:
        cut_name = i.strip('.pdf')  # number of ask 
        if cut_name in pure_dict:
            new_file_name = "{} {}.pdf".format(cut_name, pure_dict[cut_name])
            # Rename file in proper way
            os.rename(i, new_file_name)
        # List of file which doesn't include in source txt file. 
        else:
            excessive_file.append(i)
    # Show on display excessive file
    for i in excessive_file:
        print(i)


# Exucutes this part if we run this module as executing script
if __name__ == "__main__":
    import os
    
    # Reach required path.
    pwd = input(r"Input working directory: > ")
    # Normalize path for python.
    pwd = os.path.normcase(pwd)
    # Change working dir.
    os.chdir(pwd)
    # Get contain of dir.
    list_file_in_working_dir = os.listdir()
    # Type .txt file with information
    txt_file = input("type source-txt file: > ")
    # Get list with raw text
    raw_info_txt_file_list = get_text(txt_file)
    #print(raw_info_txt_file_list)
    # Delete prohibited signs from strings.
    semipure_txt = remove_prohibited_signs(raw_info_txt_file_list)
    #print(semipure_txt)
    # Splited semipure txt-file
    splited_txt = split_sublist(semipure_txt)
    # Put items from semipure-list into 1 dict
    #print(splited_txt)
    txt_dict_items = {}
    for i in splited_txt:
        # Need remove empty list, and use only full info
        if i != ['']:
            line_in_dict(txt_dict_items, i)
        else:
            pass
    # Rename files and create list which not. 
    rename_file(list_file_in_working_dir, txt_dict_items) 
    
    
