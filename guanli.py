#Python??2.7,??Notepad++ 6.1.5??? 
#???????Python?????2???
#database = shelve.open('D:\\python-test\\test.dat')?????????
#????????????,??? 

import sys, shelve
def store_person(db):
	'''
	Store your info.
	'''
	pid = raw_input('Enter your ID: ')
	person = {}
	person['name'] = raw_input('Enter your name: ')
	person['age'] = raw_input('Enter your age: ')
	person['phone'] = raw_input('Enter your phone number: ')
	db[pid] = person

#


def lookup_person(db):
	'''
	Lookup your info.
	'''
	pid = raw_input('Enter the ID: ')
	if pid in db.keys():        #?????ID????
		field = raw_input('What do you want to lookup?(Name, Age, Phone)')
		field = field.strip()   #??field???????????
		if field in ('Name', 'Age', 'Phone'):   #???????       
			field = field.strip().lower()
                        print field.capitalize() + ':', db[pid][field]
		else:
			print 'The input is error!Please enter: Name, Age or Phone'
	else:
		print "The ID is not exist!"
		#lookup_person(db)


#

def print_help():
	print '''
	The available commands are:
	store, lookup,quit,?
	'''
#

def enter_command():
	cmd = raw_input('Enter your command("?" for help): ')
	cmd = cmd.strip().lower()
	return cmd
#

def main():
	database = shelve.open('D:\\python-test\\test.dat')
	try:
		while True:
			cmd = enter_command()
			if cmd == 'store':
				store_person(database)
			elif cmd == 'lookup':
				lookup_person(database)
			elif cmd == '?':
				print_help()
			elif cmd == 'quit':
				return
	finally:
		database.close()

if __name__ == '__main__': main()