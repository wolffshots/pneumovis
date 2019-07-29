import xlrd
import csv

def xlsx_to_csv():
	try:
		book = input("Please input an exact xlsx filename: ")
		wb = xlrd.open_workbook(book+".xlsx")
		sh = wb.sheet_by_name('Sheet0')
		out = input("Please input an output csv filename: ")
		your_csv_file = open(out+'.csv', 'w')
		wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

		for rownum in range(sh.nrows):
			wr.writerow(sh.row_values(rownum))

		your_csv_file.close()
	# except FileNotFoundException:
	# 	print("File cannot be found")
	except Exception as e:
		raise e
	

# runs the csv_from_excel function:
if __name__ == "__main__":  
	try:
		xlsx_to_csv()
	except Exception as e:
		raise e