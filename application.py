from flask import Flask, render_template, url_for, send_file

application = app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about_me.html") 



#@app.route("/")
#def home():
#    return render_template("info.html") 


@app.route("/contact")
def Personal_info() :
    return render_template("contact.html")



@app.route("/cv")
def cv():
    return render_template("cv.html")
    #https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_cv&stacked=h

@app.route('/cvpdf') 
def cvpdf():
    return send_file('PDF/Esposito_Davide_Enzo.pdf', as_attachment=True)




if __name__ == "__main__":
    app.run(debug=True, port= 5000)

