import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;

import java.io.File;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
 

public class EventExtractor {
	
	private HashSet<String> actors = new HashSet<String>();
	private ArrayList<Sentence> sentences;

	public EventExtractor() {
		sentences = new ArrayList<Sentence>();
	}

	public static void main(String[] args) {
		EventExtractor eventExtractor = new EventExtractor();
		try {
			File fXmlFile = new File("PetrarchGigaWord.xml");
	    	DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	    	DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	    	Document doc = dBuilder.parse(fXmlFile);
	     
	    	//optional, but recommended
	    	//read this - http://stackoverflow.com/questions/13786607/normalization-in-dom-parsing-with-java-how-does-it-work
	    	doc.getDocumentElement().normalize();
	     
	    	System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
	     
	    	NodeList nList = doc.getElementsByTagName("sentence");
	    	eventExtractor.sentences.add(new Sentence(nList));
	     
	    	System.out.println("----------------------------");
	     
	    	} catch (Exception e) {
	    	e.printStackTrace();
	        }
		
	}
}
