from asyncio.windows_events import INFINITE
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
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


#Note: array must have a length of at least 2
def selection_sort(array):
    for i in range(len(array)):
        low = i
        for x in range(i + 1, len(array)):
            if array[x] < array[low]:
                low = x
        if array[i] > array[low]:
            low_value = array[low]
            array[low] = array[i]
            array[i] = low_value
    return array


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

#Sort the assignment array based on due date comparison (Using Selection Sort
sorted_assns = []
for assn in assignments:
    pass

print(selection_sort([5, 2, 6, 0, 1, -50]))