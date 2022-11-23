import subprocess

# subprocess.run(["chmod", "video_writer.sh"])
print(subprocess.run(["video_writer.sh"], shell=True))
