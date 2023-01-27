#Generates prime numbers
def get_prime_numbers(limit):
	lst_prime_numbers = [2]
	for num in range(limit):
		i = 0
		checker = False
		while checker == False:
			i+=1
			if num in [0,1,2] or num%(i+1) == 0:
				checker = True
			elif i > num//2:
				lst_prime_numbers.append(num)
				checker = True
	return lst_prime_numbers


#################MAIN PROGRAM#################
if __name__ == "__main__":
	print(get_prime_numbers(1000))
