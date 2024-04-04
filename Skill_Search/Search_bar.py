from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

# Enter your database connection details
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "*********"
app.config["MYSQL_DB"] = "linkedin_job"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route("/")
def index():
    return render_template("test_2.html")

@app.route("/livesearch", methods=["POST", "GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()

    # Execute queries to get desired outputs
    # Query 1: Most common experience level for the skill
    query1 = "SELECT Level FROM details WHERE Job_skills like %s  GROUP BY Level ORDER BY COUNT(*) DESC LIMIT 1"
    cursor.execute(query1, (searchbox,))
    experience_level = cursor.fetchone()

    # Query 2: Most common industry where the skill is required
    query2 = "SELECT Industry FROM details WHERE Job_skills like %s GROUP BY Industry ORDER BY COUNT(*) DESC LIMIT 1"
    cursor.execute(query2, (searchbox,))
    industry = cursor.fetchone()

    # Query 3: Most common Company Class where the skill is required
    query3 = "SELECT Class FROM details WHERE Job_skills like %s GROUP BY Class ORDER BY COUNT(*) DESC LIMIT 1"
    cursor.execute(query3, (searchbox,))
    company_class = cursor.fetchone()

    # Query 4: Number of Jobs available for the skill
    query4 = "SELECT COUNT(*) AS num_jobs FROM details WHERE Job_skills like %s"
    cursor.execute(query4, (searchbox,))
    num_jobs = cursor.fetchone()["num_jobs"]

    cursor.close()

    # Prepare the response data
    response_data = {
        "most_common_experience_level": experience_level["Level"] if experience_level else None,
        "most_common_industry": industry["Industry"] if industry else None,
        "most_common_company_class": company_class["Class"] if company_class else None,
        "number_of_jobs": num_jobs
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
