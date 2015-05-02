import xml.etree.cElementTree as ET
import os 

# works fine!
def process(number) :
	raw_filename = 'treebank/raw/wsj_' + str(number) 
	with open(raw_filename, 'r') as r:
		raw_sentences = r.readlines()
		raw_sentences.remove('.START \n')
		raw_sentences = [x for x in raw_sentences if x != "\n"]
		for s in range(0, len(raw_sentences)) :
			if raw_sentences[s].find("\n") > -1 :
				raw_sentences[s] = raw_sentences[s].replace("\n", "")
			if raw_sentences[s][len(raw_sentences[s])-1] == " " :
				raw_sentences[s] = raw_sentences[s][0: len(raw_sentences[s])-1]

	# works fine!
	parsed_filename = 'treebank/combined/wsj_' + str(number) + ".mrg"
	with open(parsed_filename, 'r') as p:
		parsed_sentence = p.read()
		parsed_sentence_lines = parsed_sentence.split('\n')
		parsed_sentence_lines = [x for x in parsed_sentence_lines if len(x) > 0]

		# boundaries for each sentence
		numS = []
		for lineNum in range(len(parsed_sentence_lines)) :
			if parsed_sentence_lines[lineNum][0] == "(" :
				numS.append(lineNum)
		numS.append(len(parsed_sentence_lines)-1)

		# divide the sentences
		parsed_sentences = []
		for numSentence in range(len(numS)-1) : 
			sentence = ""
			for s in range(numS[numSentence], numS[numSentence+1]) : 
				sentence += parsed_sentence_lines[s]
				if s < numS[numSentence+1]-1 : 
					sentence += "\n"
			parsed_sentences.append(sentence)

	sentences = ET.Element("Sentences")

	print "//////////////"
	print str(len(raw_sentences))
	for ugh_r in raw_sentences:
		print "* " + ugh_r
	print "\\\\\\\\\\\\\\\\\\\\"
	print str(len(parsed_sentences))
	for ugh_p in parsed_sentences:
		print ugh_p

	for eachSentence in range(0, len(raw_sentences)) :
		# one sentence
		sentence = ET.SubElement(sentences, "Sentence", date="20150418", id="WSJBLAH_1", source="WSJ", sentence="True")
		ET.SubElement(sentence, "Text").text = raw_sentences[eachSentence]
		ET.SubElement(sentence, "Parse").text = parsed_sentences[eachSentence]

	# .END - add the tree to the final xml
	tree = ET.ElementTree(sentences)
	xml_file_name = "xml/wsj_" + str(number)
	tree.write(xml_file_name)

def main():
	last = 199
	i = 1
	while i <= last  :
		str_i = str(i)
		numZeros = 4 - (len(str_i) % 4)
		print "=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%="
		print str(numZeros*str(0) + str_i)
		process(numZeros*str(0) + str_i)
		i += 1



if __name__ == "__main__":
    main()