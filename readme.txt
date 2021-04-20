Random Filename Generator (Adjective Animal)

Step 1. To import the .txt files into individual arrays/lists.
            - Open()
            - with open() as f: for line in f: print(line)
            - Close()

Step 2. Split the string into the arrays using:
            - lines = text_file.read().split(',')
                + alt: from numpy import loadtxt

Step 3. Randomly select a index point inside array1 and then repeat for array2.
            -

Step 4. Concatenate a string with the randomly designated index string value
            - print(array1word + " " + array2word)

https://www.pythontutorial.net/python-basics/python-read-text-file/
https://www.google.com/search?q=how+to+use+import+csv+in+python&rlz=1C1CHBF_en-GBAU913AU913&oq=how+to+use+import+csv&aqs=chrome.0.0j69i57j0i22i30l5.3785j0j1&sourceid=chrome&ie=UTF-8
https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list#comment44278184_3277516
https://convertio.co/txt-csv/
https://docs.python.org/3/library/random.html
https://stackoverflow.com/questions/4394145/picking-a-random-word-from-a-list-in-python

**Don't use file.readlines() in a for-loop, a file object itself is enough: lines = [line.rstrip('\n') for line in file**
** Use lines = [line.rstrip('\n') for line in file]**
