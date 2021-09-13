import requests, os, discord,json
from discord.ext import commands
from bs4 import BeautifulSoup
from utils import fetch_urls
import urllib3
http = urllib3.PoolManager()
client = discord.Client()


GUILDID = '882562864529965106'
IDTOKEN = 'C=0; O=0; U=5ae4283f0f45ef3f6e09f5600a3f3e7c; V=3ca5990303deeef3666b4f46cb635de85ea06479013561.41534528; exp=A311B%7CA560B%7CA803B%7CA294C%7CA259B%7CA735A%7CC024A%7CA110B%7CA270C%7CA278C%7CA289D%7CA448A%7CA890H; expkey=D6DAD6D0A82DB546F665E19DA3C0C055; _sdsat_isAdobeOptOut=false; _sdsat_oneTrustTargetingCookie=true; _sdsat_oneTrustPerformanceCookie=true; OptanonConsent=isIABGlobal=false&datestamp=Mon+Sep+13+2021+23%3A58%3A04+GMT%2B0600+(Bangladesh+Standard+Time)&version=6.18.0&landingPath=NotLandingPage&groups=snc%3A1%2Cprf%3A1%2Cfnc%3A1%2Ctrg%3A1%2CSPD_BG%3A1&AwaitingReconsent=false&hosts=&consentId=ddeb2183-fb62-40a3-a393-8dc6456aaf59&interactionCount=0; _sdsat_oneTrustCookie=,0_179421,snc,0_189848,0_182337,prf,0_189849,fnc,0_182338,trg,0_182339,0_182867,0_182340,0_182341,0_182866,0_268915,0_268916,0_189806,0_189847,0_219331,0_244142,0_213057,0_219330,0_219332,0_213058,0_260705,0_213056,0_186627,101,102,; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18884%7CMCMID%7C48714222390775171701892080411221373876%7CMCAID%7CNONE%7CMCOPTOUT-1631563082s%7CNONE%7CMCAAMLH-1632160682%7C3%7CMCAAMB-1632160682%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18891%7CvVersion%7C4.6.0%7CMCCIDH%7C-1330176081; _sdsat_maxmindCountry=Bangladesh; _ga=GA1.2.2081775466.1587569793; _sctr=1|1626372000000; s_ecid=MCMID%7C48714222390775171701892080411221373876; s_pers=%20buFirstVisit%3Dcs%252Ccore%252Cstudy-pack%7C1783352115983%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Chome%2520page%7C1631557683698%3B; LPVID=Y1YjQwNTQ3MzNkN2VmNjUy; mbox=session#f72649fa3167480099312c0f52f300f1#1587596584|PC#f72649fa3167480099312c0f52f300f1.22_0#1650839525; __gads=ID=7ce4ff501789f563-225febd2e5c70076:T=1620406511:S=ALNI_MYAX1D64mF4UKTTVt1-ewXcLTmP9A; usprivacy=1YNY; OneTrustWPCCPAGoogleOptOut=false; optimizelyEndUserId=oeu1609416353067r0.7386819746130779; _omappvp=phMe6gIADXeYBzsvTHimIzfSbyaXtcMgAVP1Bt4nvS7BMDwO5MIIq14w3lPGwD87xwwG7jKpklc2fX2ijxLbACGNUQPl0jWY; _gcl_au=1.1.1274185358.1609416356; _fbp=fb.1.1609416358429.1320248595; _rdt_uuid=1609416355497.a56d7ade-2495-43b1-aeae-d12d7084f139; sbm_mcid=48714222390775171701892080411221373876; _pxvid=30df1e5c-93bd-11eb-b857-0242ac120015; sbm_sbm_id=0100007FE7C5A05E3400266E024FDA33; sbm_dma=0; wcs_bt=s_4544d378d9e5:1631555888; _cs_c=1; __CT_Data=gpv=30&ckp=tld&dm=chegg.com&apv_79_www33=30&cpv_79_www33=30; _cs_id=2d8d8a9a-0da4-a479-8b9e-a039de00e84b.1624884167.31.1631555891.1631555695.1.1659048167682; _scid=713d56ba-f007-449b-b40d-dcb9ef0f1bc2; _ym_uid=16255855961060867728; _ym_d=1625585596; forterToken=e34bf51818754a10975b4cbad7615807_1631555613031__UDF43_13ck; __ssid=b82b6734b7fd47c208a55685356b025; chegg_web_cbr_id=a; PHPSESSID=lnls7edtsu6l0h6262m3gv7vcc; CSessionID=22fe5acb-a117-459a-a733-b277e58c885c; user_geo_location=%7B%22country_iso_code%22%3A%22BD%22%2C%22country_name%22%3A%22Bangladesh%22%2C%22region%22%3A%22C%22%2C%22region_full%22%3A%22Dhaka+Division%22%2C%22city_name%22%3A%22Ghorasal%22%2C%22postal_code%22%3A%221613%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%5D%7D%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; s_sess=%20buVisited%3Dcore%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Chome%25252520page%252526pidt%25253D1%252526oid%25253DfunctionFr%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DBUTTON%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D384FF670B846FF0B-36780C32FEFE3C32%3B%20s_ptc%3D0.01%255E%255E0.10%255E%255E0.10%255E%255E0.18%255E%255E0.91%255E%255E0.00%255E%255E5.53%255E%255E0.11%255E%255E6.99%3B; mcid=48714222390775171701892080411221373876; _sdsat_authState=Hard%20Logged%20In; CVID=48714222390775171701892080411221373876; CSID=1631555595940; sbm_a_b_test=1-control; schoolapi=null; _tq_id.TV-8145726354-1.ad8a=4f7b5c3fd98ec66c.1631555628.0.1631555890..; _px3=097b7687e9c61effdad524339937f0b3d9a796e3e40e60cffea10634e546dce5:3Z0mhji6oqE44bk/dtVsnPTcUJhQmoSCVJgGWBTHgJcacptmt13VueU0NVtYLxwvS5aLO+g4v0bvR3OJDXLjjQ==:1000:B3vr//OkLYVag6S+IoJnDy+l+29L4Jc3Su6Ni5+7OuAk/ZA2tNx5HHWw6dYcQdBQprdxDvu9aCM93Eecl+QV9uFt5gZUmTZFPCL2/JBE8kEamYoELL6Ub+GpTimZ4RARfeNYRsh/u2XfLQJO0UUV6qigMxprNZaqh8Ah7NbNhphSQM1HCyjySqcRJhWOLI2SA4xUdLdPVgmVKx0Ej1R+eQ==; _px=3Z0mhji6oqE44bk/dtVsnPTcUJhQmoSCVJgGWBTHgJcacptmt13VueU0NVtYLxwvS5aLO+g4v0bvR3OJDXLjjQ==:1000:BMlw6+nt1TfQAf9v4nBoLLGN9XKdb0sngjFYhmJwGCr/EvPvvfXK67ox6mMnzfJYswPPbIPpIcud8WqVXbQaBhog2GASXPsw2PYZb3yVxDZ38LyhWh7eazc//2KYfCGTEjSxW9ZfprGao4J2SkTkSXmkQ/RyK0dFqtC7+ITpKZkHTXmJGSXX6IS/3tEi4LGd4T+WFZNS77kfukO8YScDrhYEuU5dbxDWesEQ/d3XO+pLBOIoE2nYHkmuIFgkU8SXKH+a63yrKMwmEP52NrsiVA==; _gid=GA1.2.445569328.1631555631; _iidt=yv9xLP9bDW7/fuEU+yVeVST/EhzPYKVPFEzhvCaaseAG7d0r9RRZY7G++DMb9XKlSI/Rq6dkGrmOdg==; _vid_t=aCSgfKn5KRXjVbUd/rR/fUyYFIVQGv6bBOuFb7F/vBNrSYvTmISXAxDP+CW7+pxZUCaLCNQeL2g0Jw==; DFID=web|qSBld3S1Lorr5iHUSWr4; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%20517c1256-b143-42d1-b4ad-945a7a1661d9%2C%20%22created_date%22%20%3D%3E%202021-09-13T17%3A54%3A09.480Z%20%5D; id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFuamVsLmhhaWRhci5mYWhpbUBnLmJyYWN1LmFjLmJkIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsInN1YiI6IjUxN2MxMjU2LWIxNDMtNDJkMS1iNGFkLTk0NWE3YTE2NjFkOSIsImF1ZCI6IkNIR0ciLCJpYXQiOjE2MzE1NTU2NzcsImV4cCI6MTYzOTAxNDcxOSwicmVwYWNrZXJfaWQiOiJhcHcifQ.fO0DeDdrGtVxNyMvwXtTWruhxkc9Jiu4RxLwZ-MMjL9guq9OL5lsM7VA8Vle4jlB0jhjuyH9FbT77u1VVDvAjpSdz49B16OnQ2635wa9uCTmEETlUnmAKkOxVpne8Xg8XhBjnFvruHFlOt7NmaK-BntQ6-I-SvEXu0nda3WNwQ6jataXw1CSNbPmmrp9ynZJsPe4WmGssK-Nm2DV7__8pZqUAHWgMHJkY1M9uhsPYLCuAThQ4DojExbZseRIinU0-ZViv88DXmAfdgocZMdav0rSVkGPztcQ4GV8UnEHvbnL3F_NhpjzR5YDFNU5Oe0QxvBMMvKBH1g0jjKaKY4qxA; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh1Yi5jaGVnZy5jb20iLCJzdWIiOiI1MTdjMTI1Ni1iMTQzLTQyZDEtYjRhZC05NDVhN2ExNjYxZDkiLCJhdWQiOlsiY2hlZ2ctb2lkYyIsImh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMxNTU1Njc3LCJleHAiOjE2MzE1NTcxMTcsImF6cCI6IjNUWmJoZnNad2RlSGJob1ZNeE92WkdiMzdNY3ZjMG84Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBhZGRyZXNzIHBob25lIG9mZmxpbmVfYWNjZXNzIiwiZ3R5IjoicGFzc3dvcmQiLCJyZXBhY2tlcl9pZCI6ImFwdyIsImNoZ2hyZCI6dHJ1ZSwiY2hnbWZhIjp0cnVlfQ.H9mFifSex8NYXHLdv_d_MQlQXe07bT-zV2H99lUtFLwZI6Tau5SB8YMiU9IxLl6Fx7a53AtQt-Qmc_wxzYHJkSV9bGwkh0XwON5bjh0hNMGzAPvkgcwe4-bjbbh0VL6D9Y_f_Q-7Z0Ah4USLcaPYTB2R-EVJm6DG239W_x_dR-ogi_LUv2AKIPxAUQd4yFMnUfGpItwZ6QYtSTjClDaoAFROxXrBGUhpwXa0dOyn9ZuG5aSqm43zij5Q26m4q2d0HGBwAR_wQ9XsOMCLzwn85Sh_7M8bNKWI8no0az0QPkIRzTzW-2wjoZFgPmgnosFJcYzUlYrnUaxgfGNRUTFfjg; access_token_expires_at=1631557117; refresh_token=ext.a0.t00.v1.MSXyEeMXrOHYON7Yt0LVMLRlETQmJV_qiyfk_V4eLPg6R4Nb3ixGZI0ipPnpCgUuByjNCnBCo7xIw5JH6pkuNfM; SU=A8085Z2QXfyWZmUIk1-_hPZqB889OaMua0ysZbUhyXcY0880ETobOzPaxQ0jQW7nzAeKEkYqIW6yPjbyOqOvrt6aWwnhEZ5PebD8fM5KFhsrkpGq8rzB5OjM8Dd9D3Lq; _sdsat_cheggUserUUID=517c1256-b143-42d1-b4ad-945a7a1661d9; ab.storage.userId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%22517c1256-b143-42d1-b4ad-945a7a1661d9%22%2C%22c%22%3A1631555686848%2C%22l%22%3A1631555686854%7D; ab.storage.sessionId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%226eab2d89-23b6-9cfd-7de0-1660db175bcb%22%2C%22e%22%3A1631557689080%2C%22c%22%3A1631555686851%2C%22l%22%3A1631555889080%7D; ab.storage.deviceId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%228bf293e8-da75-2d6c-49d1-55984bb259fe%22%2C%22c%22%3A1631555686857%2C%22l%22%3A1631555686857%7D; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22home%20page%22%5D%7D; _cs_s=2.1.0.1631557691686; _uetsid=8a872a0014bb11ecbb199f72f644a96b; _uetvid=55ce2580d80e11eb835983cd4aa1ac12; _ym_isad=2'
USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'




@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILDID:
            break
    
    print(
        f'{client.user} is connected to the following guild :\n'
        f'{guild.name}(id: {guild.id})'
    )



@client.event
async  def on_message(message):
	urls = fetch_urls(message.content)
	for url in urls:
		if "https://www.chegg.com/homework-help/"  in url:
			await message.reply( f'{message.author.mention} \n  Fetching Your Answer  ')
			page =http.request('GET', url,

			headers={'User-Agent':USERAGENT ,
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Referer': url,
    'Connection': 'keep-alive',
    'Cookie': IDTOKEN,
    'Upgrade-Insecure-Requests': '1',
    'If-None-Match': '"26fd3-EKpH9vUiB7dNGZfVLRVy9BM+Gog"',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'})
			pageContent = str(page.data.decode("utf-8"))
			soup = BeautifulSoup(pageContent.replace('"//', '"https://'),"html.parser")
			file = open("ans.html", "w", encoding="utf-8")
			file.write(pageContent)
			file.close()
			url = "https://siasky.net/skynet/skyfile"
			payload={}

			files = [
				('file', ("Ans.html", open('./ans.html', 'rb'), 'text/html'))
			]
			headers7 = {
				'referrer': 'https://siasky.net/'
			}
			response = requests.request("POST", url, headers=headers7, data=payload, files=files)
			embed = discord.Embed(title= "Click This", description= "Click the link to open", color= discord.Colour.green())
			embed.url = "https://siasky.net/" + response.json()["skylink"]
			embed.set_footer(text = "Bot Coded by FlowerInPot | Homework Help")
			my_files = [discord.File('ans.html')]
			await message.reply(embed=embed)
			#print(response.text)
			#linkup = "https://siasky.net/" + response.json()["skylink"]
			#my_files = [discord.File('ans.html')]
			#await message.reply( f'{message.author.mention} \n ans : '+ linkup)


client.run("ODg3MDY3NzYzMTU4NDUwMjE2.YT-wOw.laB3CrL-kUGVc04d6u2Qc5kBJt0")
