from flask import Flask, request, jsonify, render_template_string, send_file
import os

app = Flask(__name__)

# Βάσεις Δεδομένων (Λίστες Python στη μνήμη)
παραγγελίες = []
κρατήσεις = []
αξιολογήσεις = []

# 1. Αρχική σελίδα: Εμφανίζει το index.html που βρίσκεται στον ίδιο φάκελο
@app.route('/')
def home():
    if os.path.exists('index.html'):
        return send_file('index.html')
    else:
        return "⚠️ Το αρχείο index.html δεν βρέθηκε στον ίδιο φάκελο!"

# 2. API: Λήψη Παραγγελίας από την ιστοσελίδα
@app.route('/api/order', methods=['POST'])
def new_order():
    data = request.json
    παραγγελίες.append(data)
    print("🛒 ΝΕΑ ΠΑΡΑΓΓΕΛΙΑ:", data)
    return jsonify({"status": "success", "message": "Η παραγγελία καταχωρήθηκε επιτυχώς!"})

# 3. API: Λήψη Κράτησης από την ιστοσελίδα
@app.route('/api/booking', methods=['POST'])
def new_booking():
    data = request.json
    κρατήσεις.append(data)
    print("📅 ΝΕΑ ΚΡΑΤΗΣΗ:", data)
    return jsonify({"status": "success", "message": "Η κράτηση καταχωρήθηκε επιτυχώς!"})

# 4. ADMIN PANEL: Η σελίδα του διαχειριστή (εσένα!)
@app.route('/admin')
def admin_panel():
    html_code = """
    <!DOCTYPE html>
    <html lang="el">
    <head>
        <meta charset="UTF-8">
        <title>The Business - Admin Panel</title>
        <style>
            body { font-family: sans-serif; background: #0f172a; color: white; padding: 20px; }
            h1 { color: #d97706; text-align: center; }
            .card { background: #1e293b; padding: 15px; margin-bottom: 20px; border-radius: 12px; border: 1px solid #334155; }
            table { width: 100%; border-collapse: collapse; margin-top: 10px; }
            th, td { border: 1px solid #334155; padding: 10px; text-align: left; }
            th { background: #d97706; color: white; }
            .badge { background: #2563eb; padding: 4px 8px; border-radius: 6px; font-size: 0.8rem; }
        </style>
    </head>
    <body>
        <h1>🏢 THE BUSINESS - ADMIN PANEL</h1>
        
        <div class="card">
            <h2>🛒 Παραγγελίες Live</h2>
            <table>
                <tr><th>#</th><th>Πιάτα</th><th>Σύνολο</th></tr>
                {% for p in orders %}
                <tr>
                    <td><span class="badge">#{{ loop.index }}</span></td>
                    <td>{{ p.items }}</td>
                    <td><strong>{{ p.total }} €</strong></td>
                </tr>
                {% else %}
                <tr><td colspan="3">Δεν υπάρχουν παραγγελίες ακόμα.</td></tr>
                {% endfor %}
            </table>
        </div>

        <div class="card">
            <h2>📅 Κρατήσεις Τραπεζιών</h2>
            <table>
                <tr><th>#</th><th>Όνομα</th><th>Άτομα</th><th>Ώρα / Ημερομηνία</th></tr>
                {% for k in bookings %}
                <tr>
                    <td><span class="badge">#{{ loop.index }}</span></td>
                    <td>{{ k.name }}</td>
                    <td>{{ k.guests }} Άτομα</td>
                    <td>{{ k.time }}</td>
                </tr>
                {% else %}
                <tr><td colspan="4">Δεν υπάρχουν κρατήσεις ακόμα.</td></tr>
                {% endfor %}
            </table>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_code, orders=παραγγελίες, bookings=κρατήσεις)

if __name__ == '__main__':
    print("🚀 Ο Server του The Business ξεκίνησε!")
    print("👉 Μπες στο: http://127.0.0.1:5000 για την εφαρμογή")
    print("👉 Μπες στο: http://127.0.0.1:5000/admin για το Admin Panel")
    app.run(debug=True, port=5000)