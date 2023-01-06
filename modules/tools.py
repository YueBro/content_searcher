import os
import argparse
import yaml


def read_text_file(file_addr):
    try:
        fp = open(file_addr, "r")
        s = fp.read()
        fp.close()
        return s
    except UnicodeDecodeError:
        return ""


def mywalk(root):
    iterator = os.walk(root)
    root_path, files, folders = next(iterator)
    return root_path, files, folders


def path_concatenate(*paths):
    elements = [e for path in paths for e in path.split("/")]
    
    i = 1 if (elements[0] == "") else 0
    I = len(elements)
    while i < I:
        if (elements[i] == ".") or (elements[i] == ""):
            elements.pop(i)
            I -= 1
        elif elements[i] == "..":
            if i > 0:
                elements.pop(i)
                elements.pop(i-1)
                I -= 2
                i -= 1
            else:
                i += 1
        else:
            i += 1
    return "/".join(elements)


def _get_config(config_pth="config.yaml"):
    with open(config_pth, 'r', encoding='utf-8') as fp:
        data = yaml.safe_load(fp)
    
    _temp = dict()
    _temp["dir"] = data["directory"]
    _temp["key"] = data["key"]
    _temp["root_only"] = data["root_only"]
    _temp["void_sub_dirs"] = data["dirs_ignore"]
    _temp["show_details"] = data["show_details"]
    _temp["lett_dis"] = data["discriminate_letter_case"]
    
    return argparse.Namespace(**_temp)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--use_config',
        action="store_true",
        help="Use \"config.yaml\", ignore command line args."
    )
    parser.add_argument(
        "-d", "--dir",
        default=os.getcwd(),
        help="Search path directory."
    )
    parser.add_argument(
        "-k", "--key",
        help="Keyword to lookup."
    )
    parser.add_argument(
        "--root_only",
        action="store_true",
        help="Only lookup root files."
    )
    parser.add_argument(
        "-v", "--void_sub_dirs",
        nargs="+",
        default=[],
        help="Directories not to scan."
    )
    parser.add_argument(
        "--show_details",
        action="store_true",
        help="Show the line where keyword occurs in the folder. (not implemented yet...)"
    )
    parser.add_argument(
        "-l", "--lett_dis",
        action="store_true",
        help="Discriminates lower/upper letters"
    )
    args = parser.parse_args()
    
    if args.use_config is True:
        args = _get_config()
        
    if args.dir[-1] == "/":
        args.dir = args.dir[:-1]
    
    return args


def get_cmdw():
    return os.get_terminal_size().columns


if __name__=="__main__":
    path = path_concatenate("../a/b/c", "./e")
    print(path)
