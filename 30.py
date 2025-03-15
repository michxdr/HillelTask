import re

def remove_html_tags(input_file, output_file="cleaned.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    html_content = re.sub(r'<script.*?>.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?>.*?</style>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<meta.*?>', '', html_content)
    html_content = re.sub(r'<link.*?>', '', html_content)
    html_content = re.sub(r'<[^>]+>', '', html_content)

    html_content = re.sub(r'\s+', ' ', html_content)  # заміняємо кілька пробілів на один
    html_content = re.sub(r'([^\n])\n([^\n])', r'\1 \2', html_content)  # прибираємо непотрібні розриви між словами

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content.strip())

remove_html_tags("draft.html")
