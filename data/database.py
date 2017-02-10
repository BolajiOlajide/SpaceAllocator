import sqlite3
import sys

#initialize database

class DatabaseInit():

	def __init__(self):
		try:
			self.db_conn = sqlite3.connect("dojo.db")
			self.cursor = self.db_conn.cursor()
		except sqlite3.OperationalError:
			print("Database Couldn't be accessed!")

	def initialize(self):

		print ("Database Successfully Created")

		# Create Room Table
		self.cursor.execute('''CREATE TABLE room \
			(room_name,room_type)''')

		# Save (commit) the changes
		self.db_conn.commit()

		# Create Person Table
		self.cursor.execute('''CREATE TABLE person \n
			(person_name,person_position)''')

		# Save (commit) the changes
		self.db_conn.commit()

		# We can also close the connection if we are done with it.
		# Just be sure any changes have been committed or they will be lost.
		self.db_conn.close()
		print('Database Successfully Initialized')

	def db_create_room(self,room_name,room_type):

		'''Check if room already exists'''
		self.cursor.execute("Select * from room where room_name = ?", (room_name, ))
		check = self.cursor.fetchone()

		if check is None:
			#add room to existing Room table
			self.room_name = room_name
			self.room_type = room_type
			self.cursor.execute("""INSERT INTO room (room_name, room_type) \
				VALUES ('%s','%s')""" % (self.room_name,self.room_type))
			print("A %s called %s has been successfully created!" % (self.room_type,self.room_name))

			# Save (commit) the changes
			self.db_conn.commit()
		else:
			print("Room already exists!")

	def db_add_person(self,person_name,person_position):

		#add person to existing Person table
		self.person_name = person_name
		self.person_position = person_position
		self.cursor.execute("""INSERT INTO person (person_name, person.position) \
			VALUES ('%s','%s')""" % (self.person_name,self.person_position))
		print("A %s called %s has been successfully created!" % (self.person_name,self.person_position))

		# Save (commit) the changes
		self.db_conn.commit()