from flask import Flask
import smtplib
app = Flask(__name__)

@app.route('/')
def homepage():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	#Next, log in to the server
    server.login("from@gmail.com", "paasword")

	#Send the mail
    msg = "Yo, this is shivangi"
    server.sendmail('from@gmail.com','to@gmail.com',msg)
    server.quit()
    return("Hello, this is  Shivangi!")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)