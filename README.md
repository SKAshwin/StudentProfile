# StudentProfile
Student profiler - tracks modules, gives CAP, gives CAP projections etc

--TRAVERSAL--

**Main Folder**
*All application and general files here*

**nushgrading.py** contains all the type definitions for all cap calculation
related types (such as Module, Transcript etc).

**constants.py** contain all the constants (for example, for enum types) to
be used with the rest of the application. Several methods and functions
rely on these constants as input.

**/database**
*Database, module data source and scripts relating to the database placed here*

**grading.db** is the main database used in this project. Be sure to check if  
the db has any garbage data before staging and committing! Reccomended not to  
stage your db if it was used - the hosted version of the db contains universal 
constants required for application functions, in particular the list of modules.
Local additions, like student profiles, should not be committed.

**populateDatabase.py** is a script that given a source text file, a database 
and a table will upload all the source module information to the table in the 
database. Used to update grading.db if the module list changes (just change 
moduleData.txt and run)

**moduleData.txt** is a list of all currently offered modules by NUSH. Any 
changes to offered modules (or changes to stored module structure) should
be done by changing the text file and running populateDatabase.py

**ddl.sql** is the schema for all the tables in the database. Keep updated
