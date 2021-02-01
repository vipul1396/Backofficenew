from flask import Flask, request, render_template,jsonify
import pymysql
import json

app = Flask(__name__)

"""
Connection string to connect with two databases using pymysql
"""
db = pymysql.connect("172.104.10.87", "web_map1", "sfgfgkj54@$8sAb", "linkedin")
db1 = pymysql.connect("172.104.10.87", "web_map1", "sfgfgkj54@$8sAb", "alljobs")

app = Flask(__name__)

""" Main Route home.html"""


@app.route('/')
def someName():
    cursor = db.cursor()
    cursor1 = db1.cursor()
    sql = "SELECT * FROM all_deltas_combined_vw limit 30"
    #sql2 = "SELECT * FROM mapping_clients"
    sql1 = "SELECT CompanyName FROM contact_list_vw" 
    cursor.execute(sql)
    cursor1.execute(sql1)
    #cursor2.execute(sql2) 
    results = cursor.fetchall()
    results1 = cursor1.fetchall()
    #results2 = cursor2.fetchall()
    li = []
    for var in results1:
        li.append(list(var))

    return render_template('home.html', view1_contact_list=results, view2_Company_list=li)


@app.route('/adddata', methods=['POST'])
def add_score():
    cursor = db.cursor()
    ad_source = request.form['ad_source']
    client_name = request.form['client_name']
    client_code = request.form['client_code']
    company_code = request.form['company_code']
    company_name = request.form['company_name']
    company_mail = request.form['company_mail']

    cursor.execute("INSERT INTO mapping_clients (view1_ad_source, view1_client_name, view1_client_code,"
                   "view2_CompanyCode,view2_CompanyName,view2_email) VALUES (%s,%s,%s,%s,%s,%s)",
                   (ad_source, client_name, client_code, company_code, company_name, company_mail))
    db.commit()
    return jsonify(customers='Mapping Updated')


@app.route('/get_company_data', methods=['POST'])
def company_data():
    company_name = request.form['company_name']
    cursor1 = db1.cursor()
    query_string = "SELECT companyCode,email FROM contact_list_vw WHERE CompanyName = %s"
    cursor1.execute(query_string, (company_name,))
    results1 = cursor1.fetchall()
    cursor1.close()
    print(results1)
    return jsonify(customers=results1)


@app.route('/view', methods=['GET'])
def index():
    print("Hi")
    return render_template('index_copy.html')


@app.route('/view', methods=['GET'])

def home():
    return render_template('home.html')

def vipul():
    return render_template('vipul.html')


if __name__ == '__main__':
    app.run(debug=True)
