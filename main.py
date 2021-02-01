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
