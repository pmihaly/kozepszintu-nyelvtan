import os

tant = input("Tantárgy neve: ").lower()
kozepszint = True if input("Középszint [i/n]: ").lower() == "i" else False
tant = f"{'Középszintű' if kozepszint else 'Emelt szintű'} {tant}"

CONFIG_FILE = f"""theme: jekyll-theme-cayman
title: {tant.title()} Érettségi Tételek
plugins:
  - jekyll-relative-links
relative_links:
  enabled: true
  collections: true
include:
  - CONTRIBUTING.md
  - README.md
  - LICENSE.md
  - COPYING.md
  - CODE_OF_CONDUCT.md
  - CONTRIBUTING.md
  - ISSUE_TEMPLATE.md
  - PULL_REQUEST_TEMPLATE.md"""

README = "{% for page in site.pages %} [{{ page.title }}](/" + tant.replace(
    " ", "-").lower().replace("é", "e").replace("á", "a").replace("í", "i").replace("ő", "o").replace("ü", "u").replace("ó", "o").replace("ú", "u").replace("ű", "u") + "/{{ page.url }}) {% endfor %}"

with open("_config.yml", "w") as config_file, open("README.md", "w") as readme:
    config_file.write(CONFIG_FILE)
    readme.write(README)

os.remove("setup.py")
