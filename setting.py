from flask import Flask, render_template, redirect, url_for, request, g, session
import sqlite3 as sql,os

app=Flask(__name__)
app.config["CACHE_TYPE"] = "null"
app.secret_key = os.urandom(24)


@app.route("/login_server", methods=["POST"])
def login_server():
	if request.method == "POST":
		enrollmentno = request.form['enrollmentno']
		password = request.form['password']
		con = sql.connect("static/test.db")
		cur = con.cursor()
		#try:
		cur.execute("select password from student where enrollmentno = ?",(enrollmentno,))
		a = cur.fetchone();
		ta=str(a)
		output=ta[2:-3]
		cur.execute("select name from student where enrollmentno = ?",(enrollmentno,))
		b = cur.fetchone();
		cur.close()
		con.close()
		tb=str(b)
		name=tb[2:-3]
		print(output, name)
		session.pop('user', None)
		if request.form['password'] == output and output != '':
			session['user'] = name
			session['enr'] = enrollmentno
			print('session name = ',session['user'])
			return redirect("/student")
		else:
			return ("<h1 class='display-1 text-center'>Invalid Credentials</h1><br><a href='/'>Go to Home Page</a>")


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
      g.user = session['user']


@app.route('/logout')
def logout():
  session.pop('user', None)
  session.pop('enr', None)
  return redirect('/')

@app.route("/")
def index():
	"""if 'user' in session:
		print(session['user'])
		return render_template("index1.html",UserName = session['user'])"""
	return render_template("index.html")

@app.route('/about')
def about():
   return render_template("about.html")

@app.route('/recruiters')
def recruiters():
   return render_template("recruiters.html")

@app.route('/events')
def events():
   return render_template("events.html")

@app.route('/contact')
def contact():
   return render_template("contact.html")

@app.route('/student')
def student():
   if 'user' in session:
      con = sql.connect("static/test.db")
      cur = con.cursor()
      cur.execute("select name,enrollmentno,course,section,contactno,email,batch from student where enrollmentno = ?",(session['enr'],))
      inf = cur.fetchall()
      inf = [j for i in inf for j in i]
      cur.close()
      con.close()
      return render_template("student.html",un=(session['user']).title(),info=inf)
   return redirect("/")

@app.route('/studentf', methods=["POST"])
def studentf():
   if 'user' in session:
      if request.method == "POST":
         dob = request.form['dob']
         college = request.form['college']
         backlogs = request.form['backlogs']
         percent12 = request.form['percent12']
         py12 = request.form['py12']
         stream = request.form['stream']
         maths = request.form['maths']
         percent10 = request.form['percent10']
         py10 = request.form['py10']
         careerobjective = request.form['careerobjective']
         con = sql.connect("static/test.db")
         cur = con.cursor()
         cur.execute("update student set dob = ?,college = ?, backlogs = ?, percent12 = ?, py12 = ?, percent10 = ?, py10 = ?, stream = ?, maths = ?, careerobjective = ? WHERE enrollmentno = ?",(dob,college,backlogs,percent12,py12,percent10,py10,stream,maths,careerobjective,session['enr']))
         con.commit()
         cur.close()
         con.close()
      return redirect("/student")
   return redirect("/")

@app.route("/cmessage", methods=["POST"])
def cmessage():
   if request.method == "POST":
      name = request.form['name']
      enrollno = int(request.form['enrollno'])
      email = request.form['email']
      subject = request.form['subject']
      message = request.form['message']
      con = sql.connect("static/test.db")
      cur = con.cursor()
      cur.execute("INSERT INTO contact(name,enrollment,email,subject,message)VALUES (?,?,?,?,?)",(name,enrollno,email,subject,message))
      print(name,enrollno,email,subject,message)
      con.commit()
      cur.close()
      con.close()
      return render_template("contact.html",c_modal=True)

"""

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['q']
      print(result)
      con=sql.connect("static/datab.db")
      cur=con.cursor()
      cur.execute("select image_name from photos_photo_table where image_tags like '%"+str(result)+"%'")
      inp=cur.fetchall()
      inp = [j for i in inp for j in i]
      new = []
      if len(inp) == 0:
      	result = result.split(" ")
      	for x in result:
      		cur.execute("select image_name from photos_photo_table where image_tags like '%"+str(x)+"%'")
      		temp = cur.fetchall()
      		new.extend([j for i in temp for j in i])
      	for i in new:
      		if i in inp:
      			inp.remove(i)
      			inp.insert(0,i)
      		else:
      			inp.append(i)
      con.commit()
      #return redirect('/')
      #return redirect(url_for('index'))
      cur.close()
      con.close()
      if 'user' in session:
      	if len(inp) == 0:
      		return render_template("index1.html",UserName = session['user'], r = True)
      	return render_template("index1.html", UserName = session['user'], result =inp)
      if len(inp) == 0:
      	return render_template("index.html", r = True)
      return render_template("index.html",result = inp)

@app.route('/result_category',methods = ['POST', 'GET'])
def result_category():
   if request.method == 'POST':
      result = request.form['q']
      print(result)
      con=sql.connect("static/datab.db")
      cur=con.cursor()
      cur.execute("select image_name from photos_photo_table where image_category like '%"+str(result)+"%'")
      inp=cur.fetchall()
      inp = [j for i in inp for j in i]
      print(inp)
      con.commit()
      #return redirect('/')
      #return redirect(url_for('index'))
      cur.close()
      con.close()
      if 'user' in session:
      	if len(inp) == 0:
      		return render_template("index1.html",UserName = session['user'], r = True)
      	return render_template("index1.html", UserName = session['user'], result =inp)
      if len(inp) == 0:
      	return render_template("index.html", r = True)
      return render_template("index.html",result = inp)
"""
if __name__=="__main__":
	app.run(debug=True,port=5000)
