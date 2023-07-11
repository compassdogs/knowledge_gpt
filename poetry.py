import subprocess

def setup():
    subprocess.run(["poetry", "install"], check=True)

if __name__ == "__main__":
    setup()
    subprocess.run(["streamlit", "run", "knowledge_gpt/main.py"])
