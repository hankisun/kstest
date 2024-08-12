body = ""

for r in range(1,2):
    body += "<tr>"
    body += "<th width=\"50\">No.</th>"
    for c in range(1,3):
        body += f"<th>seq_{c}</th>"
    body += "</tr>"
for r in range(1,3):
    body += "<tr>"
    body += f"<td>{str(r)}</td>"
    for c in range(1,3):
        src = rf"D:\Photo\My Memories\2023-02-01 가족사진\가족 ({c}).JPG"
        body += f"<td><img src=\"{src}\" width=\"300\" height=\"200\"></td>"
    body += '</tr>'


doc = f"""<html>
<style>
table, th, td {{
  border:1px solid black;
  border-collapse: collapse;
}}
</style>
<table>
{body}
</table>
</html>
"""

with open(r'D:\aaa.html', 'w', encoding='utf-8') as f:
    f.write(doc)