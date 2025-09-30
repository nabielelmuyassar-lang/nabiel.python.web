from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Menyimpan catatan di memori (sementara)
catatan_list = []

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Aplikasi Catatan</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; }
        h1 { color: #2c3e50; }
        .note { background: #ecf0f1; padding: 10px; margin: 5px 0; border-radius: 5px; display: flex; justify-content: space-between; }
        form { margin-bottom: 20px; }
        input[type=text] { padding: 8px; width: 250px; }
        button { padding: 6px 10px; background: #3498db; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #2980b9; }
        .hapus { background: #e74c3c; }
        .hapus:hover { background: #c0392b; }
    </style>
</head>
<body>
    <h1>Aplikasi Catatan</h1>
    <form method="POST" action="{{ url_for('tambah_catatan') }}">
        <input type="text" name="catatan" placeholder="Tulis catatan baru..." required>
        <button type="submit">Tambah</button>
    </form>
    <h2>Daftar Catatan:</h2>
    {% if catatan_list %}
        {% for note in catatan_list %}
            <div class="note">
                <span>{{ loop.index }}. {{ note }}</span>
                <form method="POST" action="{{ url_for('hapus_catatan', index=loop.index0) }}">
                    <button class="hapus" type="submit">Hapus</button>
                </form>
            </div>
        {% endfor %}
    {% else %}
        <p>Belum ada catatan.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template, catatan_list=catatan_list)

@app.route("/tambah", methods=["POST"])
def tambah_catatan():
    catatan = request.form.get("catatan")
    if catatan:
        catatan_list.append(catatan)
    return redirect(url_for("index"))

@app.route("/hapus/<int:index>", methods=["POST"])
def hapus_catatan(index):
    if 0 <= index < len(catatan_list):
        catatan_list.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
