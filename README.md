# algorithms_animation
> Animation of algorithmic tasks

https://user-images.githubusercontent.com/20164138/206535283-4edfd25e-a246-4e28-901c-387b798e70b3.mp4

## Installation

To successfully install manim, you have to install a few dependencies. Follow the guide:
[manim](https://github.com/ManimCommunity/manim)

Create and activate a virtual environment in the root directory
```sh
python3 -m venv venv
source venv/bin/activate
```
To install the project's packages, type the following command:
```sh
pip3 install -r requirements.txt
```

## Usage
To view the particular algorithm animation (for example, reverse_list), run the following command 
in your terminal
```sh
manim -p -qm src/reverse_linked_list/reverse_list.py ReverseList
```
Your native video player will pop up and play your animation.
