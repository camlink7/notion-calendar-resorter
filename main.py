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

#Collect all the assignments and store them as dictionaries in array
for row in table_rows:
    assignments.append({
        "name": row.find("td", {"class": name_class}).find("a").text,
        "class": row.find("td",  {"class": class_class}).find("span").text,
        "due_date": row.find("td", {"class": due_date_class}).find("time").text,
        "type": row.find("td", {"class": type_class}).find("span").text
    })

#Sort the assignments in the array by due date
assn_due_no_at = assignments[0]['due_date'].split("@")[1]
assn_due_chunked = assn_due_no_at.split(" ")
due_date = (assn_due_chunked[0] + " " + assn_due_chunked[1] + " " + assn_due_chunked[2] + " " + assn_due_chunked[3] + assn_due_chunked[4])
print(parser.parse(due_date))

def create_assignment_element(assignment):
    pass