# UpBox
UpBox is a free hacking tool that allow you to hack while messaging your server or team.

watch the [demo here](https://youtu.be/NeTSSWEfYNs)
this verision has very cool features like multiple themes or multiple servers etc. [python-3.10](https://www.python.org/downloads/release/python-3100/) is required for this tool and its important that you dont mess with the json files if you want to make a theme. to install UpBox just download it and then on the terminal with the dir and then run `pip install -r requirements.txt`
once all the libraries are installed just run: `python main.py`. and for linux: `python3 main.py`. just wait for it to load and you should see this:

![1](https://user-images.githubusercontent.com/103524696/196044847-f4e0ec47-83c0-4984-8851-cf53c2544e2a.PNG)

enter your desired name and it should close the script. re run it again and you should see this:

![2](https://user-images.githubusercontent.com/103524696/196044979-5f67ad8e-bf1d-4fa2-99d5-37d24837c86e.PNG)

hit enter and the you will see this:
![3](https://user-images.githubusercontent.com/103524696/196045117-2637afd6-f828-4072-9ae5-c55f0a09b61f.PNG)

you can navigate using the arrow keys (`↑`){`↓`)

if you want to create a custom theme. all you need to do so all you need is to go to the **themes** folder make a new **Folder** with your desired name and inside the folder create a **theme.json**
```
{
    "theme":[
        {
            "bg": "black",
            "fg": "white"//startup color
        }
    ],

    "client":[
        {
            "client color": "white", //your messaging color
            "server color": "red"//the servers messaging color
        }
    ]
}
```

 and a **theme.pys** file

```
{
    "theme":[
        {
            "name": "your theme name",
            "description": "your theme description"
        }
    ]
}
```
once that is done. then edit the **themes.list**
```
default
matrix
your theme name
```

and just load it in the terminal.

if you want to add a server. its pretty similar to the theme.
all you need to do is on the **servers** folder and create a **servername.srv**
```
ip:port
```
and a **servername.json**
```
{
    "server":[
        {
            "address": "ip:port",
            "description": "server description"
        }
    ]
}
```

