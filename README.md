# ALX SE

![HBNB Logo](https://github.com/kingleirbag/AirBnB_clone/blob/main/web_static/images/hbnb_logo.png)


<h1 align="center">AirBnB Clone Project (V1) - The Console<h1>

This is a simplified clone of the AirBnB website implemented in Python. It allows users to manage various objects such as users, states, cities, places, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd AirBnB_clone
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the command-line interface:

   ```bash
   python console.py
   ```

2. You will enter the interactive prompt where you can execute commands to manage the objects.

3. #### How to Use Command Interpreter
---
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `<class>.update('<id>', {'name' : 'Julien'})`  | updates attribute of an object             |
| `destroy` | `<class>.destroy('<id>')`                         | destroys specified object                  |
| `show`    | `<class>.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `<class>.all()`                                  | display all objects in class               |
| `count`   | `<class>.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exits                                      |
4. #### Installation
```bash
git clone https://github.com/0xUgochukwu/AirBnB_clone.git
cd AirBnB_clone
```
#### Usage
Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Environment
* Language: Python v3.8.5
* OS: Ubuntu 20.04 LTS

   ```

## Features

- Manage users, states, cities, places, and other objects.
- Create, retrieve, update, and delete objects.
- Data storage using JSON files.
- Interactive command-line interface.
- Integration with unit tests for testing the functionality.

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
