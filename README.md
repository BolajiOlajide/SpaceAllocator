[![Build Status](https://travis-ci.org/andela-bolajide/SpaceAllocator.svg?branch=test)](https://travis-ci.org/andela-bolajide/SpaceAllocator) [![Coverage Status](https://coveralls.io/repos/github/andela-bolajide/SpaceAllocator/badge.svg?branch=test)](https://coveralls.io/github/andela-bolajide/SpaceAllocator?branch=test) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Dojo Space Allocator

This is a system to allocate offices and living spaces to employees at Dojo.

### What the project does

    Features
        The Dojo Space Allocator comes with the following features:
            - Create Rooms
            - Allocate persons to rooms
            - Reallocate person
            - Save session to sqlite database
            - Load session from sqlite database
            - Checking occupants of a room
            - Printing room allocations to a file

### Why the project is useful
    This project helps to eradicate the current paper system used by most hostels in room allocation.

### How to setup the project/Installation/Configuration

* Clone the repo
```git clone https://github.com/andela-bolajide/SpaceAllocator.git``` and navigate to the project directory

* Install dependencies
```pip install -r requirements.txt```

* Run the program 
```python main.py ``` shows a list of available commands
```python main.py -i ``` takes you into an interactive loop
```python main.py -h ``` displays the help section of the app
    
### Usage:
```
    create_room <room_type> <room_name>...
    add_person <person_fname> <person_lname> <FELLOW/STAFF> [<wants_accommodation>]
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    get_person_id <person_fname> <person_lname>
    print_room <room_name>
    reallocate_person <person_identifier> <room_name>
    load_people <file_name>
    save_state [--db=sqlite_database]
    load_state <sqlite_database>
    purge
    quit
```

### Usage Examples:
```
    create_room office blue
    create_room office blue red green

    create_room livingspace meraki piper

    add_person John Doe staff
    add_person Jane Doe fellow y

    print_allocations
    print_allocations --o=testinput2.txt
    
    print_unallocated
    print_unallocated --o=testinput3.txt

    get_person_id john doe

    print_room green
    print_room red

    reallocate_person FCGURMGE red

    load_people testinput.txt

    save_state --db=dojo.db

    load_state --db=dojo.db

    purge

    quit
```

```    
    main.py (-i | --interactive)
    main.py (-h | --help | --version)
```

### References
https://github.com/docopt/docopt <br />
http://docopt.org/ <br />
https://docs.python.org

### Contributing to the project
```Bolaji Olajide```

### Author
Bolaji Olajide