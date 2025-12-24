# launch server
server:
    python3 -m http.server --directory www/

# Generate all HTML page form templates with jinja2-cli
gen-html:
    @jinja2 template/presentation.html.jinja template/datas/presentation.json -o www/index.html
    @echo "presentation  ✅"
    @jinja2 template/day.html.jinja template/datas/day_1.json -o www/public/days/day_1.html
    @echo "day 1         ✅"
    @jinja2 template/day.html.jinja template/datas/day_2.json -o www/public/days/day_2.html
    @echo "day 2         ✅"
    @jinja2 template/day.html.jinja template/datas/day_3.json -o www/public/days/day_3.html
    @echo "day 3         ✅"
    @jinja2 template/day.html.jinja template/datas/day_4.json -o www/public/days/day_4.html
    @echo "day 4         ✅"
    @jinja2 template/day.html.jinja template/datas/day_5.json -o www/public/days/day_5.html
    @echo "day 5         ✅"
    @jinja2 template/day.html.jinja template/datas/day_6.json -o www/public/days/day_6.html
    @echo "day 6         ✅"
    @jinja2 template/day.html.jinja template/datas/day_7.json -o www/public/days/day_7.html
    @echo "day 7         ✅"
    @jinja2 template/day.html.jinja template/datas/day_8.json -o www/public/days/day_8.html
    @echo "day 8         ✅"
    @jinja2 template/day.html.jinja template/datas/day_9.json -o www/public/days/day_9.html
    @echo "day 9         ✅"
    @jinja2 template/day.html.jinja template/datas/day_10.json -o www/public/days/day_10.html
    @echo "day 10        ✅"
    @jinja2 template/day.html.jinja template/datas/day_11.json -o www/public/days/day_11.html
    @echo "day 11        ✅"
    @jinja2 template/day.html.jinja template/datas/day_12.json -o www/public/days/day_12.html
    @echo "day 12        ✅"
    @jinja2 template/utils.html.jinja template/datas/utils.json -o www/public/utils.html
    @echo "utils         ✅"
