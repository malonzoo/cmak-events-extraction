import xml.etree.cElementTree as ET

def createXML(sentenceTree) :
	treeToWrite = ET.Element("root")
	ET.SubElement(treeToWrite, "document")
	ET.SubElement(treeToWrite, "sentences")
	ET.SubElement(treeToWrite, sentenceTree)
	file_name = "CMAK_" + str(sentenceTree.attrib['id']) + ".xml"
	treeToWrite.write(file_name)

def main():
	# prepare the document
	tree = ET.parse('sentences.xml')
	sentences = tree.getroot()[0][0]
	for sentence in sentences :
		createXML(sentence)


if __name__ == "__main__":
    main()