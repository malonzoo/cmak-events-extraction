import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;


public class TrainingSet {

	public static ArrayList<String> actors; 
	public static HashMap<String, ArrayList<String>> issues;
	
	public TrainingSet() throws FileNotFoundException 
	{
		actors = new ArrayList<String>();
		issues = new HashMap<String, ArrayList<String>>();
		loadActors(); 
		loadIssues(); 	
	}
	
	
	public void loadActors() throws FileNotFoundException {
		
		Scanner s1 = new Scanner(new File("Phoenix.Countries.actors.txt"));
		
		s1.useDelimiter("\n");
		while (s1.hasNext())
		{
			String line = s1.next();
			line = line.trim();
			String zero = null; 
			try{
				 zero = ((Character)line.charAt(0)).toString();
			} catch (StringIndexOutOfBoundsException s){};
			
			if(line != null && zero != null && !zero.equals('[') )
			{
				if(line.indexOf(";") != -1)
					line = line.substring(0, line.indexOf(";")); 
				
				if(line.indexOf("#") != -1)
					line = line.substring(0, line.indexOf("#")); 
				if(line.indexOf("[") != -1)
					line = line.substring(0, line.indexOf("["));
			}
			
			line.trim();
			
				if(!actors.contains(line))
					actors.add(line.toLowerCase());
		}	s1.close();
	}
	
	public void loadIssues() throws FileNotFoundException {
		Scanner s2 = new Scanner(new File("issues.txt"));
		s2.useDelimiter("\n");
		while (s2.hasNext()){
			String line = s2.next();
			// don't add terms beginning with an ~ since those are less imp in the orig file
			if(line.indexOf('~') == -1)
				addIssue(line.toLowerCase());
		} s2.close();
	}

	private void addIssue(String line) {
		
		int i = line.indexOf('[');
		String sub = ""; 
		String topic = ""; 
		
		// figure out where subissue is and where topic is in the formal subissue [topic]
		if(i != -1) {
			sub = line.substring(0, i); 
			sub = sub.trim().replaceAll("\\s+",""); 
			int j = line.indexOf(']');
			topic = line.substring(i+1, j); 
			topic = topic.trim(); 
		} else {
			sub = line.trim().replaceAll("\\s+",""); 
			topic = null; 
		}
		
		if(topic == null) // sub only, no topic
		{
			if(!issues.containsKey(sub)) {
				ArrayList<String> topics = new ArrayList<String>(); 
				issues.put(sub, topics); 
			} 
		} 
		else //both sub and topic
		{
			if(issues.containsKey(sub))
				issues.get(sub).add(topic); 
			else
			{
				ArrayList<String> topics = new ArrayList<String>(); 
				topics.add(topic); 
				issues.put(sub, topics); 
			}
		}
	}
	
	public static void main(String[] args) throws FileNotFoundException {
		
		TrainingSet t = new TrainingSet(); 
//		System.out.println(t.actors);
		System.out.println(actors.contains("nepal"));
		t.issues.containsKey("interamericandevelopmentbank");
	}
	
	
	
	
	
}
