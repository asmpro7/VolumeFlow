# Created by Ahmed ElSaeed
# Telegram: @asmprotk
# GitHub: @asmpro7

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import subprocess

class VolumeFlow(FlowLauncher):

    def query(self, query):
        results=[]
        if query == "up":
            subprocess.run(f"nircmd.exe changesysvolume 10000")
        elif query == "down":
            subprocess.run(f"nircmd.exe changesysvolume -10000")
        elif query == "max":
            subprocess.run(f"nircmd.exe changesysvolume 65535")
        elif query == "mute":
            subprocess.run(f"nircmd.exe mutesysvolume 1")
        elif query == "unmute":
            subprocess.run(f"nircmd.exe mutesysvolume 0")
        else:
            results.append({
                    "Title": "Volume up",
                    "IcoPath": f"Images/up.png",
                    "JsonRPCAction": {"method": "up", "parameters":[]  }
                    })
            results.append({
                    "Title": "Volume down",
                    "IcoPath": f"Images/down.png",
                    "JsonRPCAction": {"method": "down", "parameters":[]  }
                    })
            results.append({
                    "Title": "Maximum Volume",
                    "IcoPath": f"Images/max.png",
                    "JsonRPCAction": {"method": "max", "parameters":[]  }
                    })
            results.append({
                    "Title": "mute",
                    "IcoPath": f"Images/mute.png",
                    "JsonRPCAction": {"method": "mute", "parameters":[]  }
                    })
            results.append({
                    "Title": "unmute",
                    "IcoPath": f"Images/unmute.png",
                    "JsonRPCAction": {"method": "unmute", "parameters":[]  }
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
