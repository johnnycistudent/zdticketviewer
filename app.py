import os, math, datetime, requests
from flask import Flask, render_template, redirect, request, url_for, session, flash
from zenpy import Zenpy
app = Flask(__name__)

# Variables
url = 'https://johncom.zendesk.com/api/v2/tickets.json'
user = 'johnoco18@gmail.com' + '/token'
pwd = '7qdKPuvHFq3F5gokySisf3CCZE16fNsSMn3IMxlf'
response = requests.get(url, auth=(user, pwd))
data = response.json()


def authenticate():

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code,
            'Problem with the request. Exiting.')
        exit()
    else:
        print("Connected to API")

    

@app.route("/")
def get_tickets():

    authenticate()

    tickets = data['tickets']

    return render_template("index.html", tickets = tickets)

@app.route("/ticket/<ticket_id>")
def ticket_view(ticket_id):
    # Individual Ticket View
    
    info = {'ticket': { 'id': {'subject': subject}}}

    payload = json.dump(info)

    ticket_url = 'https://johncom.zendesk.com/api/v2/tickets/' + ticket_id +'.json'
    print(ticket_id)
    
    return render_template('ticket_view.html', ticket_id = ticket_id)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
