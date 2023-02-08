import os
from bs4 import BeautifulSoup

string_to_replace = """<a class="nav-link" href=".">
         Home
        </a>
</li>
<li class="navbar-item">
<a class="nav-link" href="./About">
         About Me
        </a>
</li>
<li class="navbar-item">
<a class="nav-link" href="./Blog">
         Blogs
        </a>
</li>
<div class="btn-group">
<li class="nav-item dropdown">
<a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" id="navbarDropdownMenuLink">
          My Projects
         </a>
<div aria-labelledby="navbarDropdownMenuLink" class="dropdown-menu">
<a class="dropdown-item" href="https://github.com/parrt/msds692/blob/master/hw/search.md">
           Search Engine
          </a>
<a class="dropdown-item" href="https://github.com/parrt/msds692/blob/master/hw/recommender.md">
           Recommender
          </a>
<a class="dropdown-item" href="https://github.com/Sadamingh/Projects/blob/main/Android%20Dev/UserManual.md">
           Android APP
          </a>
<a class="dropdown-item" href="./About/notes/gRPC.pdf">
           Distributed FS
          </a>
<a class="dropdown-item" href="./About/">
           Read More
          </a>
</div>
</li>
</div>
</ul>
</div>
</nav>
</div>
</section>
"""

string_after_replace = """<a class="nav-link" href="../../..">
         Home
        </a>
</li>
<li class="navbar-item">
<a class="nav-link" href="../../../About">
         About Me
        </a>
</li>
<li class="navbar-item">
<a class="nav-link" href="../../../Blog">
         Blogs
        </a>
</li>
<div class="btn-group">
<li class="nav-item dropdown">
<a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" id="navbarDropdownMenuLink">
          My Projects
         </a>
<div aria-labelledby="navbarDropdownMenuLink" class="dropdown-menu">
<a class="dropdown-item" href="https://github.com/parrt/msds692/blob/master/hw/search.md">
           Search Engine
          </a>
<a class="dropdown-item" href="https://github.com/parrt/msds692/blob/master/hw/recommender.md">
           Recommender
          </a>
<a class="dropdown-item" href="https://github.com/Sadamingh/Projects/blob/main/Android%20Dev/UserManual.md">
           Android APP
          </a>
<a class="dropdown-item" href="../../../About/notes/gRPC.pdf">
           Distributed FS
          </a>
<a class="dropdown-item" href="../../../About/">
           Read More
          </a>
</div>
</li>
</div>
</ul>
</div>
</nav>
</div>
</section>
"""


indexes = []

for root, subdirs, files in os.walk("./"):
    # if root == "./":
    #     indexes.append("./index.html")
    #     continue
    # if ".git" not in root:
    #     if "index.html" in files:
    #         indexes.append(root + "/index.html")
    if root.startswith("./Blog/posts"):
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
