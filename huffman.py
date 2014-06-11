import sys
codes = {}
def frequency(str):
	freqs = {}
	for ch in str:
		freqs[ch] = freqs.get(ch, 0) + 1
	return freqs

def sortFreq(freqs):
	letters = freqs.keys()
	tuples = []
	for let in letters:
		tuples.append((freqs[let],let))
	tuples.sort()
	return tuples

def buildTree(tuples):
	while len(tuples) > 1:
		leastTwo = tuple(tuples[0:2])
		##print 'Least Two : ', leastTwo,'\n'
		theRest = tuples[2:]
		##print 'Rest : ', theRest, '\n'
		combFreq= leastTwo[0][0] + leastTwo[1][0]
		tuples = theRest + [(combFreq, leastTwo)]
		##print 'Tuple : ', tuples, '\n'
		tuples.sort()
		##print tuples	
	return tuples[0]

def trimTree(tree):
	p = tree[1]
	##print 'P : ', p
	if type(p) == type(""):
		return p
	else:
		return (trimTree(p[0]), trimTree(p[1]))

def assignCodes(node, pat =''):
	global codes 
	##print 'Node : ', node
	##print 'Type : ', type(node)
	if type(node) == type(""):
		##print codes
		codes[node] = pat
	else:
		assignCodes(node[0], pat+"0")
		assignCodes(node[1], pat+"1")
	return codes

def encode(str):
	global codes
	output = ""
	for ch in str:
		output += codes[ch]
	return output

def decode(tree, str):
	output = ""
	p = tree
	##print '\n', p
	for bit in str:
		if bit == '0':
			##print '\np[0] : ', p[0]
			p = p[0]
		else:
			p = p[1]
			##print '\n p[1] : ', p
		if type(p) == type(""):
			output += p
			p = tree
	return output

def main():
	prompt = 'Enter a String : '
	string = raw_input(prompt)
	##string = "aaabccdeeeeeffg"
	freqs = frequency(string)
	##print 'Frequency : ', freqs
	tuples = sortFreq(freqs)
	##print 'Sorted Tuple : ', tuples 
	tree = buildTree(tuples)
	##print 'Tree : ', tree
	trim = trimTree(tree)
	##print 'Trim : ', trim
	codes = assignCodes(trim)
	##print codes
	string1 = encode(string)
	print 'Encoded Data : ', string1
	decoded = decode(trim, string1)
	print 'Decoded : ', decoded

if __name__=='__main__':
	main()
