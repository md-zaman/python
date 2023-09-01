import subprocess


# subprocess.call  # Thses are old method
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

completed = subprocess.run(["ls"])
print("args", completed.args)
print("returncode", completed.args)
print("stdout", completed.stdout)



