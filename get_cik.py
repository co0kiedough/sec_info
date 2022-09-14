import pyodbc
import urllib2
import time
import csv
import requests

class cikLookup:
	
	def __init__(self):
		self.cnxn = pyodbc.connect(r'Driver=SQL Server;Server=MSI\SQLEXPRESS;Database=tsdd;Trusted_Connection=yes;')
		self.cursor = self.cnxn.cursor()
		self.yd = {}
		self.ql = ['QTR1', 'QTR2', 'QTR3', 'QTR4']
		yd = self.yd
		for y in range(1995, 2023):
			if y not in yd:
				yd[y] = {}
			for q in ql:
				if q not in yd[y]:
					yd[y][q] = {}
				if 'text' not in yd[y][q]:
					yd[y][q]['master_idx'] = ''
					yd[y][q]['lines'] = []
					
		
				

	def get_cik(self, company, exact=True):
		if exact == True:
			qstr = '''SELECT TOP 10 cik, company_name FROM cik_lookup WHERE company_name = ?'''
			self.cursor.execute(qstr, company)
		else:
			qstr = '''SELECT TOP 10 cik, company_name FROM cik_lookup WHERE company_name LIKE ?'''
			self.cursor.execute(qstr, '%'+company+'%')
		
		cik_resp = self.cursor.fetchall()
		return cik_resp
	
			#iterate ofver qvar list object
	
	def get_sic_codes(self):
		cik_dict = {}
		tsql = '''SELECT company_name, cik FROM cik_lookup ORDER BY cik ASC'''
		self.cursor.execute(tsql)
		allcik = self.cursor.fetchall()
		for row in allcik:
			try:
				if row['company_name'] not in cik_dict:
					cik_dict[row['company_name']] = row
				cik_dict[row['company_name']]
			except Exception:
				pass
			
		
	def get_10k(self, year_list=None, qtr_list=None, cik_list=None):
		headers = {'User-Agent':'tsdd@uberedibles.com', 'Accept-Encoding':'gzip, deflate', 'Host':'www.sec.gov'}
		fl = {}
		if cik_list == None:
			cik_lookup = self.cursor.execute('''select * from tickers_xchg where name not like '[0-9]%' and name not like '@%' and name not like '"%' order by name asc''')
		if year_list == None:
			year_list = []
			for y in range(1995, 2023):
				year_list.append(y)
		if qtr_list == None:
			qtr_list = self.ql.copy()
		
			
		for year in year_list:
			if year not in fl:
				fl[year] = {}
			for qtr in qtr_list:
				if qtr not in fl[year][qtr]:
					fl[year][qtr]
				
		for y in yl:
			for qtr in yl[y]:
				idxurl='https://www.sec.gov/Archives/edgar/full-index/%s/%s/master.idx' % (y, qtr)
				idxreq = requests.get(idxurl, headers=headers)
				idxresp = idxreq.text
				
				idxlines = idxresp.splitlines()
				for line in idxlines:
					if '10-K'
			
					
		
	
	
	def get_filing(self, cik_list, year_list, qtr_list, filing_list):
		headers = {'User-Agent':'tsdd@uberedibles.com', 'Accept-Encoding':'gzip, deflate', 'Host':'www.sec.gov'}
		for year in self.yd:
			for qtr in self.yd[year]:
				idxurl='https://www.sec.gov/Archives/edgar/full-index/%s/%s/master.idx' % (year, qtr)
				idxresp = requests.get(idxurl, headers= headers)
				self.yd[year][qtr]['idx'] = idxresp.text
				idxtext = idxresp.text
				idxlines = idxtext.split('\n')
				self.yd[year][qtr]['lines'] = []
				for line in idxlines:
					if '10-K' in line:
						
						self.yd[year][qtr]['lines'].append(line)
				
# 				
# for y in yd:
#      for q in yd[y]:
#              thist = yd[y][q]['text']
#              for line in thist.split('\n'):
#                      if '40-F' in line or '10-K' in line:
#                              ourpart = line.split('edgar/data')[1]
#                              thisurl = 'https://www.sec.gov/Archives/edgar/data'+ourpart

		
	
	#code
