# Text-Extractor-and-Summarizer

The text summarizer model is originally from: https://blog.floydhub.com/gentle-introduction-to-text-summarization-in-machine-learning/ and is also represented in https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65

Overview of Code:
  Text Extractor: The code of this consists on importing tika, re ,and glob. After these imports then the code begins by reading in files from a folder through the use of glob. As the code iterates through each file it will parse the text from the pdf through the use of tika. Then will remove website links and whitespace from the text that begin read from the file by using re. The next step in the code is to remove a specific amount of text that I did not want to include in the text summarization process. Lastly, this other part of the text will be stored into a new text file.
  
  Text Summarizer: In this there are additional pre-processing steps such as removing stop words and tokenizing the sentences. After this a table is created that contains the frequency of each word and this table will then be used to determine averages of sentences. The summary is created by selecting sentences that are above the average sentence score and this "limit" can be modified by the user. 

Using this system:
In order to use this system, you would first have to have your chosen articles in a folder (include your own path file) which can be ran through the text extractor. A note for this is that in my text it had many website links and specific lines that I did not want to include and this determined what I wanted to clean from the document. Therfore, when implementing this model it is important that you determine what aspects from your dataset you would want to clean. 

For the text summarization this could be implemented for text files and this only requires you to have your own path file stated in the reader. Depending on the text that you will be using, you may or may not want to change the "limit" of the sentences that will be chosen and this is up to you. 

Limitations:
Due to this being purely an extractive approach the generated summary will grammatical errors as the model does not understand how to compose sentences effectively. In addition, this may perform better on a text that is focused on topic rather than many as seen in my results. Due to the nature of the articles containing various new stories it become much for difficult for the summary to be understandable as a whole. 
