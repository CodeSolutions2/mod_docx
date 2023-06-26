# Using PyPI repository 
import os
import sys
sys.path.insert(1, '/usr/lib/python3.11/site-packages')

# import name_of_folder
import mod_docx

# from name_of_folder import name_of_file as nickname
from mod_docx import mod_docx as mdocx

# --------------------------------------

# [Step 0] Open the docx file as an XML object
# Obtain the orignal docx file
fpath = "/usr/lib/python3.11/site-packages/mod_docx/tests"
fichier = "test_document.docx"
docx_filename = os.path.join(fpath, fichier)
        
# Create a class object for the name_of_file.class_name. Use the class object, to call the functions in the class.
md = mdocx(docx_filename)

# Convert the orignal docx file to XML
document_org = md.opendocx(docx_filename)

# --------------------------------------

# [Step 1] Modify the document
# [To be completed for next version] Modify the document as desired (ie: replace text, change style, change font)
doc_finale = document_org

# --------------------------------------

# [Step 2] Save the changed XML document as a docx file
root_dir = f'{fpath}/'
desired_output_docx_name = 'test_document_out.docx'
md.savedocx_ver_fichier(docx_filename, root_dir, desired_output_docx_name, doc_finale)
