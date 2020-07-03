import pyautogui
import appJar


def buttonPress(button):
    if(button == "Go"):
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        if button == "Right click":
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button)



app = appJar.gui("Autoclicker for Butts")
app.setSize("500x400")
app.setSticky("new")
app.addLabel("Enter amount of clicks", row=0)
app.addEntry("amount", row=1)
app.addButton("Go", buttonPress, row=3)
app.setSticky("e")
app.radioButton("click", "Right click", row=2)
app.setSticky("w")
app.radioButton("click", "Left click", row=2)

app.go()

