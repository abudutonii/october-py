'''
The replace_ending function replaces the old string in a sentence with the new string, but only if the
sentence ends with the old string. If there is more than one occurrence of the old string in the sentence,
only the one at the end is replaced, not all of them.
For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return
abcabc (no changes made).
'''

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if old in sentence:
		if sentence.split()[-1]==old:
			
			if sentence.count(old)>1:
				i = sentence[:sentence.rfind(old)]
				new_sentence = i + new
			else:
				new_sentence = sentence.replace(old, new)
			return new_sentence

	# Return the original sentence if there is no match 
	return sentence