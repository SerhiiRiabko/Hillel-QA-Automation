import re

html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>
'''

pattern = r'<div\s+id="(\w+)">\s*<a\s+href="(\S+)">\s*(\w+)\s*'

matches = re.findall(pattern, html_code)

results = [(match[0], match[1], match[2]) for match in matches]

print(results)