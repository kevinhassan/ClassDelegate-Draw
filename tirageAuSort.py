#This function extract the list of students after xls opening
def extractStudents(filename):
    """
        Pre: The list in xls file is not empty
        Post: All students are extract from file
        Returns students list
    """
    list = []
    try:
        # open Excel file
        wb = xlrd.open_workbook(str(filename))
    except IOError:
        print ("Oops! No file "+filename+ " has been found !")
    else:
        sh = wb.sheet_by_name(wb.sheet_names()[0])
        for rownum in range(1,sh.nrows):#1 to remove title line
            student = sh.row_values(rownum)
            list.append(student)
    return list

import sys,getopt,random,xlrd

def main(argv):
   filename = ''
   n = -1
   student = []
   try:
      options, remainder = getopt.getopt(sys.argv[1:], 'f:n:', ['--file=','--number='])
   except getopt.GetoptError:
      print (sys.argv[0] + ' -f <filename> -n <numberOfName>')
      sys.exit(2)
   else:
       for opt, arg in options:
        if opt == '-h':
            print (sys.argv[0] + '-f <filename> -n <numberOfName>')
            sys.exit()
        elif opt in ("-f", "--file"):
            filename = str(arg)
        elif opt in ("-n", "--number"):
            n = int(arg)
   if filename!='' and n!=-1:
       students = extractStudents(filename)
       if (len(students)<n):
           print('No need to launch program because you have only '+str(n)+' students')
           sys.exit()
       else:
           i = len(students)-n
           while i < len(students): #Get students to student & Remove n students
            k = len(students)-1
            l = random.randint(0,k)
            student.append(students[l])#add student selected
            del students[l]#Remove this student from the list
           print("Les candidats pour les elections sont : ")
           for candidat in student:
               print (candidat[0], candidat[1])
   else:
       print('error occured')
       sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])
