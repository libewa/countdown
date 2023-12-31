# run this code on the host pi
from datetime import datetime
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time/hour')
def hour():
   # Get the current time
   now = datetime.now()

   # Return the current time as a string
   return str(now.hour)

@app.route('/time/minute')
def minute():
   # Get the current time
   now = datetime.now()

   # Return the current time as a string
   return str(now.minute)

@app.route('/time/second')
def second():
   # Get the current time
   now = datetime.now()

   # Return the current time as a string
   return str(now.second)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)