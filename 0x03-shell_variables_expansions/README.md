# Shell - Init Files, Variables, & Expansions

Commands covered
* `printenv`
* `set`
* `unset`
* `export`
* `alias`
* `unalias`
* `.`
* `source`
* `printf`


## Learning Objectives:
### 1. General
- What happens when you type `$ ls -l *.txt`

### 2. Shell Initialization Files
- What are the `/etc/profile` file and the `/etc/profile.d` directory
- What is the `~/.bashrc` file

### 3. Variables
- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles of the following reserved variables: HOME, PATH, PS1
- What are special parameters
- What is the special parameter `$?`?

### 4. Expansions
- What is expansion and how to use them
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with `$()` and backticks

### 5. Shell Arithmetic
- How to perform arithmetic operations with the shell

### 6. The `alias` Command
- How to create an alias
- How to list aliases
- How to temporarily disable an alias

### 7. Other `help` pages
- How to execute commands from a file in the current shell

## Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l` file should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use `&&`, `||` or `;`
- You are not allowed to use bc, `sed` or `awk`
- All your files must be executable

### More Info
Read your `/etc/profile`, `/etc/inputrc` and `~/.bashrc` files.

Look at some files in the `/etc/profile.d` directory.

**Note:** You do not have to learn about `awk`, `tar`, `bzip2`, `date`, `scp`, `ulimit`, `umask`, or shell scripting, yet.

## Project Tasks
### 0. \<o>
**Description:** Create a script that creates an alias.
- Name: `ls`
- Value: `rm *`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `0-alias` <br>

### 1. Hello you
**Description:** Create a script that prints `hello user`, where user is the current Linux user.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `1-hello_you` <br>

### 2. The path to success is to take massive, determined action
**Description:** Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `2-path` <br>

### 3. If the path be beautiful, let us not ask where it leads
**Description:** Create a script that counts the number of directories in the `PATH`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `3-paths` <br>

### 4. Global variables
**Description:** Create a script that lists environment variables.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `4-global_variables` <br>

### 5. Local variables
**Description:** Create a script that lists all local variables and environment variables, and functions.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `5-local_variables` <br>

### 6. Local variable
**Description:** Create a script that creates a new local variable.
- Name: `BEST`
- Value: `School`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `6-create_local_variable` <br>

### 7. Global variable
**Description:** Create a script that creates a new global variable.
- Name: `BEST`
- Value: `School`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `7-create_global_variable` <br>

### 8. Every addition to true knowledge is an addition to human power
**Description:** Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `8-true_knowledge` <br>

### 9. Divide and rule
**Description:** Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
- `POWER` and `DIVIDE` are environment variables

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `9-divide_and_rule` <br>

### 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
**Description:** Write a script that displays the result of `BREATH` to the power `LOVE`
- `BREATH` and `LOVE` are environment variables
- The script should display the result, followed by a new line

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `10-love_exponent_breath` <br>

### 11. There are 10 types of people in the world -- Those who understand binary, and those who don't
**Description:** Write a script that converts a number from base 2 to base 10.
- The number in base 2 is stored in the environment variable `BINARY`
- The script should display the number in base 10, followed by a new line

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `11-binary_to_decimal` <br>

### 12. Combination
**Description:** Create a script that prints all possible combinations of two letters, except `oo`.
- Letters are lower cases, from `a` to `z`
- One combination per line
- The output should be alpha ordered, starting with `aa`
- Do not print `oo`
- Your script file should contain maximum 64 characters

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `12-combinations` <br>

### 13. Floats
**Description:** Write a script that prints a number with two decimal places, followed by a new line. <br>
The number will be stored in the environment variable `NUM`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `13-print_float` <br>

### 14. Decimal to Hexadecimal (advanced task)
**Description:** Write a script that converts a number from base 10 to base 16.
- The number in base 10 is stored in the environment variable `DECIMAL`
- The script should display the number in base 16, followed by a new line

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `100-decimal_to_hexadecimal` <br>

### 15. Everyone is a proponent of strong encryption (advanced task)
**Description:** Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `101-rot13` <br>

### 16. The eggs of the brood need to be an odd number (advanced task)
**Description:** Write a script that prints every other line from the input, starting with the first line.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `102-odd` <br>

### 17. I'm an instant star. Just add water and stir. (advanced task)
**Description:** Write a shell script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result.
- `WATER` is in base `water`.
- `STIR` is in base `stir`.
- The result should be in base `bestchol`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x03-shell_variables_expansions` <br>
File: `103-water_and_stir` <br>
