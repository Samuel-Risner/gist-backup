from misc import get_answer, save_url


def add_url():
    while True:
        print("Please enter the URL for the gist:\n"
              "(URLs should be formatted as such: https://gist.githubusercontent.com/{username}/{gist id}/raw/{commit "
              "id}/{file name})\n"
              "(https://gist.githubusercontent.com/xxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/raw"
              "/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxx)\n"
              "(Use the 'Clone via HTTPS' option)")

        url = input("> ").strip()
        print()

        print(f"The URL is: '{url}'")

        if not get_answer("Is this correct?"):
            continue

        parts = url.split("/")

        if (
                (len(parts) != 8) or
                parts[0] != "https:" or
                parts[1] != "" or
                parts[2] != "gist.githubusercontent.com" or
                parts[5] != "raw"
        ):
            print("The entered URL is invalid!\n")
            continue

        save_url(f"{parts[0]}//{parts[2]}/{parts[3]}/{parts[4]}/{parts[5]}", parts[7])
        return
