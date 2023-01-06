# 1. Content Searcher

This program can search keyword in files under a directory (currently only supports ASCII).

This program requires python3.

# 2. Usage
## 2.1. Using Command Line
Parameters:
```
0.  -h, --help              Show help message and exit.
  
1.  --use_config            Use "config.yaml", ignore command line args.

2.  -d, --dir               Search path directory.
3.  -k, --key               Keyword to lookup.
4.  --root_only             Only lookup root files.
5.  -v, --void_sub_dirs     Directories not to scan.
6.  --show_details          Show the line where keyword occurs in the folder. (not
                            implemented yet...)
7.  -l, --lett_dis          Discriminates lower/upper letters

```
Example command:
```
python3 content_searcher.py \
    -d /projects/project/ \
    -k roi_heads \
    -v build \
       datasets \
       output \
       venv
```

## 2.2. Using Config File
Parameters and example:
```
# Search path directory.
directory: /projects/project/

# Keyword to lookup.
key: roi_heads

# Only lookup at root
root_only: false

# Directories not to scan
dirs_ignore: [build, datasets, datasets, output, venv]

# Show the line where keyword occurs in the folder. (not implemented yet...)
show_details: false

# Discriminates lower/upper letters
discriminate_letter_case: false
```
Then run command:
```
python3 content_searcher.py --use_config
```

# 3. Sample Output
Found case:
```
=========== Results =======================================
Root path = /projects/project
Here are the files containing "roi_heads":
   1	/AdelaiDet.egg-info/SOURCES.txt
   2	/adet/modeling/__init__.py
   3	/adet/modeling/domain_shift_modules/meta_arch.py
   4	/adet/modeling/explainer/rcnn_heads_explainer.py
Here are the folders with name having "roi_heads":
   1	/adet/modeling/roi_heads
===========================================================
```
Not found case:
```
=========== Results =======================================
Root path = /projects/project
No file contains "sadsjadsn".
No folder name contains "sadsjadsn".
===========================================================
```

# Future Work
- Implement feature "Show the line where keyword occurs in the folder".
- GUI version.
