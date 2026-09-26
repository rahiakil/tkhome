import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    """
    Take the path of a docx file, read the document.xml file from inside the zip file,
    and return the text content.
    """
    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    PARA = WORD_NAMESPACE + 'p'
    TEXT = WORD_NAMESPACE + 't'
    
    with zipfile.ZipFile(path) as docx:
        tree = ET.parse(docx.open('word/document.xml'))
        root = tree.getroot()
        paragraphs = []
        for paragraph in root.iter(PARA):
            texts = [node.text for node in paragraph.iter(TEXT) if node.text]
            if texts:
                paragraphs.append(''.join(texts))
        return '\n'.join(paragraphs)

if __name__ == '__main__':
    text = get_docx_text('AI Product Engineer Real Case.docx')
    with open('case_description.txt', 'w') as f:
        f.write(text)
    print("Successfully wrote document contents to case_description.txt")
