from tika import parser
import glob
import re

file = "C:\\Users\\jenni\\Desktop\\New York Articles"

txtNames = ["Article1-4.txt", "Article2-4.txt", "Article3-4.txt", "Article4-4.txt"]
count = 0;

pdfFiles = glob.glob("%s/*.pdf" % file)

for pdf in pdfFiles:
    f = open(txtNames[count], "w+", encoding = 'utf8')
    fileData = parser.from_file(pdf)   # Parse data from file
    text = fileData['content']  # Get files text content
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\s+\n', ' ', text)
    text = text.split("Reporting was contributed", 1)
    substring = text[0]
    f.write(substring)
    count += 1

#Need a for loop for the files that are in the folder looking for pdfs and store them into text files