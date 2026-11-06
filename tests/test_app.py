from app import app
import pytest
@pytest.fixture
def client(tmp_path):
    app.config["TESTING"]=True; app.config["DATABASE"]=str(tmp_path/"test.sqlite3")
    from app import init_db
    with app.app_context(): init_db()
    return app.test_client()
def test_issue_lifecycle(client):
    r=client.post("/api/issues",json={"title":"Login bug","priority":"High"})
    assert r.status_code==201
    issue=r.get_json()
    assert client.patch(f"/api/issues/{issue['id']}",json={"status":"Resolved"}).get_json()["status"]=="Resolved"
    assert len(client.get(f"/api/issues/{issue['id']}/activity").get_json())==2
