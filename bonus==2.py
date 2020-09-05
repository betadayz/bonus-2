def isVowel(ch): 

	if (ch != 'a' and ch != 'e' and
		ch != 'i' and ch != 'o' and
		ch != 'u'): 
		return False; 

	return True; 

def replaceConsonants(s): 
	 
	for i in range(len(s)): 
		if (isVowel(s[i])==False): 

			if (s[i] == 'z'): 
				s[i] = 'b'; 

			else: 
       
				s[i] = chr(ord(s[i]) + 1); 

				if (isVowel(s[i])==True): 
					s[i] = chr(ord(s[i]) + 1); 

	return ''.join(s); 

s = "jesus is lord"; 

print(replaceConsonants(list(s))); 

