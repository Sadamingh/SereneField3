import os
from bs4 import BeautifulSoup


def main():
    post_list = os.listdir('posts')
    post_list.remove('css')
    post_list.remove('Leetcode')
    post_list.remove('Others')
    post_list.remove('PWN')
    post_list.remove('.DS_Store')
    post_list.remove('image')

    for post_dir in post_list:
        with open("./posts/" + post_dir + "/index.html", "r", encoding='utf-8') as fp:
            soup = BeautifulSoup(fp, "html.parser")
            posts = os.listdir("./posts/" + post_dir)
            posts = [i for i in posts if i.endswith(".html")]
            posts.remove("index.html")
            link_tag = ""
            for post in sorted(posts):
                name = post.replace(".html", "")
                name = name.replace("-", " ")
                name = name.replace("_", " ")
                link_tag += f"<a href=\"./{post}\"><div class=\"post-link\">{name}</div></a>\n<br>\n"
            links = BeautifulSoup(link_tag, 'html.parser')
            pi_section = soup.find("section", {"id": "personal-info"})
            pi_section.clear()
            pi_section.insert(1, links)

        with open("./posts/" + post_dir + "/index.html", "w", encoding='utf-8') as fp:
            fp.write(str(soup))

if __name__ == '__main__':
    main()
