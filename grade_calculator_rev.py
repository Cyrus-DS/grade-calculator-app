# %%
from flask import Flask, request, render_template_string
import threading

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head><title>Grade Calculator</title></head>
<body>
    <h2>Enter your score:</h2>
    <form method="post">
        <input type="number" name="score" required>
        <button type="submit">Submit</button>
    </form>
    {% if grade %}
        <h3>Your grade is: {{ grade }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    grade = None
    if request.method == 'POST':
        try:
            score = int(request.form['score'])
            if score > 80:
                grade = 'Grade A'
            elif score > 70:
                grade = 'Grade B'
            elif score > 60:
                grade = 'Grade C'
            elif score > 50:
                grade = 'Grade D'
            else:
                grade = 'Grade E'
        except ValueError:
            grade = "Invalid input"
    return render_template_string(html, grade=grade)


def run_app():
    app.run(port=5000)

threading.Thread(target=run_app).start()



# %%



