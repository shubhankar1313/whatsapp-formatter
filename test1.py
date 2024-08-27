text = """
10/06/24, 4:47 pm - Event 1 details here.
11/06/24, 4:49 pm - Event 2 details here.
13/06/24, 7:30 pm - Event 3 details here.
18/06/24, 12:32 pm - Event 4 details here.
"""

actual_text = """
14/06/24, 10:18\u202fpm - Gunjan Aggarwal (Client): this whole went out of focus and the other views have grains next time lets use my camera.
18/06/24, 1:03\u202fpm - Gunjan Aggarwal (Client): We need to make sure every shot is clear.
11/06/24, 9:35\u202fpm - Gunjan Aggarwal (Client): We will try to wrap it up by 4.
11/06/24, 4:47\u202fpm - Shubhankar Nath: Yeah actually, that would be better.
11/06/24, 4:48\u202fpm - Gunjan Aggarwal (Client): https://www.instagram.com/reel/C8CImraP1vi/?igsh=MXI2NXYxdXU0d2tpOQ==.
"""

file = open("sample_client.txt", "r", encoding="utf8")
content=file.readlines()
print(content)
file.close()

import re

# # Sample text containing date-time patterns
# text = """
# 10/06/24, 4:47 pm - Event 1 details here.
# 11/06/24, 4:49 pm - Event 2 details here.
# 13/06/24, 7:30 pm - Event 3 details here.
# 18/06/24, 12:32 pm - Event 4 details here.
# """

# Regular expression pattern to match the date-time string
pattern = r'\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\u202f?[ap]m - (.*?)\n'

# Find all matches using the pattern
matches = re.findall(pattern, actual_text, re.DOTALL)

# Print the results
for i, match in enumerate(matches, 1):
    print(f"Event {i}: {match.strip()}")
