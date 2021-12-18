import webbrowser, requests, bs4, os, time

#url='https://manga4life.com/read-online/The-Irregular-of-the-Royal-Academy-of-Magic-chapter-1-page-1.html'
#url='https://xkcd.com/'
#url='https://mangakakalot.com/chapter/tsuki_ga_michibiku_isekai_douchuu/chapter_59'
#url='https://manga4life.com/read-online/Ore-No-Ie-Ga-Maryoku-Spot-Datta-Ken-chapter-1-page-1.html'
#url='https://mangadex.org/chapter/01d4ec62-647c-486b-a458-b13cf44d56ef'

url='https://www.mngdoom.com/ore-no-ie-ga-maryoku-spot-datta-ken-sundeiru-dake-de-sekai-saikyou/1/1'
#url='https://www.facebook.com/'
os.makedirs('Manga',exist_ok=True)
j=1
z=1
Fname=str(z)+'.jpg'
while not url.endswith('#'):
    print('Donwloading Page : '+url)
    res=requests.get(url)
    res.raise_for_status()
    #HTML PRINTING IN TEXT
    f1=open('HTML.txt','wb')
    for i in res.iter_content(1000000):
        f1.write(i)
    ######################

    soup=bs4.BeautifulSoup(res.content,'html.parser')
    comicElem=soup.select('img')
    print(comicElem)
    if comicElem==[]:
       print('No Image Found')
    else:

        comicChapter=soup.select('select.chapter-page2 option')
        Count=len(comicChapter)
        print(Count)
        for i in range(Count):
            comicUrl=comicElem[0].get('src')
            Url=list(comicUrl)
            Url[-5]=str(i)
            comicUrl=''.join(Url)
            print(comicUrl)
            res=requests.get(comicUrl)
            res.raise_for_status()
            print('Downloading Image.....')
            #imgfile=open(os.path.join('Manga',os.path.basename(comicUrl)),'wb')
            imgfile=open(os.path.join('Manga',Fname),'wb')
            z=z+1
            Fname=str(z)+'.jpg'
            for chunk in res.iter_content(1000000):
                imgfile.write(chunk)
            print('DOWNLOADED')
    j=j+1
    Murl=list(url)
    Murl[-3]=str(j)
    url=''.join(Murl)
            
        
print('Done')