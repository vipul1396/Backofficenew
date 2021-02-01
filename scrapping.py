from flask import Flask ,render_template 
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='templates') 
app.config['MYSQL_HOST'] = '172.104.10.87'
app.config['MYSQL_USER'] = 'web_map1'
app.config['MYSQL_PASSWORD'] = 'sfgfgkj54@$8sAb'
#app.config['MYSQL_DB'] = 'alljobs'
app.config['MYSQL_DB'] = 'linkedin'
mysql = MySQL(app)
@app.route('/')
def main():
    cur = mysql.connection.cursor()
    #cur.execute('SELECT * FROM contact_list_vw' )
    cur.execute('SELECT * FROM all_deltas_combined_vw' )
    rv = cur.fetchall()
    cur.close()
    Company_list = []
    for var in rv:
        for var1 in list(var):
            if not var1:
                continue
            else:
                Company_list.append(var1)
    #print(Company_list)
    print(len(Company_list))
    #return render_template('index.html',data = Company_list)
    return render_template('main.html',Company_list = Company_list)
    #return str(rv)



if __name__ == '__main__':
    app.run(debug=True)
