from asyncio.windows_events import INFINITE
from pydoc import classname
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser

assignments = []

name_class = "cell-title"
class_class = "cell-;bwx"
complete_class = "cell-lR;U"
due_date_class = "cell-hWhl"
type_class = "cell-UfRw"

export_file_path = 'AssignmentsExport.html'
soup = BeautifulSoup(open(export_file_path, encoding='utf8').read(), 'html.parser')

table = soup.find("tbody")
table_rows = table.findChildren("tr")

#HELPERS
def create_assignment_element(assignment):
    new_row = soup.new_tag("tr")

    #name
    name = soup.new_tag("td", **{'class': name_class})
    name.string = assignment['name']
    new_row.append(name)

    #class
    course = soup.new_tag("td", **{'class': class_class})
    course.string = assignment["class"]
    new_row.append(course)

    #complete
    is_complete_class = "checkbox-off"
    if assignment['complete']:
        is_complete_class = "checkbox-on"
    complete = soup.new_tag("td", **{'class': complete_class})
    complete_checkbox = soup.new_tag("div", **{'class': "checkbox " + str(is_complete_class)})
    complete.append(complete_checkbox)
    new_row.append(complete)

    #due date
    due_date = soup.new_tag("td", **{'class': due_date_class})
    due_date.string = assignment["due_date"].strftime("%b %d, %Y @ %I:%M %p")
    new_row.append(due_date)

    #type
    type = soup.new_tag("td", **{'class': type_class})
    type.string = assignment["type"]
    new_row.append(type)


    #append to the main table
    table.append(new_row)



#Note: array must have a length of at least 2
# @array is an array of assignment objects
def selection_sort(array):
    for i in range(len(array)):
        low = i
        for x in range(i + 1, len(array)):
            if array[x]['due_date'] < array[low]['due_date']:
                low = x
        if array[i]['due_date'] > array[low]['due_date']:
            low_value = array[low]
            array[low] = array[i]
            array[i] = low_value
    return array


#--------------------------------------------------------------------------

#Collect all the assignments and store them as dictionaries in array
for row in table_rows:
    is_complete = False
    if ("checkbox-on" in row.find("td", {"class": complete_class}).find("div")['class']):
        is_complete = True

    assignments.append({
        "name": row.find("td", {"class": name_class}).find("a").text,
        "class": row.find("td",  {"class": class_class}).find("span").text,
        "complete": is_complete,
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


table.clear()
#Sort the assignment array based on due date comparison (Using Selection Sort) and create html elements for each
for assn in selection_sort(assignments):
    create_assignment_element(assn)


#Save the modified soup to a new html file
with open("SortedAssignments.html", "w", encoding="utf-8") as file:
    file.write(str(soup.prettify()))