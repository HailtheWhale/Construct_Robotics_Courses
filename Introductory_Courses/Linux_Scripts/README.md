# Intro to Linux 
The "Linux for Robotics" course provided by the Construct. 

## Interesting Info that was learned:
- ROS only fully supports Linux.
- How to see hidden files and what these are.
- How to view permission and set them.
- How to create and exectute .bash scripts.
- What a .bashrc file is. What changing it does.

## Skills that were learned:
1. Linux Shell skills:
- Navigating through and interacting with folders and files on a Linux filesystem.
- Creating, copying, pasting, and deleting folders and files.
- Editing file contents in the "vi" visual editor. The basics.
- Modifying permissions to files.
- Starting, pausing and killing foreground and background applications.
2. Other skills:
- Skill2
- Skill3

## Commands and Script Syntax Cheatsheet
Noteworthy commands and code syntax from this course. For your and my convenience. 
1. Linux Commands 
- Navigating to a given file or folder.
    `cd <FileName_or_PathToFile>`
- Navigating back one folder.
    `cd ..`
- Returning to the path root.
    `cd`
- Printing current working directory.
    `pwd`
- Printing folder contents.
    `ls`   
- Printing folder contents *WITH HIDDEN CONTENTS* and permissions.
    `la -la`    
- Getting info about a command.
    `<CommandName> --help`   
- Getting info about a command alternative.
    `man <CommandName>`
    - Hit "q" to exit.
    - Use UP and DOWN arrow keys to scroll
- Making a folder.
    `mkdir <DesiredFolderName>`   
- Making a file.
    `touch <FileName>`   
- Opening a file in "vi" visual editor. 
    `vi <FileName.Extension>`
    - Switch between "command" and "insert" modes by pressing "i"
    - Go to "insert" mode to write things. Go back to "command" mode to save things.
    - Type `:wq` to *write* what was added to the file and *quit* vi.
    - Type `:q!` to *quit* vi without saving. 
- Moving folders and files around.
    `mv <File_or_Folder_or_DirectoryToThese> <Destination_Directory>`   
- Copying files in the current directory.
    `cp <FileName.Extension> <CopiedFileName.Extension>`   
- Copying folders in the current directory. **DOES NOT work if folders have contents.**
    `cp -r <FolderName> <CopiedFolderName>`
- Deleting files in current directory.
    `rm <FileName.Extension> <CopiedFileName.Extension>`
- Deleting folders in the current directory. **DOES NOT work if folders have contents.**
    `rm -r <FolderName> <CopiedFolderName>`
- Adding perissions to files
    `chmod <GroupToChangePermissions>+/-<Permissions> <NameOfFile.Extension>`
    - <GroupToChangePermissions> can be:
      - u for "owner"
      - g for "group"
      - o for "others"
      - a for "All users"
    - Permissions may be added with "+" and taken away with "-"
    - <Permissions> can be:
      - x for "execute"
      - w for "write"
      - r for "read"
- Changing permissions using binary. 
    `chmod <BinaryCode> <NameOfFile.Extension>`
    - <BinaryCode> is based on the sum of granted permissions. 
      - r = 4
      - w = 2
      - x = 1
    - <BinaryCode> has 3 spaces. Ex: 777. 
      - 1st space = "Owner"
      - 2nd space = "Group"
      - 3rd space = "All users"
- Running .bash scripts
    `./<BashScript.sh>`
- Running .bash scripts
    `./<BashScript.sh>`
- Running .bash scripts
    `./<BashScript.sh>`
    
## Snapshots and Demonstrations
Snapshots and demonstrations of what I found interesting. 
