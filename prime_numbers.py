#Generates prime numbers
def get_prime_numbers(limit):
	lst_prime_numbers = [2] #Add two to list cause it is the first one, avoids errors
	for num in range(limit):
		i = 0
		checker = False
		while checker == False:
			i+=1
			if num in [0,1,2] or num%(i+1) == 0: #This will break the loop
				checker = True
			elif i > num//2: #This will also break the loop if the number is more than half stop number
				lst_prime_numbers.append(num)
				checker = True
	return lst_prime_numbers


#################MAIN PROGRAM#################
if __name__ == "__main__":
	print(get_prime_numbers(1000))
