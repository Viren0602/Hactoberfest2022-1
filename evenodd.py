# wapp to accept an integer and print if its even or odd
# try with single except


print("Welcome")

try :

	num = int(input("enter an integer "))
	if num % 2 == 0:
		print("even")
	else:
		print("odd")
except ValueError :
	print("u should enter integers only ")

print("Bye")
