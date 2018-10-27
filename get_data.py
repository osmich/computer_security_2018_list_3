import sys
import subprocess

file_name = 'data'
cmd = ['tshark', '-w', file_name]
result = subprocess.run(cmd, stdout=subprocess.PIPE)