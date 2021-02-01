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
