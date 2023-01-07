# Intro to Linux 
The "Linux for Robotics" course provided by the Construct. 

## Interesting Info that was learned:
- ROS only fully supports Linux.
- How to see hidden files and what these are.
- How to view permission and set them.
- How to create and execute .bash scripts.
- What a .bashrc file is. What changing it does.
- What Environment variables are.
- What Foreground and Background processes are.
- How to ssh into a machine remotely.
- What the Advanced Packing Tool is. 
- How to use the sudo cmd. 

## Skills that were learned:
1. Linux Shell skills:
- Navigating through and interacting with folders and files on a Linux filesystem.
- Creating, copying, pasting, and deleting folders and files.
- Editing file contents in the "vi" visual editor. The basics.
- Modifying permissions to files.
- Viewing and changing environment variables.
- Starting, pausing and killing foreground and background applications.
2. Other skills:
- Making and executing .bash scripts
- Remotely connecting to a machine. 

## Commands Cheatsheet
Noteworthy commands from this course. For your and my convenience. 
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
- Seeing environment variables AND filtering these. 
    `export | grep <TextToSearchFor>`
    - Note: | grep also works to sort other commmands involving sorting.
- Setting environment variables.
    `export <VariableName>=<NewValue>`
- Visualizing running system processes.
    `htop`
- Visualizing running system processes alternative.
    `ps faux`
- Getting the PID of a process.
    `ps faux | grep <ProcessName>`
    - PID is the 5 digit number to the far left.
- Killing a process via PID
    `kill <PID>`
- Starting a background process.
    `<NormalWaytoExecuteAProgram> &`
    - Note: NEED to kill this via PID. 
- Connecting to a machine remotely
    `ssh <user>@<host> -p <PortValue>`
    - <user> is the account you wish to sign in to.
    - <host> is the machine's IP.
    - <PortValue> is the value of the port the ssh server is hosted on. 
        - Find this by using the `ps faul | grep ssh` command.
- Updating the APT.
    `sudo apt-fet update`
- Becoming a super user. Temporary elevated permissions. 
    `sudo <Command>`
    
## Snapshots and Demonstrations
Snapshots and demonstrations of what I found interesting. 
