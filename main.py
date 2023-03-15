import subprocess
import sys
import webbrowser
from urllib.parse import quote
import json

def setupGit():

        git_name = input("Enter your github username for git features: ")
        data["name"] = git_name 
        with open("storage.json", "w") as f:
            json.dump(data,f)



while True:
    input_str = input()

    if input_str.startswith("#"):
        new = 2
        # If it does, simply echo it back to the terminal
        
        if input_str == "# gpt":
            webbrowser.open("https://chat.openai.com/chat")

        
        else:

            base_url = "http://www.google.com/search?q="
                        

            input_str.replace("#","")
            input_str = input_str + " (site:reddit.com OR site:Stackoverflow.com OR site:github.com OR site:www.geeksforgeeks.org)"
            final_url = base_url + quote(input_str)
            webbrowser.open(final_url,new=new)

     
    elif input_str.startswith("!"):
       
        webbrowser.open("https://www.youtube.com/results?search_query="+ input_str.replace("!",""))
    
    elif input_str.startswith("$git"):
        with open("storage.json","r") as f:
            data = json.load(f)

        if data["name"]== "":
            setupGit()
        
        else:
            webbrowser.open("https://github.com/"+data["name"])
    
        
    else:
        # If it doesn't, execute the input as a shell command
        try:
            result = subprocess.run(input_str, shell=True, check=True, stdout=subprocess.PIPE)
            print(result.stdout.decode())
        except subprocess.CalledProcessError as e:
            print("Error:", e, file=sys.stderr)
