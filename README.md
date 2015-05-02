# Event Extraction for Political Modeling
#### CMAK Political Events Extraction by Camille Malonzo + Areeba Kamal

## Introduction 
As students of politics and computer science, we were naturally impressed by the need for collaboration between the two disciplines for successful computational political forecasting. In addition, we felt that an automated, historically grounded, reliable approach was needed for better political decision-making in contemporary politics, since too often political actors are motivated by their own biases and opinions in predicting future political events. Add to this the fact that hyper active online media and the advent of big data have made it almost impossible for human analyzers alone to take into account every piece of available data, and the idea of a computer reading a large mass of data to make educated predictions is even more appealing. 


## Abstract
Efforts to create automated models that can successfully forecast political events have escalated in the past decade, as security agencies and governments have demanded better, more reliable ways to build early warnings systems for political crises in the wake of global civic and economic unrest. Probing into this area of research, we learnt that the field of automated event extraction is of critical importance. Probabilistic models that predict political events do so by observing large scale corpora of coded events from past decades, and following the patterns observed to identify what sort of events current political situations may incite. Hence, large databases of political events from past years are needed to build these forecasting models. Having realized this, we researched the field of automated event extraction, and found that the most successful event extraction models use a combination of statistical and semantic methods to pull out events data from political newswire. 

Components of our event extraction research and model building include finding training and test data suited to our needs, drafting an algorithm to identify and extract political events from sentences, and comparing our test results to those of state of the art event extraction models currently in use, such as 'Python Engine for Text Resolution and Related Coding Hierarchy' aka PETRARCH, a NLP tool for machine-coding events data, designed to process fully-parsed news summaries in Penn Treebank format, from which ‘whom-did-what-to-whom’ relations are extracted. The final result of our work was a fairly successful event extraction model, with a precision rate of 96.55%, compared to PETRARCH's precision of 100% and a recall rate of 93.44% to PETRARCH’s 16.77% for 40 sentences.


## Running CMAK
Always run CMAK in the command line. Our training set is quite large and because of the large quanitity of memory, CMAK will run incorrectly in IDE's such as Eclipse. Simply run CMAK:

	java -cp bin CMAK __path_to_xml__

## TODOs
1. Implement a simplier pipeline for processes. Currently, the user must input an already processed XML in specific format CMAK takes it in (Stanford Core NLP xml format). It would be more useful if instead the user can just input a sentence without having to do the extra work of creating said XML.
2. Implement a user interface. Command line just doesn't cut it.
3. Create a solution for when sentences have political events mentioned but the main action of the political event is not the root main action.
4. Create a solution for an actor that is not the main noun subject of the root verb. In some cases, the noun subject of the root verb is a non-proper noun that later refers to a proper noun mentioned later in the text. Resolve this discrepancy.