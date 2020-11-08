# Code from https://repl.it/@TheDrone7/discordpy-rewrite#keep_alive.py
from flask import Flask
from threading import Thread
app = Flask('')

@app.route('/')
def main():
    #index = open("index.html", "r")
    return "<!DOCTYPE html>\n<html>\n	<body>\n		<center><h1>This bot is alive!</h1></center>\n	</body>\n</html>"
    #return '<!DOCTYPE html>\n<html>\n	<head>\n		<style>\n			table, th, td {\n				border: 1px solid black;\n				border-collapse: collapse;\n			}\n			th, td {\n				padding: 5px;\n				text-align: left;\n			}\n		</style>\n	</head>\n	<body>\n		<h2>Bot Stats</h2>\n		<p>To add a caption to a table, use the caption tag.</p>\n		<table style="width:100%">\n			<caption>Monthly savings</caption>\n			<tr>\n				<th>Month</th>\n				<th>Savings</th>\n			</tr>\n			<tr>\n				<td>Prefix</td>\n				<td>' + a.prefix + '</td></tr>\n			<tr>\n				<td>February</td>\n				<td>$50</td>\n			</tr>\n		</table>\n	</body>\n</html>'
    #index.close()
@app.route('/privacy')
def en():
  return '<!DOCTYPE html>\n<html>\n	<body style="display: flex; text-align: center; ">\n		<br></br>\n		<object data="https://apicord.github.io/privacy" width="600" height="500"></object>\n	</body>\n</html>'

def run():
    app.run(host="0.0.0.0", port=2984)

def keep_alive():
    server = Thread(target=run)
    server.start()
