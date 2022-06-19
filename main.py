import os
rootdir = '/Users/andipiee/Dev/job-test/dropsuite-backend/DropsuiteTest'

def read_file(rootdir):
    # Get list of files path
    listFiles = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            listFiles.append(os.path.join(subdir, file))

    # Filter only file
    filteredFiles = []
    for file in listFiles:
        if '.DS_Store' not in file:
            filteredFiles.append(file)

    # Save the file content into array
    listOfValues = []
    for file in filteredFiles:
        listOfValues.append(open(file).read())

    # Count the most shown values
    counter = 0
    value = listOfValues[0]
    for i in listOfValues:
        current_frequency = listOfValues.count(i)
        if current_frequency > counter:
            counter = current_frequency
            value = i

    return value + " " + str(counter)

print(read_file(rootdir))