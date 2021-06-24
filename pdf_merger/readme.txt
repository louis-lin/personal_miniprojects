This python file merges PDFs.

It reads a the pdf_instructions.txt file which includes the output pdf name and list the pdfs to be merged. One option is to have the path of the FOLDER to the instructions be copied to the clipboard (not the path to the instructions). 

The instructions has 2 parts. The output file name and the input file list. The template is provided. The output file name should be on line 2 and any pdf to be merged should be listed on lines 4 and above.

It should look something like this 

1 Output:
2 FILENAME.pdf
3 Input:
4 LIST OF PDFs <optional page range>

One additional feature is being to select pages to merge. Please refer to:
https://docs.linuxconsulting.mn.it/notes/use_page_ranges_in_pypdf2_pdffilemerger
> : 	all pages
> -1	last page
> :-1	all but the last page
> -2:	last two pages

This can be attached as the second part of the LIST OF PDFs in the optional.

One way to list all the PDFs in a folder is to use Python's glob function. Open a Powershell or command window in the main directory with all the PDFs. 

> python
> from glob import glob
> [print(f) for f in glob.glob('**/*.pdf', recursive=True)]

This prints all of the pdf files found in the current directory and child directories.