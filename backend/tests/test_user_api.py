





def test_read_users(test_app):
    response = test_app.get(f"/users")
    assert response.status_code == 200
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]


def test_create_user(test_app):
    response = test_app.post(f"/users", params={"username": "Rick"})
    assert response.status_code == 200
    assert response.json() == {"username": "Rick"}


def test_update_user(test_app):
    response = test_app.put(f"/users/Rick", json={"username": "Rick"})
    assert response.status_code == 200
    assert response.json() == {"username": "Rick"}


def test_delete_user(test_app):   
    response = test_app.delete(f"/users/Rick")
    assert response.status_code == 200

    