# launch server
server:
    # cd www
    python3 -m http.server

# Generate index.html from template with jinja2-cli
gen_html:
    jinja2 template/index.html template/data.json -o www/index.html
