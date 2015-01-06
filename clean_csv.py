
import sys
import csv


DEFAULT_HEADER = ['FID', 'REF_NUM', 'ADDED_BY', 'DATE_ADD', 'DATE_REV', 'EVENT_DATE', 'EVT_ADDR', 'TRUE_SINK', 'LONGDD', 'LATDD', 'COUNTY', 'TWNSHP', 'TWNSHP_D', 'RANGE', 'RANGE_D', 'SECTION', 'QTRSECT1', 'QTRSECT2', 'ACCURACY', 'RPT_SOURCE', 'RPT_PHONE', 'RPT_NAME', 'OSTREET', 'OCITY', 'OZIP', 'SIZDIM', 'SINSHAPE', 'SINLNGTH', 'SINWIDTH', 'SINDEPTH', 'SLOPE', 'WATSIN', 'WATBLS', 'LIMVIS', 'CAVVIS', 'SUBRATE', 'PROPDAM', 'REPAIR_S', 'DRAINSTR', 'SOILTYPE', 'COMMENTS', 'COMMENTS_2', 'ACCESS', 'WITNAM', 'WITADDRE', 'WITCTZIP', 'WITPHONE', 'EM_Hard_Co', 'Pre_Collap', 'LandUseCod', 'Topography', 'Triggers_1']

def get_csv_data(file_name):
	with open(file_name) as f:
		reader = csv.reader(f)
		header = next(reader)
		rest_of_lines = [line for line in reader]
	csv_data = {'header': header, 'lines': rest_of_lines}
	return csv_data

def clean_csv_data(csv_data):
	clean_csv_data = csv_data.copy()
	clean_csv_data['header'][0] = DEFAULT_HEADER[0]
	return clean_csv_data

def print_csv_stats(file_name, csv_data):
	length = len(csv_data['lines'])
	print "We have %s lines in our csv file %s" % (length, file_name)
	header = csv_data['header']
	print "The header is %s" % header

def process_csv_data(file_name):
	csv_data = get_csv_data(file_name)
	csv_data = clean_csv_data(csv_data)
	print_csv_stats(file_name, csv_data)

if __name__ == '__main__':
	file_name = sys.argv[1]
	process_csv_data(file_name)
