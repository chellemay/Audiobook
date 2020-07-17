import pyttsx3
import PyPDF2
book = open('Maya.pdf', 'rb')
# change book
# book = open('opp.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# print(pages)
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    rate = speaker.getProperty('rate')
    # print (rate)
# Voice
    # voices = speaker.getProperty('voices')
    # speaker.setProperty('volume', 1.0)
# Rate
    speaker.setProperty('rate', 150)
    speaker.runAndWait()
    speaker.stop()
