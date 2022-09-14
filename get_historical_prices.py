import requests, pyodbc, re, os


class getHistoricalPrices:
	def __init__(self):
		self.cnxn = pyodbc.connect(r'Driver=SQL Server;Server=MSI\SQLEXPRESS;Database=tsdd;Trusted_Connection=yes;')
		self.cursor = self.cnxn.cursor()
	


url = "https://stock-data2.p.rapidapi.com/v6/finance/recommendationsbysymbol/AAPL"

headers = {
	"X-RapidAPI-Host": "stock-data2.p.rapidapi.com",
	"X-RapidAPI-Key": "634cb62ab1msh8663a4ee19fa272p187b02jsne472fde632d9"
}

response = requests.request("GET", url, headers=headers)

print(response.text)