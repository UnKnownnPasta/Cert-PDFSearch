# Cert-PDFSearch
This is more of a personal project but the code is cool.
Created to search for sepcific pdfs (originally in a google drive)

# How it works:
There's a folder (locally stored) that contains pdfs (each having 1 page) which have text written in them (names)
This program can take the input of a name and return the exact pdf with that name written in it.

# How to use 
##### ~~noone would or has the use for this anyways~~
Just type in a name in the text field and click find. It'll give you the result at the top bar; if there's pdfs found then below the status bar will be the pdf name (which you can copy) and below that an option to download the file directly.

## Prerequisites
Needs:
  - PyPDF 3.0.1 (Extracting text)
  - tkinter (for GUI)
  - pystray 0.19.4 (Windows app view)

## Notes
The program can also accept words worded weirdly but you should still check for all possible combinations of a name (by each word)
