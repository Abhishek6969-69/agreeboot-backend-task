from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_user_cannot_access_another_users_report():
    # Login as Asha
    response = client.post(
        "/login",
        json={
            "username": "asha",
            "password": "asha123",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    # Asha tries to access Ravi's report
    response = client.get(
        "/reports/r_101",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 403

def test_user_cannot_score_another_users_report():
    response = client.post(
        "/login",
        json={
            "username": "asha",
            "password": "asha123",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    response = client.get(
        "/reports/r_101/score",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 403



def test_user_cannot_update_another_users_report():
    response = client.post(
        "/login",
        json={
            "username": "asha",
            "password": "asha123",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    response = client.patch(
        "/reports/r_101/readings",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "readings": {
                "fasting_glucose": 90
            }
        },
    )

    assert response.status_code == 403

def test_user_can_access_own_report():
    response = client.post(
        "/login",
        json={
            "username": "asha",
            "password": "asha123",
        },
    )

    token = response.json()["access_token"]

    response = client.get(
        "/reports/r_100",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200
    assert response.json()["report_id"] == "r_100"