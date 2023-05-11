# 0x01-shell_permissions

This directory contains shell scripts related to file and directory permissions.

## Files

### 0-iam_betty
- Script that switches the current user to the user "betty".
- Usage: `./0-iam_betty`

### 1-who_am_i
- Script that prints the effective username of the current user.
- Usage: `./1-who_am_i`

### 2-groups
- Script that prints all the groups the current user is part of.
- Usage: `./2-groups`

### 3-new_owner
- Script that changes the owner of the file "hello" to the user "betty".
- Usage: `sudo ./3-new_owner`

### 4-empty
- Script that creates an empty file called "hello".
- Usage: `./4-empty`

### 5-execute
- Script that adds execute permission to the owner of the file "hello".
- Usage: `./5-execute`

### 6-multiple_permissions
- Script that adds execute permission to the owner and the group owner, and read permission to other users, to the file "hello".
- Usage: `./6-multiple_permissions`

### 7-everybody
- Script that adds execution permission to the owner, the group owner, and other users, to the file "hello".
- Usage: `./7-everybody`

### 8-James_Bond
- Script that sets the permission to the file "hello" as follows: Owner has no permission, group has no permission, and other users have all permissions.
- Usage: `./8-James_Bond`

### 9-John_Doe
- Script that sets the mode of the file "hello" to "-rwxr-x-wx".
- Usage: `./9-John_Doe`

### 10-mirror_permissions
- Script that sets the mode of the file "hello" the same as the mode of "olleh".
- Usage: `./10-mirror_permissions`

### 11-directories_permissions
- Script that adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users.
- Usage: `./11-directories_permissions`

### 12-directory_permissions
- Script that creates a directory called "my_dir" with permissions "751" in the working directory.
- Usage: `./12-directory_permissions`

### 13-change_group
- Script that changes the group owner of the file "hello" to "school".
- Usage: `sudo ./13-change_group`

### 100-change_owner_and_group
- [Advanced] Script that changes the owner to "vincent" and the group owner to "staff" for all files and directories in the working directory.
- Usage: `sudo ./100-change_owner_and_group`

## Repository Information

GitHub repository: [alx-system_engineering-devops](https://github.com/GideonBature/alx-system_engineering-devops)
Directory: 0x01-shell_permissions


