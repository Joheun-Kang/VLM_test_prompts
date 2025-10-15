# qwenvl8-b promt 

# this is good 
prompt1 = """
extract notes section from image as it is.
"""

# this works great on 

prompt2 = """
extract notes section from image and return format like {'notes': "\n1. intertpret....\n 2.refer...}.
"""

# works well for notes and tube table 
prompt3 = """
There are four tasks to do. For all tasks, do not change any charaters and keep special characters as it is.
1. Extract notes section information from image and format like {'notes': "\n1. intertpret....\n2.refer..."}. you must add newline symbol "\n" before the enumerated number.
2. Find the notes section's coordinates with page number (1-based) like
 {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}
3. Extract tube data table. For a table with 7 columns, the return structure should resemble this:
```html 
<table> 
	<caption> TUBE DATA TABLE<caption> 
	<thread>
		<tr>
			<th>STOCK NO.</th>
			<th>SEGMENT </th>
			<th>BEND # </th>
			<th>OFFSET </th>
			<th>TWIST(R)</th>
			<th>ANGLE </th>
			<th>ANGLES</th>
			<th>Radius</th>	
		<tr>
	</thread>
	<tbody>
		<tr>
			<td>TS-320</td>
			<td>3</td>
			<td>1.4</td>
			<td>2.0</td>
			<td>0.0</td>
			<td>24</td>
			<td>21</td>
			<td>3.5</td>
		<tr>
	</tbody>
</table> 
```
4. Find the tube data table's coordinates with page number (1-based) like
 {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}.

put note section information to "notes" and it's coordinates to "notes_location".
put tube data table information to "tube_table_data" and its coordinate to "tube_table_location". 
{"notes":, 'notes_location': , 'tube_table_data': , 'tube_table_location': }

Return a sinlge JSON object, and  Do not change any skeleton JSON format.

"""
# best results
prompt_3_1= """
YOUR GOAL: Extract ALL required data from the image and output a SINGLE, VALID JSON object. Do not output any text, explanation, or code block markers (like ```json).

--- INSTRUCTIONS ---
1. Extract notes section text. For each enumerated item, start with a newline character: "\n1. ...", "\n2. ...".
2. Find the notes section coordinates with page number (1-based) like {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max': <float:0-1>}.
3. Extract the tube data table. **CRITICAL: Format the entire HTML output as a single, continuous string. REMOVE all newline characters (\\n), tab characters (\\t), and excessive spaces from the HTML string before putting it into the JSON field.**
   Use the corrected HTML structure with <thead> and </tr> tags.
4. Find the tube data table coordinates with page number (1-based) like {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max': <float:0-1>}.

--- JSON SKELETON (FILL THIS IN) ---
{
"notes": "[Your Notes Text Here]",
"notes_location": [Your Notes Location Object Here],
"tube_table_data": "[Your SINGLE-LINE HTML Table String Here]",
"tube_table_location": [Your Table Location Object Here]
}

--- OUTPUT FORMAT ---
Start with the opening brace '{' and end with the closing brace '}' of the JSON object. Do not include any surrounding text, comments, or markdown formatting (e.g., no ```json).

{
"""


# # ['```json\n[\n    {"page": 1, "x_min": 0.14, "y_min": 0.37, "x_max": 0.48, "y_max": 0.82},\n    {"page": 1, "x_min": 0.57, "y_min": 0.44, "x_max": 0.73, "y_max": 0.77},\n    {"page": 1, "x_min": 0.57, "y_min": 0.13, "x_max": 0.73, "y_max": 0.32}\n]\n```']
# prompt4 = """
# Goal: you sole objective is to perform a meticulously detailed and 100% verbatim extraction of bounding boxes of all possible manufacturing parts in this image.

# Each parts' format should be  {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}, and page number is 1-based.

# This task demands absolute precision and has zero tolerance for deviation, summariztion, or interpretation. 
# """ 

## Best format for part image extraction! (10/14)
# ['{"page": 1, "x_min": 0.57, "y_min": 0.18, "x_max": 0.83, "y_max": 0.54}, {"page": 1, "x_min": 0.13, "y_min": 0.54, "x_max": 0.48, "y_max": 0.83}, {"page": 1, "x_min": 0.57, "y_min": 0.54, "x_max": 0.72, "y_max": 0.78}']
prompt4_1_image_bbox_extraction = """
Goal: you sole objective is to perform a meticulously detailed and 100% verbatim extraction of bounding boxes of all distinct images of the engineering part in this image.

Each parts' format should be  {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}
Page number is 1-based.
This task demands absolute precision and has zero tolerance for deviation, summariztion, or interpretation. 

Perfect output format is like 
"{"page": 1, "x_min": <float:0-1> , "y_min":  <float:0-1>, "x_max": <float:0-1>, "y_max": <float:0-1>}\n{"page": 1, "x_min": <float:0-1>, "y_min": <float:0-1>, "x_max": <float:0-1>, "y_max": <float:0-1>}\n{}...}
""" 

prompt4_1_image_bbox_extraction_2 ="""
Goal: Your **ABSOLUTE SOLE OBJECTIVE** is to perform a 100% verbatim extraction of bounding boxes for **ALL DISTINCT DRAWING VIEWS** of the mechanical part in this image.

**Definition of a Bounding Box for a Drawing View (Non-Negotiable):**
For each unique drawing view (orthographic, isometric, sectional, or detail), the bounding box **MUST** encompass the **ABSOLUTE MAXIMUM RECTANGULAR AREA DEFINED BY THE VIEW'S EXTREMITIES.** This means the box must be drawn around the outermost elements of the entire view, including:

1.  **PART GEOMETRY:** All visible, hidden, and center line geometry.
2.  **DIMENSION SYSTEM:** The bounding box MUST extend to the furthest point of **ANY** dimension line, extension line, arrow, or their corresponding text/tolerances. **If a dimension line is drawn far from the part, the bounding box must still include the entire length of that dimension line and its text.**
3.  **LEADERS/CALLOUTS:** All leader lines, arrows, and the text of any callout associated with the view.
4.  **LABELS/TITLES:** All associated view labels, titles, and section identifiers (e.g., "VIEW A", "SECTION B-B").

**CRITICAL INSTRUCTIONS FOR BOUNDING BOX EXTENT:**
* **ZERO CLIPPING TOLERANCE:** The bounding box is absolutely forbidden to clip, truncate, or cut off any part of the drawing view, its geometry, dimension lines, extension lines, arrows, or associated text/labels.
* **OVERLAPPING IS MANDATORY IF REQUIRED:** Bounding boxes **ARE PERMITTED TO OVERLAP** (and expected to) if views or their elements are close. Do not shrink any box to prevent overlap.
* **PRIORITIZE DIMENSION LINES:** When in doubt about the box's edge, always extend it further to ensure all dimension text and line work is contained.

Each part's format should be  {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}
Page number is 1-based.

This task demands absolute precision and has zero tolerance for deviation, summarization, or interpretation.

Perfect output format is a newline-separated list of JSON objects:
{"page": 1, "x_min": <float:0-1> , "y_min":  <float:0-1>, "x_max": <float:0-1>, "y_max": <float:0-1>}
{"page": 1, "x_min": <float:0-1>, "y_min": <float:0-1>, "x_max": <float:0-1>, "y_max": <float:0-1>}
{}...
"""

# # why this does not work? 
# prompt5 = """
# Goal: you sole objective is to perform a meticulously detailed and 100% verbatim extraction of bounding boxes of all possible part drawings in this image.
# Each part drawing's  format should be  {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}, and 
# if there are multiple parts, then the final output shoule be 
# {1:{'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}, 2 :{'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>} ,...}
# This task demands absolute precision and has zero tolerance for deviation, summariztion, or interpretation. 
# """ 

# # why this does not work? 
# prompt4_2 = """
# Goal: you sole objective is to perform a meticulously detailed and 100% verbatim extraction of bounding boxes of all possible manufacturing parts in this image.
# This task demands absolute precision and has zero tolerance for deviation, summariztion, or interpretation. 

# Each parts' bounding box format should be  
# {'page': <integer> ,"x_min":<float:0-1>, "y_min":<float:0-1>, "x_max":<float:0-1>, "y_max": <float:0-1>}, and page number is 1-based.

# If there are mutiple parts' image, make a single list with that skeleton format. 
# """ 


# ['```json\n{\n  "notes": "1. INTERPPT DIMENSIONING AND TOLERANCING PER ASME Y14.5 2018. 2. REFERENCE TITLE BLOCK FOR MATERIAL AND FINISH. 3. MINIMUM SURFACE FINISH OF (23) UNLESS OTHERWISE SPECIFIED 4. DIMENSIONS NOTED WITH A O REQUIRE SUPPLIER INSPECTION PER CUSTOMER APPROVED SAMPLING PLAN. CERTIFICATE OF COMPLIANCE REQUIRED WITH EACH PART SHIPMENT 5. MATERIAL CERTIFICATION REQUIRED WITH EACH FART SHIPMENT 8. BAG AND TAG PARTS TOR SHIPMENT (OTY 10 PER BAG)",\n  "tube_table_data": "<table> <caption> TUBE DATA TABLE</caption> <thread> <tr> <th>STOCK NO.</th> <th>SEGMENT </th> <th>BEND # </th> <th>OFFSET </th> <th>TWIA(R)</th> <th>ANGLE </th> <th>ANGLES</th> <th>Radius</th> </tr> </thread> <tbody> <tr> <td>TS-1001</td> <td>1.1</td> <td>1</td> <td>0.0</td> <td>0.0</td> <td>45</td> <td>43</td> <td>1.5</td> </tr> <tr> <td>TS-1001</td> <td>2.0</td> <td>2</td> <td>15.0</td> <td>15.0</td> <td>-175</td> <td>-10.5</td> <td>2.0</td> </tr>']
