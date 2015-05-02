import xml.etree.cElementTree as ET
import os 

def processRaw() :
	with open('sentences.txt') as r:
		raw_sentences = r.read().split('\n')
		return raw_sentences		

def processTree() :
	parse_sentences = []
	tree = ET.parse('sentences.xml')
	sentences = tree.getroot()[0][0]
	for sentence in sentences :
		parse = sentence.find('parse').text
		parse = parse[6:len(parse)-2] 
		parse_sentences.append(parse)		
	return parse_sentences

def createXML(n, raw_sentence, parse_tree, tree):
	sentenceID = "CMAK_" + str(n)
	sentence = ET.SubElement(tree, "Sentence", date="20150422", id=sentenceID, source="CMAK", sentence="True")
	ET.SubElement(sentence, "Text").text = raw_sentence
	ET.SubElement(sentence, "Parse").text = parse_tree
	return tree


def main():
	raw = processRaw()
	parse = processTree()

	sentences = ET.Element("Sentences")

	if len(raw) == len(parse) :
		print "getting to raw = parse"
		last = 0
		for s in range(len(raw)) :
			print raw[s]
			print parse[s]
			sentences = createXML(s, raw[s], parse[s], sentences)
			last = s
		if last+1 == len(raw):
			print "getting here"
			tree = ET.ElementTree(sentences)
			xml_file_name = "CMAK.xml"
			tree.write(xml_file_name)


if __name__ == "__main__":
    main()