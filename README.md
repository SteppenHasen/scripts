# scripts
here will be different small things

## unarchive.py

1. Download **unarchive.py** file

2. for set path were arhives are - change variable "path"

3. for set path were extracted put - change variable "extraction_path"

4. install python:
--- for windows:
------ https://www.python.org/downloads/
--- for *nix:
------ https://docs.python.org/3/using/unix.html

5. run ``` pip install rarfile ``` in command line(terminal, cmd, shell etc.)
--- if you have error like "no such command":
------ check if python is in PATH:
--------- for windows:
------------ in terminal ** Win+R ** run ``` sysdm.cpl ``` and in the Settings window, under Related Settings, click Advanced system settings, on the Advanced tab, click Environment Variables. Look at line named PATH.
--------- for *nix:
------------ ** in terminal ** run ``` echo $PATH ```
------ if you have Python in PATH, reload terminal or what you prefer to use.
------ if you **NOT** add Python in PATH:
--------- for windows:
------------ double click on PATH line and write full path to folder, were Python installed, in new line. Then rerun terminal.
--------- for *nix:
------------ ** in terminal ** run ``` export PATH=$PATH:/path/to/installed/python/folder ```. Then rerun terminal.

6. Run ``` python /path/to/unarchive.py ```
--- if you have error like "no such command" look at 5 paragraph
