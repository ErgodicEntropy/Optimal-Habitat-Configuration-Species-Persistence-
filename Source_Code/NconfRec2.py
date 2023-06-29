
mod = 1000000007


def calculate(pos, left, k, L, R):

	# Base Case
	if (pos == k):
		if (left == 0):
			return 1
		else:
			return 0

	# If N is divides completely
	# into less than k groups
	if (left == 0):
		return 0

	answer = 0

	# Put all possible values
	# greater equal to prev
	for i in range(L, R + 1):
		if (i > left):
			break
		answer = (answer +
				calculate(pos + 1,
							left - i, k, L, R)) % mod
	return answer

# Function to count the number of
# ways to divide the number N
def countWaystoDivide(n, k, L, R):
	return calculate(0, n, k, L, R)

def mapper(x):
    return countWaystoDivide(x,15,0,15)


x = np.array([random.randint(60,100) for k in range(15)])
y = list(map(mapper,x))

plt.scatter(x,y)
plt.show()



