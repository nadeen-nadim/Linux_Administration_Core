#!/bin/sh

<<List
The list function looks for the the address book name in the system and prints its content.
If the file doesnot exist it will create it in the current working directory and tells the user that a new address book
has been created.
List

List()
{
	echo "Enter address book name"
	read bookName
	if [ -f "$bookName" ];then
		echo "Found"
		cat $bookName
	else
		echo "Address book not found\nCreating a new address book in the current directory\n"
		touch $bookName
	fi
}

<<Search
The Search function looks for a contact by name and displays all contacts with that name
Search
Search()
{
	echo "Enter address book name"
	read bookName
	if [ -f "$bookName" ];then
		echo "Enter contact name"
		read Name
		res=`cat $bookName | grep "$Name" | wc -w`
		if  [ $res -gt 0 ]
		then
			echo "Contact info"
			echo `grep -h -C 1 "$Name" $bookName`
		else
			echo "Contact not found"
		fi
		
	else
		echo " Address book not found"
		
	fi
}
<<Add
The add function add a new contact if the phone number given does not exist

Add
Add()
{
	echo "Enter address book name"
	read bookName
	if [ -f "$bookName" ];then
		echo "Enter contact phone number"
		read phoneNumber
		res=`cat $bookName | grep $phoneNumber | wc -w`
		if  [ $res -gt 0 ]
		then
			echo "Number already exist"
			
		else
			echo "Enter contact name"
			read Name
			echo "name:$Name pnone-no.:$phoneNumber\n" >> $bookName

			
		fi
		
	else
		echo "Address book not found"
		
	fi
}

Edit()
{
	echo "Enter address book name"
	read bookName
	if [ -f "$bookName" ];then
		echo "Enter contact phone number"
		read phoneNumber
		res=`cat $bookName | grep $phoneNumber | wc -w`
		if  [ $res -gt 0 ]
		then
			echo "Enter new name"
			read  newName
			echo "Enter new number"
			read newNumber
			old=`cat $bookName | grep -w $phoneNumber`
			new=`echo "name:$newName pnone-no.:$newNumber"`
			sed -i s/"$old"/"$new"/g $bookName
			echo "Contact edited"
			
			
			
			
		else
			echo "Number not found"
			
		fi
		
	else
		echo "Address book not found"
		
	fi
}


Remove()
{
	echo "Enter address book name"
	read bookName
	if [ -f "$bookName" ];then
		echo "Enter contact phone number"
		read phoneNumber
		res=`cat $bookName | grep $phoneNumber | wc -w`
		if  [ $res -gt 0 ]
		then
			old=`cat $bookName | grep -w $phoneNumber`
			sed -i s/"$old"//g $bookName
			echo "Contact removed successfuly"	
		else
			echo "Number not found"
			
		fi
		
	else
		echo "Address book not found"
		
	fi
}



while :
do
	echo "************WELCOME*****************"
	echo "Select one of the following operation:"
	echo "1- List"
	echo "2- Search"
	echo "3- Add"
	echo "4- Edit"
	echo "5- Remove"
	echo "6- Quit"
	read choice
	
	case $choice in
	
		1)
		
		List ;;
		2)
		Search ;;
		
		3)
		Add ;;
		
		4)
		Edit ;;
		
		5)
		Remove ;;
		
		
		6)
		
		exit ;;
		
		*) echo "Unrecognized Command" ;;
	esac

done
	


