# app.py

import subprocess
import sys

def setup():
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    subprocess.run([sys.executable, "-m", "knowledge_gpt.main"])

if __name__ == "__main__":
    setup()

