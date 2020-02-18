from collections import Counter
filename = 'log.txt'


def get_data(prompt, errorMessage = 'At least one task must be used'):
	with open(filename) as fn:
		ln = fn.readline()
		task = input(prompt)
		if task=='1':
			my_list = []
			while ln:
				ln = fn.readline()
				xpage = ln.split('"')
				try:
					my_list.append(xpage[1])
				except IndexError:
					my_list.append('NULL')
					a = (Counter(my_list).most_common(10))
					print('Top 10 requested pages and number of made requests for each one: ')
					print(a)
		elif task=='2':
			my_list = []
			while ln:
				ln = fn.readline()
				xpage = ln.split('"')
				try:
					my_list.append(xpage[2][:4])
				except IndexError:
					my_list.append('NULL')
					countsuccess = 0
					countfail = 0
					for f in my_list:
						if f==' 200' or f==' 300':
							countsuccess += 1
						else:
							countfail += 1
					print('Percentage of successful requests: '+str(round((countsuccess*100)/len(my_list),2))+'%')
		elif task=='3':
			my_list = []
			while ln:
				ln = fn.readline()
				xpage = ln.split('"')
				try:
					my_list.append(xpage[2][:4])
				except IndexError:
					my_list.append('NULL')
					countsuccess = 0
					countfail = 0
					for f in my_list:
						if f==' 200' or f==' 300':
							countsuccess += 1
						else:
							countfail += 1
					print('Percentage of unsuccessful requests: '+str(round((countfail*100)/len(my_list),2))+'%')
		elif task=='4':
			my_list = []
			final_list = []
			while ln:
				ln = fn.readline()
				xpage = ln.split('"')
				try:
					my_list.append(xpage[1]+':'+xpage[2][:4])
				except IndexError:
					my_list.append('NULL')
					countsuccess = 0
					countfail = 0
					for f in my_list:
						request = f[-3:]
						page = f[:-5]
						if request !='200' and request !='300':
							final_list.append(page+':'+request)
					a = (Counter(final_list).most_common(10))
					print('Top 10 unsuccessful page requests: ')
					print(a)
		elif task=='5':
			my_list = []
			while ln:
				ln = fn.readline()
				xpage = ln.split('- -')
				my_list.append(xpage[0])
			a = (Counter(my_list).most_common(10))
			print('The top 10 IPs making the largest number of requests: ')
			print(a)
data = get_data('Enter task: ')
