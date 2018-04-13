import CV

def addNewline(path, strline):
    with open(path, "a", encoding=CV.ENCODING, newline="\n") as f:
        f.writelines(strline)
        f.close()

def rewriteFile(path, strobj):
    with open(path, "w+", encoding=CV.ENCODING, newline="\n") as f:
        f.truncate()
        f.writelines(strobj)
        f.close()