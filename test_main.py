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



def test_login_does_not_return_password():
    response = client.post(
        "/login",
        json={
            "username": "asha",
            "password": "asha123",
        },
    )

    assert response.status_code == 200
    assert "password_was" not in response.json()
    assert "access_token" in response.json()


def test_update_readings_normalizes_alias():
    login_response = client.post(
        "/login",
        json={"username": "asha", "password": "asha123"},
    )

    token = login_response.json()["access_token"]

    response = client.patch(
        "/reports/r_100/readings",
        headers={"Authorization": f"Bearer {token}"},
        json={"readings": {"FBS": 92}},
    )

    assert response.status_code == 200
    assert response.json()["readings"]["fasting_glucose"] == 92
    assert "FBS" not in response.json()["readings"]


def test_update_readings_ignores_unknown_marker():
    login_response = client.post(
        "/login",
        json={"username": "asha", "password": "asha123"},
    )

    token = login_response.json()["access_token"]

    response = client.patch(
        "/reports/r_100/readings",
        headers={"Authorization": f"Bearer {token}"},
        json={"readings": {"unknown_marker": 123}},
    )

    assert response.status_code == 200
    assert "unknown_marker" not in response.json()["readings"]