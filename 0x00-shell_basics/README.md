# Shell - basics

Covers the following commands:
* `cd`
* `ls`
* `pwd`
* `less`
* `file`
* `ln`
* `cp`
* `mv`
* `rm`
* `mkdir`
* `type`
* `which`
* `help`
* `man`

## Learning Objectives:
### 1. General
- What does RTFM mean?
- What is a Shebang

### 2. What is the Shell
- What is the shell
- What is the difference between a terminal and a shell
- What is the shell prompt
- How to use the history (the basics)

### 3. Navigation
- What do the commands or built-ins `cd`, `pwd`, `ls` do
- How to navigate the filesystem
- What are the `.` and `..` directories
- What is the working directory, how to print it and how to change it
- What is the root directory
- What is the home directory, and how to go there
- What is the difference between the root directory and the home directory of the user root
- What are the characteristics of hidden files and how to list them
- What does the command `cd -` do

### 4. Looking Around
- What do the commands `ls`, `less`, `file` do
- How do you use options and arguments with commands
- Understand the ls long format and how to display it
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
- What does the `ln` command do
- What do you find in the most common/important directories
- What is a symbolic link
- What is a hard link
- What is the difference between a hard link and a symbolic link

### 5. Manipulating Files
- What do the commands `cp`, `mv`, `rm`, `mkdir` do
- What are wildcards and how do they work
- How to use wildcards

### 6. Working with Commands
- What do `type`, `which`, `help`, `man` commands do
- What are the different kinds of commands
- What is an alias
- When do you use the command help instead of man

### 7. Reading Man Pages
- How to read a man page
- What are man page sections
- What are the section numbers for User commands, System calls and Library functions

### 8. Keyboard Shortcuts for Bash
- Common shortcuts for Bash

### 9. LTS
- What does `LTS` mean?

## Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789)) 
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we’ll learn more about how to utilize this command.

## Project Tasks
### 0. Where am I?
**Description:** Write a script that prints the absolute path name of the current working directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `0-current_working_directory` <br>

### 1. What’s in there?
**Description:** Display the contents list of your current directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `1-listit` <br>

### 2. There is no place like home
**Description:** Write a script that changes the working directory to the user’s home directory.
- You are not allowed to use any shell variables.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `2-bring_me_home` <br>

### 3. The long format
**Description:** Display current directory contents in a long format.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `3-listfiles` <br>

### 4. Hidden files
**Description:** Display current directory contents, including hidden files (starting with `.`). Use the long format.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `4-listmorefiles` <br>

### 5. I love numbers
**Description:** Display current directory contents.
- Long format
- with user and group IDs displayed numerically
- And hidden files (starting with `.`)

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `5-listfilesdigitonly` <br>

### 6. Welcome
**Description:** Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `6-firstdirectory` <br>

### 7. Betty in my first directory
**Description:** Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `7-movethatfile` <br>

### 8. Bye bye Betty
**Description:** Delete the file `betty`.
- The file `betty` is in `/tmp/my_first_directory`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `8-firstdelete` <br>

### Bye bye My first directory
**Description:** Delete the directory `my_first_directory` that is in the `/tmp` directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `9-firstdirdeletion` <br>

### 10. Back to the future
**Description:** Write a script that changes the working directory to the previous one.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `10-back` <br>

### 11. Lists
**Description:** Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `11-lists` <br>

### 12. File type
**Description:** Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `12-file_type` <br>

### 13. We are symbols, and inhabit symbols
**Description:** Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `13-symbolic_link` <br>

### 14. Copy HTML files
**Description:** Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.  <br>
You can consider that all HTML files have the extension `.html`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `14-copy_html` <br>

### 15. Let’s move (advanced task)
**Description:** Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`. <br>
You can assume that the directory `/tmp/u` will exist when we will run your script.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `100-lets_move` <br>

### 16. Clean Emacs (advanced task)
**Description:** Create a script that deletes all files in the current working directory that end with the character `~`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `101-clean_emacs` <br>

### 17. Tree (advanced task)
**Description:** Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory. <br>
You are only allowed to use two spaces (and lines) in your script, not more.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `102-tree` <br>

### 18. Life is a series of commas, not periods (advanced task)
**Description:** Write a command that lists all the files and directories of the current directory, separated by commas (`,`).
- Directory names should end with a slash (`/`)
- Files and directories starting with a dot (`.`) should be listed
- The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
- Only digits and letters are used to sort; Digits should come first
- You can assume that all the files we will test with will have at least one letter or one digit
- The listing should end with a new line.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `103-commas` <br>

### 19. File type: School (advanced task)
**Description:** Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x00-shell_basics` <br>
File: `school.mgc` <br>
