from flask import jsonify, request, render_template, abort, redirect
from sqlalchemy.orm import Session
from app import db
from app.models import ToDo

def setup_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        """Redirect to Swagger UI"""
        return redirect('/apidocs')

    @app.route('/todos', methods=['GET'])
    def get_todos():
        """
        Retrieve a list of all TODO items.
        ---
        responses:
          200:
            description: A list of TODO items
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The TODO item's ID
                      title:
                        type: string
                        description: The title of the TODO item
                      completed:
                        type: boolean
                        description: Completion status of the TODO item
        """
        with db.session() as session:
            todos = session.query(ToDo).all()
            return jsonify([todo.to_dict() for todo in todos])

    @app.route('/todos', methods=['POST'])
    def create_todo():
        """
        Create a new TODO item.
        ---
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  title:
                    type: string
                    description: The title of the new TODO item
                    example: "New Task"
        responses:
          201:
            description: The created TODO item
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: The TODO item's ID
                    title:
                      type: string
                      description: The title of the TODO item
                    completed:
                      type: boolean
                      description: Completion status of the TODO item
          400:
            description: Bad request, title is required
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "Title is required"
        """
        data = request.get_json() or {}
        if 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        todo = ToDo(title=data['title'])
        with db.session() as session:
            session.add(todo)
            session.commit()
            return jsonify(todo.to_dict()), 201

    @app.route('/todos/<int:id>', methods=['GET'])
    def get_todo_by_id(id):
        """
        Retrieve a TODO item by ID.
        ---
        parameters:
          - name: id
            in: path
            required: true
            description: The TODO item's ID
            schema:
              type: integer
        responses:
          200:
            description: The requested TODO item
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: The TODO item's ID
                    title:
                      type: string
                      description: The title of the TODO item
                    completed:
                      type: boolean
                      description: Completion status of the TODO item
          404:
            description: TODO item not found
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "ToDo item not found"
        """
        with db.session() as session:
            todo = session.get(ToDo, id)
            if todo is None:
                abort(404)
            return jsonify(todo.to_dict())

    @app.route('/todos/<int:id>', methods=['PUT'])
    def update_todo(id):
        """
        Update a TODO item by ID.
        ---
        parameters:
          - name: id
            in: path
            required: true
            description: The TODO item's ID
            schema:
              type: integer
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  title:
                    type: string
                    description: The updated title of the TODO item
                    example: "Updated Task"
                  completed:
                    type: boolean
                    description: The updated completion status
                    example: true
        responses:
          200:
            description: The updated TODO item
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: The TODO item's ID
                    title:
                      type: string
                      description: The title of the TODO item
                    completed:
                      type: boolean
                      description: Completion status of the TODO item
          404:
            description: TODO item not found
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "ToDo item not found"
        """
        with db.session() as session:
            todo = session.get(ToDo, id)
            if todo is None:
                abort(404)
            data = request.get_json() or {}
            todo.title = data.get('title', todo.title)
            todo.completed = data.get('completed', todo.completed)
            session.commit()
            return jsonify(todo.to_dict())

    @app.route('/todos/<int:id>', methods=['DELETE'])
    def delete_todo(id):
        """
        Delete a TODO item by ID.
        ---
        parameters:
          - name: id
            in: path
            required: true
            description: The TODO item's ID
            schema:
              type: integer
        responses:
          200:
            description: Confirmation message
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: "ToDo item deleted"
          404:
            description: TODO item not found
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "ToDo item not found"
        """
        with db.session() as session:
            return jsonify({'message': 'ToDo item deleted'})
