

# 0x00. AirBnB clone - The console

![Holberton AirBnB](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220702%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220702T195401Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ef32d56087201e2cc4a03801729c217656fb2bdc06033784c9895ab3fd2b2938)

## ***About this project***
This is the first step of our first full web application: the AirBnB clone. Our console is able to work in interactive mode 
but also in non-interactive mode. It main goal is to manage the AirBnB objects. It is capable of creating new objects, 
retrieving an object from a file, doing operations on objects like counting and computing stats, updating attributes of an object
and destroying them.
## ***Learning objectives of this project***
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to implement modules such as datetime, UUID, etc.

## ***How to start and use the console***
- Clone our directory to your working space:
```bash
git clone https://github.com/MatiasMtz/holbertonschool-AirBnB_clone.git
```
- Execute the console: 
```bash
./console.py
```
- Type your commands: 
```
ex.: (hbnb) create BaseModel
```
- If you want to work in non-interactive mode:
```bash
ex.: maxmat@ubuntu:~/AirBnB_clone$ echo "<command>" | ./console.py
```

## ***Implemented commands***

| **COMMAND** | **UTILIZATION**                                                 | **DESCRIPTION**                                                                             |
| ---         | ---                                                             | ---                                                                                         |
| **HELP**    | (hbnb) help \<command>                                          | Gives information about the selected command                                                |
| ‎            | ‎                                                                | ‎                                                                                            |
| **QUIT**    | ‎(hbnb) quit                                                     | Exit console.                                                                               |
| ‎            | \<Ctrl + D>                                                     | Exit console.                                                                               |
| ‎            | ‎                                                                | ‎                                                                                            |
| **CREATE**  | (hbnb) create \<class>                                          | Creates a new instance of the desired class, saves it (to the JSON file) and prints the id. |
| ‎            | ‎                                                                | ‎                                                                                            |
| **DESTROY** | (hbnb) destroy \<class> <id>                                    | Deletes an instance based on the class name and id.                                         |
| ‎            | (hbnb) \<class>.destroy(\<id>)                                  | Deletes an instance based on his id.                                                        |
| ‎            | ‎                                                                | ‎                                                                                            |
| **UPDATE**  | (hbnb) update \<class> \<id> \<attr name> "\<attr value>"       | Updates an instance based on the class name and id by adding or updating attribute.         |
| ‎            | (hbnb) \<class>.update(\<id>, \<attr name> \<attribute value>") | Updates an instance based on his ID                                                         |
| ‎            | (hbnb) \<class>.update(\<id>, \<dict>)                          | Updates an instance based on his ID with a dictionary as it value                           |
| ‎            | ‎                                                                | ‎                                                                                            |
| **ALL**     | (hbnb) all **\***\<class>                                       | Prints all string representation of all instances based or not on the class name.           |
| ‎            | (hbnb) \<class>.all()                                           | Retrieves all instances of a class.                                                         |
| ‎            | ‎                                                                | ‎                                                                                            |
| **SHOW**    | (hbnb) show \<class> \<id>                                      | Prints the string representation of an instance based on the class name and id.             |
| ‎            | (hbnb) \<class>.show(\<id>)                                     | Retrieves an instance based on its ID.                                                      |
| ‎            | ‎                                                                | ‎                                                                                            |
| **COUNT**   | \<class>.count()                                                | Retrieves the number of instances of a class.                                               |

#### References:

- Implemented classes (\<class>) - BaseModel, User, Place, State, City, Amenity, Review.
- \* - Optional argument.

## ***Examples***:
```
maxmat@ubuntu:~/AirBnB_clone$$ ./console.py
```
- Help
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb)
```
- Quit
```
(hbnb) quit 
maxmat@ubuntu:~/AirBnB_clone$$ 
```
- Create
```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907d
(hbnb) create User
d06a167f-9a53-4a45-b61a-0e2851381f75a
```
- All
```
(hbnb) all AnyClass
** class doesn't exist **
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) BaseModel.all()
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
- Show
```
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel WithoutId
** no instance found **
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) BaseModel.show(49faff9a-6318-451f-87b6-910505c55907)
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
- Update
```
(hbnb) update Basemodel
** instance id missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) User.update("d06a167f-9a53-4a45-b61a-0e2851381f75a", "first_name", "John")
(hbnb) User.update("d06a167f-9a53-4a45-b61a-0e2851381f75a", "age", 89)
(hbnb) User.show("d06a167f-9a53-4a45-b61a-0e2851381f75a")
[User] (d06a167f-9a53-4a45-b61a-0e2851381f75a) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': 'd06a167f-9a53-4a45-b61a-0e2851381f75a'}
```
- Destroy
```
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```
- Count
```
(hbnb) User.count()
1
(hbnb) all User
["[User] (c7af570f-6645-4a3f-80cf-be57027ac165) {'id': 'c7af570f-6645-4a3f-80cf-be57027ac165', 'created_at': datetime.datetime(2022, 7, 2, 20, 6, 3, 343076), 'updated_at': datetime.datetime(2022, 7, 2, 20, 6, 3, 343084)}"]
```

### ***Authors***
[Matías Martínez](https://github.com/MatiasMtz) & [Maximiliano Alonso](https://github.com/MaxiHBTN) from Holberton School cohort #17.
