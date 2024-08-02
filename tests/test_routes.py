import pytest
from app import create_app, db
from app.models import ToDo

@pytest.fixture
def app():
    # Define test-specific configuration
    test_config = {
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    }
    app = create_app(config=test_config)

    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.session.remove()
        clear_tables()  # Clear tables

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def populate_todos(app):
    with app.app_context():
        todos = [
            ToDo(title='First Todo'),
            ToDo(title='Second Todo', completed=True),
            ToDo(title='Third Todo')
        ]
        db.session.bulk_save_objects(todos)
        db.session.commit()

def clear_tables():
    """Clear all tables in the database."""
    with db.session() as session:
        for table in reversed(db.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()

def test_get_todos_no_items(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json == []

def test_get_todos_with_items(client, populate_todos):
    response = client.get('/todos')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 3
    titles = [todo['title'] for todo in data]
    assert 'First Todo' in titles
    assert 'Second Todo' in titles
    assert 'Third Todo' in titles

def test_create_todo_success(client):
    response = client.post('/todos', json={'title': 'Test Todo'})
    assert response.status_code == 201
    data = response.json
    assert 'id' in data
    assert data['title'] == 'Test Todo'
    assert data['completed'] == False

def test_create_todo_missing_title(client):
    response = client.post('/todos', json={})
    assert response.status_code == 400
    assert b'Title is required' in response.data

def test_update_todo_success(client):
    response = client.post('/todos', json={'title': 'Update Test Todo'})
    assert response.status_code == 201
    todo_id = response.json['id']

    response = client.put(f'/todos/{todo_id}', json={'title': 'Updated Title', 'completed': True})
    assert response.status_code == 200
    data = response.json
    assert data['title'] == 'Updated Title'
    assert data['completed'] == True

def test_update_todo_not_found(client):
    response = client.put('/todos/9999', json={'title': 'Non-existent'})
    assert response.status_code == 404

def test_delete_todo_success(client):
    response = client.post('/todos', json={'title': 'Delete Test Todo'})
    assert response.status_code == 201
    todo_id = response.json['id']

    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 200
    assert b'ToDo item deleted' in response.data

    response = client.get('/todos')
    assert response.status_code == 200
    assert all(todo['id'] != todo_id for todo in response.json)

def test_delete_todo_not_found(client):
    response = client.delete('/todos/9999')
    assert response.status_code == 404
