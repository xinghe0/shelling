import datetime
import os
import subprocess
import shutil

filepath = '.'
for i in os.listdir(filepath):
	if i[-4:] == '.dex':
		if i[-12:] != '_patched.dex':
			cmd = ["dp", "fix", "-d", i, "-j", i[:-4]+"_class.json", "--nolog"]
			print("cmd:", cmd)
			try:
				output = subprocess.check_output(cmd)
			except Exception as e:
				print(e)
print("dex修复完成")

dexdir = datetime.datetime.now().strftime('%Y-%m-%d')
os.mkdir(dexdir)
for i in os.listdir(filepath):
	if i[-12:] == '_patched.dex':
		src = os.path.join(filepath, i)
		dst = os.path.join(dexdir, i)
		shutil.move(src, dst)

print("dex in " + dexdir)

