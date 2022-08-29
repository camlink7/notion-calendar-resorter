from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
i

assignments = []

name_class = "cell-title"
class_class = "cell-;bwx"
due_date_class = "cell-hWhl"
type_class = "cell-UfRw"

export_file_path = 'AssignmentsExport.html'
soup = BeautifulSoup(open(export_file_path, encoding='utf8').read(), 'html.parser')

table = soup.find("tbody")
table_rows = table.findChildren("tr")

#HELPERS
def create_assignment_element(assignment):
    pass

#Note: Partition should be an array with a length of at least 2
def quicksort(partition):
    pivot = len(partition) - 1
    lo = 0
    hi = pivot - 1

    while lo < hi:
        if (partition[lo] > partition[hi]):
            part_lo = partition[lo] #temp partition lo variable
            partition[lo] = partition[hi]
            partition[hi] = part_lo
        lo += 1
        hi -= 1
    pivot = lo #can be set to either lo or hi
    return quicksort(partition[0:pivot+1]) partition[pivot+1:len(partition)]]

#--------------------------------------------------------------------------

#Collect all the assignments and store them as dictionaries in array
for row in table_rows:
    assignments.append({
        "name": row.find("td", {"class": name_class}).find("a").text,
        "class": row.find("td",  {"class": class_class}).find("span").text,
        "due_date": row.find("td", {"class": due_date_class}).find("time").text,
        "type": row.find("td", {"class": type_class}).find("span").text
    })

#Convert the assignment's date to datetime objects for comparison
for assn in assignments:
    assn_due_no_at = assn['due_date'].split("@")[1]
    assn_due_chunked = assn_due_no_at.split(" ")
    due_date = None
    if 'AM' in assn_due_chunked or 'PM' in assn_due_chunked:
        due_date = (assn_due_chunked[0] + " " + assn_due_chunked[1] + " " + assn_due_chunked[2] + " " + assn_due_chunked[3] + assn_due_chunked[4])
    else:
         due_date = (assn_due_chunked[0] + " " + assn_due_chunked[1] + " " + assn_due_chunked[2])
    assn['due_date'] = parser.parse(due_date)

#Sort the assignment array based on due date comparison (Using Quicksort Algorithm)
sorted_assns = []
for assn in assignments:
    pass



print(quicksort([5, 2, 0, 6, 1, 3]))