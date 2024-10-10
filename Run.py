try:
    import requests, re, time, os, sys, random, string, urllib.parse
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as printf
    from requests_toolbelt import MultipartEncoder
except (ModuleNotFoundError) as e:
    __import__('sys').exit(f"[Error] {str(e).capitalize()}!")

DUMPS = []

class FEATURE:

    def __init__(self) -> None:
        pass

    def MAIN(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        printf(
            Panel(r"""[bold red]     _____       _             _      _       _    
    / ____|     (_)           | |    (_)     | |   
   | |  __  ___  _ _ __ ___   | |     _ _ __ | | __
   | | |_ |/ _ \| | '_ ` _ \  | |    | | '_ \| |/ /
   | |__| | (_) | | | | | | | | |____| | | | |   < 
[bold white]    \_____|\___/|_|_| |_| |_| |______|_|_| |_|_|\_\ 
          [underline green]Google Image To Link - by Rozhak""", width=59, style="bold bright_black")
        )

        printf(
            Panel(f"[bold white]Please fill in the image file you want to search for, make sure it is available in the correct director\ny, for example:[bold green] Temp/Image.jpg[bold white] *[bold red]only input one image!", width=59, style="bold bright_black", title="[bold bright_black]> [ File Gambar ] <", subtitle="[bold bright_black]╭───────", subtitle_align="left")
        )
        self.IMAGES = Console().input("[bold bright_black]   ╰─> ")
        if os.path.exists(self.IMAGES) == True:
            printf(
                Panel(f"[bold white]Do you want to use print from rich module or not, if you want type[bold green] Y[bold white] if not type[bold red] N[bold white]. Consider\nnot using pretty print so the link can be copied!", width=59, style="bold bright_black", title="[bold bright_black]> [ Tampilan ] <", subtitle="[bold bright_black]╭───────", subtitle_align="left")
            )
            self.PRETTY_PRINT = Console().input("[bold bright_black]   ╰─> ")
            if str(self.PRETTY_PRINT.upper()) == "N":
                self.PRINT = False
            else:
                self.PRINT = True
            printf(
                Panel(f"[bold white]You can use CTRL + Z to stop, if the search fails there is likely no exact match, as\nthis only looks for exact matches in the image!", width=59, style="bold bright_black", title="[bold bright_black]> [ Catatan ] <")
            )
            CLASS = CONVERT()
            CLASS.IMAGES(files=self.IMAGES)

            if bool(self.PRINT) == True:
                LOOPING = 1
                for TAUTAN in DUMPS:
                    printf(
                        Panel(f"[bold red]{LOOPING}[bold white]. Link:[bold green] {TAUTAN}", width=59, style="bold bright_black")
                    )
                    LOOPING += 1
                pass
            else:
                LOOPING = 1
                for TAUTAN in DUMPS:
                    if int(LOOPING) == len(DUMPS):
                        print(f"{LOOPING}. Link: {TAUTAN}")
                    else:
                        print(f"{LOOPING}. Link: {TAUTAN}\n")
                    LOOPING += 1
                pass
            printf(
                Panel(f"[bold green]Congratulations![bold white] you have successfully collected[bold red] {len(DUMPS)}[bold white] ex\nact match links from google search by Image!", width=59, style="bold bright_black", title="[bold bright_black]> [ Selesai ] <")
            )
            Console().input("[bold white][[bold green]Selesai[bold white]]")
            sys.exit()
        else:
            printf(
                Panel(f"[bold red]The file you entered is not available, please enter the correct file and make sure the image is available!", width=59, style="bold bright_black", title="[bold bright_black]> [ File Kosong ] <")
            )
            sys.exit()

class CONVERT:

    def __init__(self) -> None:
        pass

    def GENERATE_RANDOM_FILENAME(self, extension="jpg", length=6):
        self.LETTERS = string.ascii_lowercase
        self.RANDOM_NAME = ''.join(random.choice(self.LETTERS) for _ in range(length))

        return f"{self.RANDOM_NAME}.{extension}"

    def IMAGES(self, files):
        with requests.Session() as SESSION:
            SESSION.headers.update(
                {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Host': 'lens.google.com',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'sec-ch-ua-wow64': '?0',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Dest': 'document',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                }
            )
            RESPONSE = SESSION.get('https://lens.google.com/search?hl=in&p=')

            BOUNDARY = '----WebKitFormBoundary' \
                + ''.join(random.sample(string.ascii_letters + string.digits, 16))
            
            data = MultipartEncoder(fields=({
                'encoded_image': (f'{self.GENERATE_RANDOM_FILENAME()}.jpg', open(files, 'rb'), 'image/jpeg'),
                'processed_image_dimensions': (None, '608,879'),
            }), boundary=BOUNDARY)

            self.COOKIES = ('; '.join([str(key) + '=' + str(value) for key, value in SESSION.cookies.get_dict().items()]))
            self.STCS = int(time.time() * 1000)

            SESSION.headers.update(
                {
                    'Content-Type': 'multipart/form-data; boundary={}'.format(BOUNDARY),
                    'Referer': 'https://lens.google.com/',
                    'Cache-Control': 'max-age=0',
                    'Origin': 'https://lens.google.com',
                    'Cookie': '{}'.format(self.COOKIES),
                    'Content-Length': '{}'.format(data.len),
                }
            )

            RESPONSE_2 = SESSION.post('https://lens.google.com/v3/upload?hl=in&stcs={}&vpw=1280&vph=585&ep=subb'.format(self.STCS), data=data)

            self.LENS_WEb = re.search(r',\["(.*?)"\],\["/lens-web-standalone-prod/(.*?)"', str(RESPONSE_2.text))
            self.UX, self.STANDALONE = self.LENS_WEb.group(1), self.LENS_WEb.group(2)
            self.IDS = re.search(r"{id:'(.*?)'", str(RESPONSE_2.text)).group(1)
            self.BL = re.search(r"'(boq_lensfrontendapiserver_\d{8}\.\d{2}_p\d)'", str(RESPONSE_2.text)).group(1)
            self.DATA_HASH = re.search(r'data:\[\["(.*?)",', str(RESPONSE_2.text)).group(1)
            self.UI = re.search(r'"([a-zA-Z0-9_\-]+==)"', str(RESPONSE_2.text).replace('\\u003d', '=')).group(1)

            self.SEARCH_F_SID = re.search(r'"FdrFJe":"(.*?)"', str(RESPONSE_2.text))
            self.F_SID = self.SEARCH_F_SID.group(1) if self.SEARCH_F_SID else ''
            self.SEARCH_OPI = re.search(r'"S6lZl":(\d+),', str(RESPONSE_2.text))
            self.OPI = self.SEARCH_OPI.group(1) if self.SEARCH_OPI else ''

            try:
                self.SIDECHANNEL = str(RESPONSE_2.text).replace('\\u003d', '=').split('"MAE=')[1].split(', sideChannel:')[0]
                self.DETECTED_OBJECT = re.search(r',"(.*?)"\]\]', str(self.SIDECHANNEL)).group(1)
            except (Exception):
                self.URL_FINDER = re.findall(r'<a href="(https://.*?)"', str(RESPONSE_2.text))
                if len(self.URL_FINDER) != 0:
                    for ENCODED_URL in self.URL_FINDER:
                        self.DECODED_URL = urllib.parse.unquote(ENCODED_URL)
                        if 'google' in str(self.DECODED_URL):
                            continue
                        else:
                            DUMPS.append(f'{self.DECODED_URL.replace("amp;", "")}')
                    if len(DUMPS) != 0:
                        return (True)
                    else:
                        printf(
                            Panel(f"[bold red]Sorry, we couldn't find any links or exact matches for this image, please try another image!", width=59, style="bold bright_black", title="[bold bright_black]> [ Empty Link ] <")
                        )
                        sys.exit()
                else:
                    printf(
                        Panel(f"[bold red]Sorry, we couldn't find any links or exact matches for this image, please try another image!", width=59, style="bold bright_black", title="[bold bright_black]> [ Empty Link ] <")
                    )
                    sys.exit()

            params = {
                'source-path': '/search',
                'f.sid': f'{self.F_SID}',
                'soc-device': '1',
                'rpcids': f'{self.IDS}',
                'bl': f'{self.BL}',
                'rt': 'c',
                '_reqid': '69971',
                'hl': 'in',
                'opi': f'{self.OPI}',
                'soc-app': '1',
                'soc-platform': '1',
            }

            data = (
                f'f.req=%5B%5B%5B%22{self.IDS}%22%2C%22%5B%5B%5C%22{self.DATA_HASH}%5C%22%2C1%2C1%5D%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5C%22{self.UX}%5C%22%5D%2C%5B%5C%22%2Flens-web-standalone-prod%2F{self.STANDALONE}%5C%22%2C%5Bnull%2Cnull%2C608%2C879%5D%5D%5D%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C3%2C%5B%5C%22id%5C%22%2Cnull%2C%5C%22US%5C%22%2C%5C%22Asia%2FBangkok%5C%22%5D%2Cnull%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2C%5B%5Bnull%2C1%2C1%2C1%2C1%2C1%2C1%2Cnull%2Cnull%2Cnull%2C1%2C1%2C1%2C1%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C1%2C1%2Cnull%2C1%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2Cnull%2Cnull%2C%5B5%2C6%2C2%5D%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C1%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C1%2Cnull%2Cnull%2C1%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C1%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%5D%2C%5B%5B%5B7%5D%5D%5D%2Cnull%2Cnull%2Cnull%2C26%2Cnull%2Cnull%2Cnull%2C%5B1280%2C585%5D%2C%5B%5D%2C%5Bnull%2C34%5D%2Cnull%2C%5B34%5D%2C%5Bnull%2C%5C%22{urllib.parse.quote(self.DETECTED_OBJECT, safe="")}%5C%22%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2Cnull%2C%5B%5B%5C%22region_search%5C%22%2Cnull%2C%5B%5B0.5%2C0.5%2C1%2C1%2Cnull%2C1%5D%2Cnull%2Cnull%2C1%5D%5D%5D%2C%5C%22{urllib.parse.quote(self.UI, safe="")}%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C%5B%5D%5D%5D%2Cnull%2C%5C%22%5C%22%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&'
            )

            SESSION.headers.update(
                {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Dest': 'empty',
                    'Accept': '*/*',
                    'Sec-Fetch-Mode': 'cors',
                    'X-Same-Domain': '1',
                    'Content-Length': '{}'.format(len(str(data))),
                }
            )

            RESPONSE_3 = SESSION.post('https://lens.google.com/_/LensWebStandaloneUi/data/batchexecute?', params=params, data=data)
            self.URL_FINDER = re.findall(r'https?://[^\s"]+', str(RESPONSE_3.text))
            for URL in self.URL_FINDER:
                if 'encrypted' not in str(URL):
                    self.CLEANED_URL = re.sub(r'(https://[^\s]+)[^\w/]', r'\1', URL).replace('\\', '')
                    DUMPS.append(f'{self.CLEANED_URL.replace("amp;", "")}')
                else:
                    continue
            if len(DUMPS) != 0:
                return True
            else:
                printf(
                    Panel(f"[bold red]Sorry, we couldn't find any links or exact matches for this image, please try another image!", width=59, style="bold bright_black", title="[bold bright_black]> [ Empty Link ] <")
                )
                sys.exit()

if __name__ == "__main__":
    try:
        os.system('git pull')
        FEATURE().MAIN()
    except (Exception) as e:
        printf(
            Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title="[bold bright_black]> [ Error ] <")
        )
        sys.exit()
    except (KeyboardInterrupt):
        sys.exit()