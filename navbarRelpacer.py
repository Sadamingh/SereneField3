import os
from bs4 import BeautifulSoup

string_to_replace = """<li class="nav-item dropdown">
<a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" id="navbarDropdownMenuLink">
Projects
</a>
<div aria-labelledby="navbarDropdownMenuLink" class="dropdown-menu">
<a class="dropdown-item" href="#">
Project_1
</a>
<a class="dropdown-item" href="#">
Project_2
</a>
<a class="dropdown-item" href="#">
Project_3
</a>
</div>
</li>
<li class="nav-item dropdown">
<a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" id="navbarDropdownMenuLink">
Interesting Links
</a>
<div aria-labelledby="navbarDropdownMenuLink" class="dropdown-menu dropdown-menu-end">
<a class="dropdown-item" href="#">
Link_1
</a>
<a class="dropdown-item" href="#">
Link_2
</a>
<a class="dropdown-item" href="#">
Link_3
</a>
</div>
</li>
"""

string_after_replace = """<li class="nav-item dropdown">
<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
My Projects
</a>
<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
<a class="dropdown-item" href="https://github.com/parrt/msds692/blob/master/hw/search.md">Search Engine</a>
<a class="dropdown-item" href="https://github.com/parrt/msds692/blob/master/hw/recommender.md">Recommender</a>
<a class="dropdown-item" href="https://github.com/Sadamingh/Projects/blob/main/Android%20Dev/UserManual.md">Android APP</a>
<a class="dropdown-item" href="./About/notes/gRPC.pdf">Distributed FS</a>
<a class="dropdown-item" href="./About/">Read More</a>
</div>
</li>
"""


indexes = []

for root, subdirs, files in os.walk("./"):
    if root == "./":
        indexes.append("./index.html")
        continue
    if ".git" not in root:
        if "index.html" in files:
            indexes.append(root + "/index.html")

for n, filename in enumerate(indexes):

    print(len(indexes) - n, filename)

    with open(filename, "r") as fp:
        content = fp.readlines()
        content = [i.strip() for i in content]
        content = [i + "\n" for i in content]
        content = "".join(content)
        content = content.replace(string_to_replace, string_after_replace)

    soup = BeautifulSoup(content, "html.parser")
    content = soup.prettify()

    with open(filename, "w") as fp:
        fp.write(content)
