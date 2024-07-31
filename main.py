from tkinter import filedialog
import PyPDF2
import pyttsx3

text_speech = pyttsx3.init()

# opens the file explorer to choose a pdf file
file_path = filedialog.askopenfilename()


def extract_text(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        read_file = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []
        # adds each page as a list element to pdf_text
        for page in read_file.pages:
            content = page.extract_text()
            pdf_text.append(content)
        return pdf_text


extracted_text = extract_text(file_path)
# turns the text into speech
for text in extracted_text:
    text_speech.say(text)
    text_speech.runAndWait()
