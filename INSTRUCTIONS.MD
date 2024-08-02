# Task Instructions for Augmenting the ToDo List Application

Welcome! You have been asked to enhance the existing ToDo list application; the tasks outlined below are meant to mimic 
real world tasks that would be addressed in the workplace.

Below are the instructions and requirements for the enhancements to match the expectations on the frontend application. 

Be sure to complete each of the tasks below to the best of your ability.
Update documentation as necessary and/or add comments as you go along.

If anything is unclear or you have technical difficulty, please comment with your observations and/or explain what
you would do given more time or resources.

Reference the README.md for project specific initial setup, migration creation, and testing instructions.

Note this is OPEN BOOK - it is OK if you do know currently user any of the technologies listed above, please just try your 
best and use any and all resources at your disposal to find and fix the tasked items. Be ready to discuss any changes 
you have made to the application or discoveries while working on the application code.

Take your time, and have fun!

## Tasks

### Task 1: Add New Fields to the existing ToDo Model/Database

Users are requesting additional fields on the Todo model. They want two new fields:
  1. Extend the `ToDo` model to include:
      - `description`: A text field to provide a detailed description of the task.
      - `priority`: An integer field to indicate the priority of the task (e.g., 1 for high, 2 for medium, 3 for low).

  2. **Update CRUD Operations**
     - **Create Operation**: Ensure the two new fields can be set when creating a new ToDo.
     - **Read Operation**: Include the two new fields in the output of the `GET /todos` endpoint.
     - **Update Operation**: Include the two new fields can be updated.

  3. **Update DB via Migrations**
     - Create and apply a new database migration to reflect the changes in the `ToDo` model.


### Task 2: The unittests are broken again!

The automated testing pipeline has failed and kicked back an error, another developer has mentioned that unit tests are 
failing for the test_delete_todo_success and test_delete_todo_not_found tests and they think you forgot to include your 
latest changes.

  1. Code completeness :
     - Ensure that the tested code is complete.

  2. Fix the broken tests :
     - Ensure that the 8 unit tests pass when running the test command mentioned in the README.me file.

  3. Update existing tests :
     - Ensure testing coverage is adequate in covering the two new fields added in Task 1.