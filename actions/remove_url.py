from misc import get_urls, delete_url, get_answer


def remove_url():
    urls = get_urls()

    if len(urls) == 0:
        print("There are no URLs!\n")
        return

    text = "What URL would you like to remove?"

    for i in range(0, len(urls), 1):
        text += f"\n\t({i}) URL: '{urls[i]['url']}' name: '{urls[i]['name']}'"

    print(text)

    while True:
        index = input("> ").strip()

        try:
            index = int(index)
        except ValueError:
            print("Please enter a number!")
            continue

        if index >= len(urls):
            print("Please enter a valid number!")
            continue

        if not get_answer("Are you sure?"):
            print()
            return

        delete_url(index)
        return
