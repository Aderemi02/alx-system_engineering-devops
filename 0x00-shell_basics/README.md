This file gives an explicit description of each of the script in the file.

1. 	The first script: current working directory
 	- pwd: This script is used to write out the path of the present working directory

2.	The second script: to list the content in current directory
	- ls: this is used in listing the content of the current working directory

3.	The third script: to move to the home directory
	- cd \: this is used to move from the current directory to the home directory

4.	The fourth script: to list files in long format
	- ls -l: this is used in listing content in a directory in a long list format

5.	The fifth script: to list hidden files
	- ls -la: this is used to list hidden files with the . in a long list format

6.	The sixth script: to list thr user and group ID in numbers
	- ls -la -n: thisi is used to list the content of a directory with the user and group ID in numbers

7.	The seventh script: to make a new directory in tmp
	- mkdir /tmp/my_first_directory: this is used to make a new directory in tmp.

8.	The eighth script: moving file into different foldeers
	- mv ./betty /tmp/my_first_directory: this is used to move your folder between folders.

9.	The nineth script: Deleting a file
	- rm /tmp/my_first_directory/betty: this is used to delete the file in the directory.

10. 	The tenth script: Deleting a folder
	- rm -r: this is used in deleting a folder from a directory

11.	The eleventh script: moving from a directory one step back
	- cd -: This is used to move to the prevous directory.

12.	The twelveth script: listing files is different directories
	- ls . .. /boot -la: this is used to list files in current directory, parent directory and boot directory

13.	The thirteenth script: listing the file type
	- file tmp/iamafile: this is used to identify the type of file a particular file is.

14.	The fourteenth script: creating a symbolic link
	- ln --symbolic -T /bin/ls _ls_: this is used to create a symbolic link(_ls_) to /bin/ls

15.	The fifteenth script: copying all files from ond directory to another
	- cp *.html ..: this is used to copy all .html extension to the parent directory
