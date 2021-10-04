import subprocess
from sys import executable
print(executable)

subprocess.run([executable, '-m', 'sslyze', '--regular', 'www.datai.ai'],)