import os
from modules.tools import get_args
from modules.tools import read_text_file, mywalk, path_concatenate, get_cmdw


current_root = ""
def file_search(root_path, key, void_dirs, search_depth, letter_dis):
    global current_root
    current_root = root_path

    if letter_dis is False:
        key = key.lower()

    matched_file_names = []
    matched_folder_names = []
    if root_path not in void_dirs:
        root, folder_names, file_names = mywalk(root_path)
        for file_name in file_names:
            file_addr = "/".join(root.split("/")) + "/" + file_name
            s = read_text_file(file_addr)
            if letter_dis is False:
                s = s.lower()
            if (key in s) or (key in file_name):
                matched_file_names.append(file_addr)
        for folder_name in folder_names:
            folder_path = root + "/" + folder_name
            # Folder name check
            if key in folder_name:
                matched_folder_names.append(folder_path)
            # Recurrent
            if search_depth > 0:
                sub_file_names, sub_folder_names = file_search(folder_path, key, void_dirs, search_depth-1, letter_dis)
                matched_file_names += sub_file_names
                matched_folder_names += sub_folder_names
    return matched_file_names, matched_folder_names


if __name__=="__main__":
    args = get_args()
    root_path = args.dir
    content_key = args.key
    root_only = args.root_only
    void_sub_dirs = args.void_sub_dirs
    lett_dis = args.lett_dis

    assert os.path.exists(root_path), "Provided root does not exist!"

    void_roots = [path_concatenate(root_path, void_sub_dir) for void_sub_dir in void_sub_dirs]
    void_roots = sorted(void_roots, key=lambda pth: pth.lower())
    
    search_depth = 2048 if root_only is False else 0
    try:
        matched_file_names, matched_folder_names = file_search(root_path, content_key, void_roots, search_depth, lett_dis)
    except KeyboardInterrupt:
        raise KeyboardInterrupt(f"Interrupted at \"{current_root}\".")

    # Print files
    print()
    print("="*11 + " Results =" + "="*(get_cmdw()-21))
    print(f"Root path = {root_path}")
    l_root = len(root_path)
    if matched_file_names != []:
        print(f"\033[4mHere are the files containing \"{content_key}\":\033[0m")
        for i, file_name in enumerate(matched_file_names, start=1):
            print("   \033[1;90m", i, "\033[0m\t", file_name[l_root:], sep="")
    else:
        print(f"\033[91mNo file contains \"{content_key}\".\033[0m")

    # Print folders
    if matched_folder_names != []:
        print(f"\033[4mHere are the folders with name having \"{content_key}\":\033[0m")
        for i, folder_name in enumerate(matched_folder_names, start=1):
            print("   \033[1;90m", i, "\033[0m\t", folder_name[l_root:], sep="")
    else:
        print(f"\033[91mNo folder name contains \"{content_key}\".\033[0m")

    print("="*get_cmdw())
