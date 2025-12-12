from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)





  
@app.route("/")
def hello_prat():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", 
                           jobs = jobs_list,
                           company_name="Prat Careers")    

@app.route("/api/jobs")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host = '0.0.0.0', debug = True)



# # DB_HOST=gateway01.ap-southeast-1.prod.aws.tidbcloud.com
# DB_PORT=4000
# DB_USERNAME='3GxHxErWsrD7EfV.root'
# DB_PASSWORD='RqhJphXNZb16UJOO'
# DB_DATABASE='test'