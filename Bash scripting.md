# Bash scripting
This is one of the exciting things I have learned in Linux - Ubuntu

## Task 1
### A bash script to prompt and allow the user to perform basic functions on the terminal

I used the **Nano** editor to write the code. To create/open in Nano from the terminal, run the command

```
nano <filename>

```

Here's the bash script that guides/prompts the user to perform basic file operations.

```
 #!/bin/bash

echo
dir=$(pwd)
echo -e "Your current directory is: $dir "

echo
while true; do
	echo "Select an option [1-9]"
	echo "-----------------------"
	echo "1. Create a new directory"
	echo "2. Delete an existing directory"
	echo "3. List the contents of a directory"
	echo "4. Change into a directory"
	echo "5. Create a new file"
	echo "6. Write to an existing file"
	echo "7. Read from an existing file"
	echo "8. Delete an existing file"
	echo "9. Exit the script."

	read choice

case $choice in
	1)	
		dir=$(pwd)
		echo "Enter the name of the newdirectory:"
		read dirname
		
		if [ -d $dir/$dirname ]
		then
			echo -e "Directory name already exists"
			echo -e "Choose another name"
			echo
		else
			mkdir $dirname
		fi
		;;
	
	2)
		dir=$(pwd)
		echo "Enter the name of the directory to delete:"
		read deldir
		
		if ! [ -d $dir/$deldir ]
		then
			echo -e "Directory do not exist"
			echo
		else
			rm -rf $deldir
			echo
		fi

		if [ $? -eq 0 ]
		then
			echo "Successful"
			echo
		else
			echo "Not Successful"
			echo
		fi
		;;
	
	3)
	
		echo  "Are you in the right directory (y/n): "
		read input	
		
		if [ $input == "n" ]
		then
			echo -e "Change your directory"
			echo
				
		elif [ $input == "y" ]
		then 
		
			ls -l
 			echo
		else 
			
			echo "Wrong choice"
			echo "Enter y or n"
			echo
		fi
		
		
		if [ $? -eq 0 ]
		then
			echo "Successful"
			echo
		else
			echo "Not Successful"
			echo
		fi
		;;
	4)
		dir=$(pwd)
		echo "Enter the name of the directory:"
		read chdir
		if ! [ -d $dir/$chdir ]
		then
			echo -e "Directory do not exist"
			echo -e "Choose another name"
			echo
		else
			cd $chdir
			echo
		fi
		if [ $? -eq 0 ]
		then
			echo Successful
			echo
		else
			echo Not Successful
			echo
		fi
		;;
		
	5)
		dir=$(pwd)
		echo "Are you in the right directory (y/n): "
		read input
	
		if [ $input == "n" ]
		then
			echo -e "Change your directory"
			echo
		elif [ $input == "y" ]
		then 
			echo -e "Enter the new file name"
			read newfile
			if [ -f $dir/$newfile ]
			then
				echo -e "File name already exist"
				echo -e "Choose another name"
				echo
			else
				touch $newfile
				echo
 			fi	
		else 
			
			echo "Wrong choice"
			echo "Enter y or n"
			echo
				
		fi

		if [ $? -eq 0 ]
		then
			echo Successful
			echo
		else
			echo Not Successful
			echo
		fi
		;;
	
	6)
		dir=$(pwd)
		echo "Are you in the right directory (y/n): "
		read input
		echo
	
		if [ $input == "n" ]
		then
			echo -e "Change your directory"
				
		elif [ $input == "y" ]
		then 
			echo -e "Enter the file name"
			read writefile
			if ! [ -f $dir/$writefile ]
			then
				echo -e "File name do not exist"
				echo -e "Choose another name"
				echo
			else
				cat >> $writefile
			fi
				
 		else 
			
			echo "Wrong choice"
			echo "Enter y or n"
			echo	
		fi
		
		if [ $? -eq 0 ]
		then
			echo Successful
			echo
		else
			echo Not Successful
			echo
		fi
		;;
	7)
		dir=$(pwd)
		echo "Are you in the right directory (y/n): "
		read input
		echo
		if [ $input == "n" ]
		then
			echo -e "Change your directory"
		elif [ $input == "y" ]
		then	
			echo "Enter the name of file: "
			read readfile
			if ! [ -f $dir/$readfile ]
			then
				echo -e "File name do not exist"
				echo -e "Choose another name"
				echo
			else
				cat $readfile
			fi
		else
			echo -e "Wrong Choice"
			echo -e "Enter y or n"
		echo
		fi
				
		if [ $? -eq 0 ]
		then
			echo Successful
			echo
		else
			echo Not Successful
			echo
		fi
		;;
	
	8)
		dir=$(pwd)
		echo "Are you in the right directory (y/n): "
		read input
		echo
	
		if [ $input == "n" ]
		then
			echo -e "Change your directory"
		elif [ $input == "y" ]
		then
			echo "Enter the name of file: "
			read delfile
			if ! [ -f $dir/$delfile ]
			then
				echo -e "File name do not exist"
				echo -e "Choose another name"
				echo
			else
				rm $delfile
			fi
		else 
			echo -e "Wrong Choice"
			echo -e "Enter y or n"
			echo
		fi
		
		if [ $? -eq 0 ]
		then
			echo Successful
			echo
		else
			echo Not Successful
			echo
		fi
		;;
	9)
		exit 1
		;;
esac
done
```
## Task 2
Design an interactive menu system using Bash scripting, allowing users to add a new record, edit existing records, search for specific records, and generate reports

The bash script I generated was as follows:
```
#!/bin/bash

# Function to display the menu

display_menu() {
    echo "Menu:"
    echo "1. Add a new record"
    echo "2. Edit an existing record"
    echo "3. Search for a new record"
    echo "4. Generate reports"
    echo "5. Exit"
}

# Function to add a new record
add_record() {
     echo "Enter details for the new record:"
     read -p "Name: " name
     read -p "Age: " age
     read -p "Email: " email

    # Append the new record to the file
     echo "$name, $age, $email" >> records.txt
     echo "Record added successfully"
}

# Function to edit an existing record
edit_record() {
      
  
      echo "Enter the name of the record to edit: "
      read -p "Name: " name

     # Check if the record exists
     if grep -q "^$name," records.txt; then
              # grep -q is used to search for a pattern in files but does not output the matching lines. Instead it returns a success or failure code

          
         # Prompt for new details
         read -p "New age: " new_age
         read -p "New email: " new_email

         # Edit the record in the file 
         sed -i
"s/^$name,.*/$name,$new_age,$new_email/"
records.txt
          echo "Record updated successfully"
     else
          echo "Record not found."
     fi
}

# Function to search for a record
search_record() {
      read -p "Enter the name to search for: "
query
      grep -i "$query" records.txt
}


# Function to generate reports
generate_reports() {
      
      echo "Generating reports..."

      # Example report: Total number of records:
      total_records=$(wc -l < records.txt)
      echo "Total number of records: $total_records"
}


# Main loop
while true; do
    display_menu
    read -p "Enter your choice: " choice
    case $choice in
         1) add_record ;;
         2) edit_record ;;
         3) search_record ;;
         4) generate_reports ;;
         5) echo "Existing program." && break ;;
         *) echo "Invalid choice. Please enter a number from 1 to 5." ;;

     esac
done
```

## Task 3
Bash script that automates the process of creating regular backups of the personal record file

```
#!/bin/bash

# Define varibles
source_file="$HOME/records.txt"
backup_dir="$HOME/backup"
timestamp=$(date +%Y%m%d%H%M%S)
backup_file="$backup_dir/records.txt"

# Create backup dir if it doesn't exist

mkdir -p "$backup_dir"

# Copy the records to the backup directory with timestamp

cp "$source_file" "$backup_file"

# Display sucess message
echo "Backup created successfully: $backup_file"
```

## Task 4
 Bash script that generates strong and random password

 ```
#!/bin/bash

echo "Welcome to my password generator"

# Prompt user for length of password
echo "Please enter the desired length of your password"
read pass_length

# A loop to create 5 options to choose from
for p in $(seq 1 5);
do
    openssl rand -base64 48 | cut -c1-$pass_length
done
```
