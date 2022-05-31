from multiprocessing.pool import ThreadPool
import concurrent.futures
data = '0000000000000000'
def people1(date):
	first = 0
	for i in date[0:8] :
		first += int(i)
		first = first%10 + first//10
	return str(first)

def people2(date):
	second = 0
	for i in date[8:16] :
		second += int(i)
		second = second%10 + second//10
	return str(second)


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future1 = executor.submit(people1, data)
#     future2 = executor.submit(people2,data)
#     return_value1 = future1.result()
#     return_value2 = future2.result()
#     print(return_value1)
#     print(return_value2)
print(people1(data))
print(people1(data))
