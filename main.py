# Created by Ahmed ElSaeed
# Telegram: @asmprotk
# GitHub: @asmpro7

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))
actions = {
    "Volume up":["Images/up.png", {"method": "up", "parameters": []}],
    
    "Volume down":["Images/down.png", {"method": "down", "parameters": []}],
    
    "Maximum Volume": ["Images/max.png", {"method": "max", "parameters": []}],
    
    "mute":  ["Images/mute.png", {"method": "mute", "parameters": []}],
    
    "unmute": ["Images/unmute.png", {"method": "unmute", "parameters": []}],
    
}

from flowlauncher import FlowLauncher
import subprocess

class VolumeFlow(FlowLauncher):

    def query(self, query):
        results=[]
        # if query == "up":
        #     subprocess.run(f"nircmd.exe changesysvolume 10000")
        # elif query == "down":
        #     subprocess.run(f"nircmd.exe changesysvolume -10000")
        # elif query == "max":
        #     subprocess.run(f"nircmd.exe changesysvolume 65535")
        # elif query == "mute":
        #     subprocess.run(f"nircmd.exe mutesysvolume 1")
        # elif query == "unmute":
        #     subprocess.run(f"nircmd.exe mutesysvolume 0")
        # elif query.isdigit():
        #     value=65535*int(query)/100
        #     subprocess.run(f"nircmd.exe changesysvolume -65535")
        #     subprocess.run(f"nircmd.exe changesysvolume {value}")
        if True:
            user_input = [item for item in actions.keys() if query.strip().lower() in item.strip().lower()]
            for action in user_input:
                results.append({
                    "title": action,
                    "IcoPath": actions[action][0],
                    "JsonRPCAction": actions[action][1]
                })
                
            


        return results
    def up(self):
        subprocess.run(f"nircmd.exe changesysvolume 10000") 
    def down(self):
        subprocess.run(f"nircmd.exe changesysvolume -10000") 
    def max(self):
        subprocess.run(f"nircmd.exe changesysvolume 65535") 
    def mute(self):
        subprocess.run(f"nircmd.exe mutesysvolume 1") 
    def unmute(self):
        subprocess.run(f"nircmd.exe mutesysvolume 0") 

if __name__ == "__main__":
    VolumeFlow()
