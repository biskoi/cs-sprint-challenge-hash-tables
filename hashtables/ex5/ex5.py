# Your code here



def finder(paths, queries):
    directory = {}

    for fullPath in paths:
        stringIndex = fullPath.rfind('/') # gives us the index of the last instance of the argument
        filename = fullPath[stringIndex + 1:] # strips the full path into the last directory/file

        if filename not in directory:
            directory[filename] = []
        
        directory[filename].append(fullPath) # stores a list of places where we can find this file

    # directory can now tell us where we can find any file

    result = []

    for terms in queries: # look at each search term
        if terms in directory: # is it in the dictionary?
            result.extend(directory[terms]) # if it is, add the list of places to our result

    return result








#    results = []
#    files = {}
#    for filenames in queries:
#       if filenames not in files:
#          files[filenames] = []


#    for names in files:

#       if string.find(names) != 1:
#          files[names].append(string)

#    arr = [].extend(files[key] for key in files)

#    return arr

   # for string in paths:
   #    for files in queries:
   #       if string.find(files) != -1:
   #          results.append(string)
   
   # return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
