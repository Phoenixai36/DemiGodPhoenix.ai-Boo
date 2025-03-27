from flask import Flask
from core.system_core import SystemCore

app = Flask(__name__)
core = SystemCore(month=1)

@app.route('/')
def dashboard():
    core.run_cycle()
    users = core.user_manager.users
    total_commission = core.user_manager.get_total_commission()
    html = "<h1>DemiGod Phoenix Dashboard</h1>"
    html += f"<p>Admin Income: ${core.income:.2f}</p>"
    html += f"<p>Admin Costs: ${core.costs:.2f}</p>"
    html += f"<p>Total Commission from Users: ${total_commission:.2f}</p>"
    html += "<h2>User Matrix</h2><ul>"
    for user in users.values():
        roi = user.get_roi()
        commission = user.get_commission()
        html += f"<li>{user.username} (ID: {user.user_id}) - Clicks: {user.clicks}, Income: ${user.income:.2f}, ROI: ${roi:.2f}, Commission: ${commission:.2f}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)