# Steven Ngo's Report

## Introduction

This document provides an in-depth look at the updates I made to the TODO List application. It details the thought process behind design decisions, implementation strategies, and reflects on the challenges faced and solutions implemented.

## Task 1: Add New Fields to the existing ToDo Model/Database

### 1. Extend the `ToDo` model

I extended the `ToDo` model to include two new fields: a string field `description` and integer field `priority`.I also set the default values for these fields to empty strings and 1 (high), respectively to ensure that the fields are not null. 

One challenge I faced was whether or not to enforce the suggested range of 1-3 for the `priority` field, as I interpreted it as one of many examples of how priority could be represented as integers. However, after taking a look at the frontend, where the priority is represented as a dropdown with three distinct values in the create ToDo page, I decided to enforce the range of 1-3. I did this by adding a `CheckConstraint` to the model to ensure that the `priority` field is within the desired range. I also validated the `priority` field in the API to ensure that only valid values are accepted and sending an appropriate error message if an invalid value is provided. I also wrote a test to ensure the correct error message is returned when an invalid priority value is provided.

Another challenge I faced was if `description` and `priority` should be included when creating a new `ToDo` item, as the current implementation only requires a `title` field and not completion status. However, the add ToDo page in the frontend includes fields for `description` and `priority`, so I decided to include them in the create operation.

### 2. Update CRUD Operations

#### Create Operation

The current implementation of the `create_todo` function only requires the `title` field to create a new `ToDo` item, with the other fields (i.e. `completed`) being updated via the `update_todo` function. Thus the only change required was to update the pydocstring to reflect the new fields in the response. However, to ensure that this was intended I plan to ask for clarification on this as well.

#### Read Operation

The current implementation of `get_todos` and `get_todo_by_id` converts the `ToDo` model to a dictionary with `to_dict` and returns it as a JSON response with all fields. As such, the only change I made was updating the pydocstrings.

#### Update Operation

I updated the `update_todo` function to allow for updating the `description` and `priority` fields by retrieving the values from the request JSON, if provided. I also updated the pydocstring to reflect the new fields.

### 3. Update DB via Migrations

I created a new migration to reflect the changes by following the README, with `flask db migrate -m "Add description and priority to model"` and `flask db upgrade`.

## Task 2: The unittests are broken again!

### 1. Code completeness

I noticed that the two failing tests were due to the `delete_todo` function not being implemented. I implemented the function and updated the pydocstring to reflect the new fields. If a `ToDo` item with the provided `id` is not found, the function returns a 404 error, else it deletes the item and returns a 200 response.

### 2. Fix the broken tests

With the `delete_todo` function implemented, the two failing tests now pass.

### 3. Update existing tests

To ensure the tests cover the new fields I added new `ToDo` items in `populate_todos` with various `description` and `priority` values. I updated `test_get_todos_with_items` to check for the titles of the new items, using list comprehension to simplify the process. I also added assertions for the `description` and `priority` fields in `test_create_todo_success` and `test_update_todo_success`. Lastly, I created new tests to ensure that a ToDo item is created successfully with the new fields and that the correct error message is returned when an invalid `priority` value is provided during creation and updating.


## Challenges and Solutions

I have experience working with Flask and SQLAlchemy, so the initial setup was straightforward. However, the ~~two~~ main challenges I faced were the aforementioned decision on how to handle the range of the `priority` field ~~and whether or not to include the `description` and `priority` fields in the create operation~~. I initially planned on not enforcing the range ~~and not including the fields in creation~~, with the intention of asking for clarification after and making a note. However, after reviewing the current implementation of the frontend, I decided to enforce the range ~~and include the fields during creation~~. I realized after the fact that the instructions specifies to include the fields during creation.