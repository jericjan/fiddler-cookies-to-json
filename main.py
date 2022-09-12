import os

def main():    
    domain = input("What is your domain?\n> ")    
    if not os.path.exists("fiddler_cookies.txt"):
        with open("fiddler_cookies.txt", "w", encoding="utf-8") as f:
            f.write("")
        print("fiddler_cookies.txt created!")
        print('"Copy Header" from Fiddler and paste it there.')
        return
    with open("fiddler_cookies.txt",encoding="utf-8") as f:
        text = f.read()
    if text:
        if text.startswith("Cookie: "):
            text = text[8:]
        text = text.split(";")
        text = [x.strip("\n").strip() for x in text]
        mihoyo_json = []
        for x in text:
            item, value = x.split("=")
            temp_json = {}
            temp_json["domain"] = domain
            temp_json["name"] = item
            temp_json["value"] = value
            mihoyo_json.append(temp_json)

        with open("cookies.json", "w", encoding="utf-8") as f:
            f.write(str(mihoyo_json).replace("'", '"'))
        with open("fiddler_cookies.txt", "w", encoding="utf-8") as f:
            f.write("")
        print("cookies.json created!")
        print(
            "You can now import this to Cookie-Editor (https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en)."
        )
        print(
            "If it fails, paste to https://jsonformatter.curiousconcept.com/# to fix it."
        )
        print("Also don't forget to correct the user-agent. It might need it like Honkai does.")
    else:
        print("fiddler_cookies.txt is empty")


if __name__ == "__main__":
    main()
