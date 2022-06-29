"""Script with functions."""

def get_text(source):
    """Save text data in list."""
    #filling_file = []
    with open(source, "r") as txt_file:
        filling_file = txt_file.readlines()
    return filling_file

def line_in_dict(line):
    """Put one line into 1 dict."""
    one_oject = {
        "number":"",
        "data":"",
        "locality":"",
        "steet":"",
        "build":"",
        "flat":"",
        "feature":"",
        "customer":"",
    }

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
            #replace("|","_").
            replace(":","_").
            replace("*","_").
            replace("?","_").
            replace('"',"_").
            replace("<","_").
            replace(">","_")
        )
    return raw_1

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
    # Delete prohibited signs from strings.
    semipure_txt = remove_prohibited_signs(raw_info_txt_file_list)