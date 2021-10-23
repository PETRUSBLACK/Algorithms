all_code = input("Press 'A' = 'ENCRYPTION' and 'B' = 'DECRIPTION'.  >")

conf = all_code.upper()
universal_num = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','za','zb','zc','zd','ze','zf','zg','zh','zi','zj','zk','zl','zm','zn','zo']

password = input("Input your password")
c = []
d = []
e = []
f = []
i = 0
m = 0
n = int(input("ENTER YOUR KEY NUMBER.  >"))

if conf == 'A':


	
	
	while i < len(password):
		c.append(universal_num.index(password[i]) + n)
		i += 1
	
	for i in c:
		d.append(universal_num[i])
	
	print(f'This is your encryption code {d}')
else:
	# THIS IS THE END OF ENCRYTION
	while m < len(password):
		e.append(universal_num.index(password[m]) - n)
		m += 1

	for i in e:
		f.append(universal_num[i])

	print(f'This is the description {f}')