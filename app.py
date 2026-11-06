import os, sqlite3
from flask import Flask, request, jsonify, render_template

app=Flask(__name__); app.config["DATABASE"]=os.environ.get("DATABASE","incidentboard.sqlite3")
STATUSES=("Open","In Progress","Resolved","Closed")
PRIORITIES=("Low","Medium","High","Critical")
def db():
    c=sqlite3.connect(app.config["DATABASE"]); c.row_factory=sqlite3.Row; return c
def init_db():
    with db() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS issues(
        id INTEGER PRIMARY KEY,title TEXT NOT NULL,description TEXT NOT NULL DEFAULT '',
        category TEXT NOT NULL DEFAULT 'General',priority TEXT NOT NULL DEFAULT 'Medium',
        assignee TEXT NOT NULL DEFAULT '',status TEXT NOT NULL DEFAULT 'Open',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
        c.execute("""CREATE TABLE IF NOT EXISTS activity(
        id INTEGER PRIMARY KEY,issue_id INTEGER NOT NULL,action TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(issue_id) REFERENCES issues(id) ON DELETE CASCADE)""")
@app.get("/")
def home(): return render_template("index.html")
@app.get("/api/issues")
def issues():
    status=request.args.get("status",""); priority=request.args.get("priority","")
    sql="SELECT * FROM issues WHERE 1=1"; args=[]
    if status: sql+=" AND status=?"; args.append(status)
    if priority: sql+=" AND priority=?"; args.append(priority)
    sql+=" ORDER BY CASE priority WHEN 'Critical' THEN 0 WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END,updated_at DESC"
    with db() as c: rows=c.execute(sql,args).fetchall()
    return jsonify([dict(x) for x in rows])
@app.post("/api/issues")
def create_issue():
    d=request.get_json(silent=True) or {}
    title=str(d.get("title","")).strip(); desc=str(d.get("description","")).strip()
    category=str(d.get("category","General")).strip() or "General"; priority=d.get("priority","Medium"); assignee=str(d.get("assignee","")).strip()
    if not title: return jsonify(error="Issue title is required."),400
    if priority not in PRIORITIES: return jsonify(error="Invalid priority."),400
    with db() as c:
        cur=c.execute("INSERT INTO issues(title,description,category,priority,assignee) VALUES(?,?,?,?,?)",(title,desc,category,priority,assignee))
        issue_id=cur.lastrowid; c.execute("INSERT INTO activity(issue_id,action) VALUES(?,?)",(issue_id,"Issue created"))
        row=c.execute("SELECT * FROM issues WHERE id=?",(issue_id,)).fetchone()
    return jsonify(dict(row)),201
@app.patch("/api/issues/<int:issue_id>")
def update_issue(issue_id):
    d=request.get_json(silent=True) or {}
    with db() as c:
        row=c.execute("SELECT * FROM issues WHERE id=?",(issue_id,)).fetchone()
        if not row: return jsonify(error="Issue not found."),404
        status=d.get("status",row["status"]); priority=d.get("priority",row["priority"]); assignee=str(d.get("assignee",row["assignee"])).strip()
        if status not in STATUSES or priority not in PRIORITIES: return jsonify(error="Invalid status or priority."),400
        changes=[]
        if status!=row["status"]: changes.append("Status: "+row["status"]+" → "+status)
        if priority!=row["priority"]: changes.append("Priority: "+row["priority"]+" → "+priority)
        if assignee!=row["assignee"]: changes.append("Assignee: "+(row["assignee"] or "Unassigned")+" → "+(assignee or "Unassigned"))
        c.execute("UPDATE issues SET status=?,priority=?,assignee=?,updated_at=CURRENT_TIMESTAMP WHERE id=?",(status,priority,assignee,issue_id))
        for action in changes: c.execute("INSERT INTO activity(issue_id,action) VALUES(?,?)",(issue_id,action))
        updated=c.execute("SELECT * FROM issues WHERE id=?",(issue_id,)).fetchone()
    return jsonify(dict(updated))
@app.get("/api/issues/<int:issue_id>/activity")
def issue_activity(issue_id):
    with db() as c:
        if not c.execute("SELECT 1 FROM issues WHERE id=?",(issue_id,)).fetchone(): return jsonify(error="Issue not found."),404
        rows=c.execute("SELECT * FROM activity WHERE issue_id=? ORDER BY id DESC",(issue_id,)).fetchall()
    return jsonify([dict(x) for x in rows])
@app.delete("/api/issues/<int:issue_id>")
def delete_issue(issue_id):
    with db() as c:
        c.execute("PRAGMA foreign_keys=ON"); cur=c.execute("DELETE FROM issues WHERE id=?",(issue_id,))
    return ("",204) if cur.rowcount else (jsonify(error="Issue not found."),404)
@app.get("/api/stats")
def stats():
    with db() as c:
        rows=c.execute("SELECT status,COUNT(*) n FROM issues GROUP BY status").fetchall()
    return jsonify({r["status"]:r["n"] for r in rows})
with app.app_context(): init_db()
if __name__=="__main__": app.run(debug=os.environ.get("FLASK_DEBUG")=="1")
