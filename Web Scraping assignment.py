#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


#importing the required libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd


# # Q1 all the header tags from ‘en.wikipedia.org/wiki/Main_Page’

# In[14]:


q1 = requests.get('https://en.wikipedia.org/wiki/Main_Page')
q1


# In[15]:


q1.content


# In[21]:


soup = BeautifulSoup(q1.content)
soup


# In[23]:


print(soup.prettify())


# In[59]:


page1 = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page1


# In[60]:


page1.content


# In[61]:


soup1 = BeautifulSoup(page1.content)
soup1


# In[62]:


print(soup1.prettify())


# In[98]:


h1 = []
headings = soup.find_all('h1',id="firstHeading")
for i in headings:
    h1.append(i.text)
h1


# In[80]:


h2 = []
headings = soup.find_all('h2', class_="mp-h2" )


for i in headings:
    h2.append(i.text.replace('\n',''))
h2


# In[94]:


h3 = []
headings = soup.find_all('h3', class_="vector-menu-heading" )

for i in headings:
    h3.append(i.text.strip())
h3


# In[93]:


wiki_headings = h1+h2+h3


# In[95]:


print(wiki_headings)


# In[104]:


import pandas as pd


# In[107]:


heading = pd.DataFrame({})
heading['Header tags on wikipedia'] = wiki_headings
heading


# # Q2 IMDB’s Top rated 100 movies’ data

# In[108]:


page2 = requests.get('https://www.imdb.com/list/ls091520106/')
page2


# In[112]:


page2.content


# In[118]:


soup = BeautifulSoup(page2.content)
soup


# In[119]:


print(soup.prettify())


# In[176]:


name = soup.find_all('h3',class_="lister-item-header")
name


# In[179]:


Movie = []
for i in name:
    Movie.append(i.text)
Movie


# In[183]:


movie_name = []

for i in name:
    for j in i.find_all('a'):
        movie_name.append(j.text)
movie_name


# In[131]:


year = soup.find_all('span',class_="lister-item-year text-muted unbold")
year


# In[ ]:





# In[162]:


release_year = []
for i in year:
    release_year.append(i.text.replace('(',' ').replace(')','').replace('I','').strip())
release_year


# In[245]:


rating = soup.find_all('span',class_="ipl-rating-star__rating")
rating


# In[246]:


IMBD = []

for i in rating:
    IMBD.append(i.text)
IMBD


# In[249]:


IMBD_rating = []

for i in range(0,len(IMBD),23):
    IMBD_rating.append(IMBD[i])
IMBD_rating


# In[254]:


import pandas as pd
IMBDtop100 = pd.DataFrame({})
IMBDtop100['NAME'] = movie_name
IMBDtop100['IMBD rating'] = IMBD_rating
IMBDtop100['Year of release'] = release_year


# In[253]:


IMBDtop100


# # Q3 IMDB’s Top rated 100 Indian movies’ data

# In[255]:


page3 = requests.get('https://www.imdb.com/list/ls009997493/')
page3


# In[256]:


page3.content


# In[257]:


soup = BeautifulSoup(page3.content)
soup


# In[259]:


print(soup.prettify())


# In[260]:


name = soup.find_all('h3',class_="lister-item-header")
name


# In[265]:


movie_ = []

for i in name:
    for j in i.find_all('a'):
        movie_.append(j.text)
movie_


# In[266]:


Year = soup.find_all('span',class_="lister-item-year text-muted unbold")
Year


# In[272]:


Release_Year = []

for i in Year:
    Release_Year.append(i.text.replace('(','').replace(')','').replace('I ',''))
Release_Year


# In[273]:


Rating = soup.find_all('span',class_="ipl-rating-star__rating")
Rating


# In[276]:


IMBDrating = []

for i in Rating:
    IMBDrating.append(i.text)
IMBDrating


# In[277]:


IMBD_ratings = []

for i in range(0,len(IMBDrating),23):
    IMBD_ratings.append(IMBDrating[i])
IMBD_ratings


# In[278]:


print(len(movie_),len(IMBD_ratings),len(Release_Year))


# In[280]:


import pandas as pd

TopIndianMovies = pd.DataFrame({})
TopIndianMovies['MOVIE NAME'] = movie_
TopIndianMovies['RELEASE YEAR'] = Release_Year
TopIndianMovies['IMBD RATING'] = IMBD_ratings
 


# In[281]:


TopIndianMovies


# # Q4 Information about any 5 books from www.bookpage.com

# In[11]:


page4 = requests.get('https://bookpage.com/reviews')
page4


# In[12]:


page4.content


# In[13]:


soup = BeautifulSoup(page4.content)
soup


# In[14]:


print(soup.prettify())


# In[15]:


name = soup.find_all('h4',class_="italic")
name


# In[16]:


book_name = []

for i in name:
    for j in i.find_all('a', href = True):
        book_name.append(j['href'])
book_name


# In[17]:


books = []
for i in book_name:
    book = requests.get('https://bookpage.com/'+i)
    soup = BeautifulSoup(book.content,'html.parser')
    books.append(soup.find('h1').text.replace('\n',''))
    
books


# In[18]:


books_name = books[0:5]
books_name


# In[31]:


author_name = []
author = soup.find_all('p',class_="sans bold")
author

for i in author:
    author_name.append(i.text)
author_name


# In[ ]:





# In[32]:


genre = []

genre1 = soup.find_all('p',class_="genre-links hidden-phone")
genre1

for i in genre1:
    genre.append(i.text)
genre


# In[33]:


review = []

rev = soup.find_all('div',class_="article-body")

for i in rev:
    review.append(i.text)
review


# In[ ]:





# In[ ]:





# # Q5. cricket rankings from ‘www.icc-cricket.com’
# #(i) Top 10 ODI teams in men’s cricket

# In[10]:


page5 = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page5


# In[5]:


page5.content


# In[6]:


soup = BeautifulSoup(page5.content)
soup


# In[7]:


print(soup.prettify())


# In[8]:


team = soup.find_all('span',class_="u-hide-phablet")
team


# In[9]:


team_country = []

for i in team:
    team_country.append(i.text)
name = team_country[0:10]
name


# In[127]:


info = []
info1 = soup.find_all('td',class_="rankings-block__banner--matches")
info1

for i in info1:
    info.append(i.text)
info


# In[128]:


info_2 = []
info2 = soup.find_all('td',class_="table-body__cell u-center-text")
info2

for i in info2:
    info_2.append(i.text)
info_2


# In[132]:




for i in range(0,len(info_2),2):
    info.append(info_2[i])
info


# In[134]:


no_of_matches = info[0:10]
no_of_matches


# In[137]:


point = []
point1  = soup.find_all('td', class_="rankings-block__banner--points")
point1 

for i in point1:
    point.append(i.text)
point
    


# In[138]:


for i in range(1,len(info_2),2):
    point.append(info_2[i])
point


# In[140]:


points = point[0:10]
points


# In[142]:


rating = []

rating1 = soup.find_all('td',class_="rankings-block__banner--rating u-text-right")

for i in rating1:
    rating.append(i.text.strip())
rating


# In[143]:


rating2 = soup.find_all('td', class_="table-body__cell u-text-right rating")

for i in rating2:
    rating.append(i.text.strip())
rating


# In[145]:


ratings = rating[0:10]
ratings


# In[152]:


MEN_ODI = pd.DataFrame({})
MEN_ODI['TEAM NAME '] = name
MEN_ODI['MATCHES'] = no_of_matches
MEN_ODI['POINTS'] = points
MEN_ODI['RATINGS'] = ratings
MEN_ODI


# # ii) Top 10 ODI Batsmen in men along with the records of their team and rating

# In[189]:


page52 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page52


# In[190]:


page52.content


# In[191]:


soup = BeautifulSoup(page52.content)
soup


# In[192]:


print(soup.prettify())


# In[193]:


Name = []

name = soup.find_all('div',class_="rankings-block__banner--name")
                

for i in name:
    Name.append(i.text)
Name


# In[194]:


Names = []
Names.append(Name[0])
Names    
    


# In[195]:


Names2 = []
n = soup.find_all('td',class_="table-body__cell name")
for i in n:
    Names.append(i.text.strip())
Names


# In[196]:


TopBatsman = Names[0:10]
TopBatsman


# In[217]:


Team_name = []
Team = soup.find_all('span',class_="table-body__logo-text")

for i in Team:
    Team_name.append(i.text.replace('\n',''))
Team_name
team = Team_name[0:9]
team


# In[267]:


t = []

team1 = soup.find_all('div',class_="rankings-block__banner--nationality")
for i in team1:
    t.append(i.text.replace('\n','').replace('873','').strip().replace('737','').strip())
    
TEAM = [t[0]]
TEAM


# In[238]:


TEAM_NAME = TEAM + team
print(TEAM_NAME)


# In[240]:


TeamName = TEAM_NAME[0:10]
TeamName


# In[243]:


ra = []
R1 = soup.find_all('div',class_="rankings-block__banner--rating")
R1
for i in R1:
    ra.append(i.text)
ra


# In[247]:


r1 = [ra[0]]
r1


# In[248]:


R2 = soup.find_all('td',class_="table-body__cell u-text-right rating")
R2
for i in R2:
    r1.append(i.text)
r1


# In[249]:


ratings = r1[0:10]
ratings


# In[250]:


ODIBatsman = pd.DataFrame({})
ODIBatsman['NAME'] = TopBatsman
ODIBatsman['TEAM NAME'] = TeamName
ODIBatsman['RATINGS'] = ratings
ODIBatsman


# # iii) Top 10 ODI bowlers along with the records of their team and rating.
# 

# In[252]:


TopBowlers = []
Topbowlers = soup.find_all('div',class_="rankings-block__banner--name")

for i in Topbowlers:
    TopBowlers.append(i.text)
TopBowlers


# In[254]:


TopBowlers1 = [TopBowlers[1]]
TopBowlers1


# In[ ]:


class="table-body__cell name"


# In[258]:


TopBowlers2 = Names[10:19]
TopBowlers2


# In[259]:


Top10B = TopBowlers1 + TopBowlers2
Top10B


# In[272]:


T1 = [t[1]]
T1


# In[273]:


T2 = TEAM_NAME[10:19]
T2


# In[275]:


BowlersTeam = T1+T2
BowlersTeam


# In[279]:


Bowlersra1 = [ra[1]]
Bowlersra1


# In[280]:


Bowlersra2 = r1[10:19]
Bowlersra2


# In[281]:


BowlersRating = Bowlersra1 + Bowlersra2
BowlersRating


# In[283]:


Top10 = pd.DataFrame({})
Top10['NAME OF TOP BOWLERS'] = Top10B
Top10['TEAM NAME'] = BowlersTeam
Top10['RATINGS'] = BowlersRating
Top10


# # Q6.  cricket rankings from ‘www.icc-cricket.com’
# i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[284]:


page6 = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page6


# In[285]:


page6.content


# In[286]:


soup = BeautifulSoup(page6.content)
soup


# In[287]:


print(soup.prettify())


# In[289]:


WomenTeam = []
wt1 = soup.find_all('span',class_="u-hide-phablet")
wt1

for i in wt1:
    WomenTeam.append(i.text)
WomenTeam


# In[298]:


WomenTeam1 = WomenTeam[0:10]
WomenTeam1


# In[315]:


WMatches = []

WM = soup.find_all('td',class_="rankings-block__banner--matches")
WM

for i in WM:
    WMatches.append(i.text)
WMatches


# In[316]:


WM_1 = []
WM1 = soup.find_all('td',class_="table-body__cell u-center-text")
WM1

for i in WM1:
    WM_1.append(i.text)
WM_1


# In[317]:


WM_2 = []
for i in range(0,len(WM_1),2):
    WM_2.append(WM_1[i])
WM_2
    


# In[318]:


WMatches


# In[319]:


WomenMatches = WMatches + WM_2
print(WomenMatches)


# In[320]:


WPoints = []

WP = soup.find_all('td',class_="rankings-block__banner--points")
WP

for i in WP:
    WPoints.append(i.text)
WPoints


# In[321]:


WP_1 = []
WP1 = soup.find_all('td',class_="table-body__cell u-center-text")
WP1

for i in WP1:
    WP_1.append(i.text)
WP_1


# In[324]:


WP_2 = []
for i in range(1,len(WP_1),2):
    WP_2.append(WM_1[i])
WP_2


# In[325]:


WomenPoints = WPoints + WP_2
print(WomenPoints)


# In[327]:


WRatings = []

WR = soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
WR

for i in WR:
    WRatings.append(i.text.strip())
WRatings


# In[329]:


WR_1 = []
WR1 = soup.find_all('td',class_="table-body__cell u-text-right rating")
WR1

for i in WR1:
    WR_1.append(i.text)
WR_1


# In[331]:


WomenRatings = WRatings + WR_1
print(WomenRatings)


# In[333]:


WOMEN__TEAM = pd.DataFrame({})
WOMEN__TEAM['TEAM NAME'] = WomenTeam1
WOMEN__TEAM['MATCHES'] = WomenMatches
WOMEN__TEAM['POINTS'] = WomenPoints
WOMEN__TEAM['RATINGS'] = WomenRatings
WOMEN__TEAM  


# # ii) Top 10 women’s ODI players along with the records of their team and rating

# In[335]:


page62 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
page62


# In[336]:


page62.content


# In[337]:


soup = BeautifulSoup(page62.content)
soup


# In[338]:


print(soup.prettify())


# In[360]:


WName = []
wn1 = soup.find_all('div',class_="rankings-block__banner--name")
wn1

for i in wn1:
    WName.append(i.text)
WName
WN1 = [WName[0]]
WN1


# In[361]:


WN_1 = []
WN__1 = soup.find_all('td',class_="table-body__cell name")
WN__1

for i in WN__1:
    WN_1.append(i.text.replace('\n',''))
WN_1


# In[362]:


WN2 = WN_1[0:9]
WN2


# In[363]:


Womenname= WN1 + WN2
Womenname


# In[367]:


WTeam_name = []
WTeam = soup.find_all('span',class_="table-body__logo-text")

for i in WTeam:
    WTeam_name.append(i.text.replace('\n',''))
WTeam_name

Wteam = WTeam_name[0:9]
Wteam


# In[389]:


wt = []

wteam1 = soup.find_all('div',class_="rankings-block__banner--nationality")
for i in wteam1:
    wt.append(i.text.replace('\n','').replace('762','').strip().replace('418','').strip())
    
wTEAM = [wt[0]]
wTEAM


# In[372]:


WomenTeam = wTEAM + Wteam 
WomenTeam


# In[374]:


wra = []
wR1 = soup.find_all('td',class_="table-body__cell u-text-right rating")
wR1
for i in wR1:
    wra.append(i.text)
wra
WRA1 = wra[0:9]
WRA1


# In[376]:


WR2 = []
wr2 = soup.find_all('div',class_="rankings-block__banner--rating")
wr2

for i in wr2:
    WR2.append(i.text)
WR2


# In[377]:


WRA3 = [WR2[0]]
WRA3


# In[378]:


WomenRating = WRA3 + WRA1
WomenRating


# In[380]:


TopWomen = pd.DataFrame({})
TopWomen['Name'] = Womenname
TopWomen['Team'] = WomenTeam
TopWomen['Rating'] = WomenRating
TopWomen


# # iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[386]:


AR1 = [WName[2]]
AR1


# In[387]:


AR2 = WN_1[18:29]
AR2


# In[388]:


ARname = AR1 + AR2
ARname


# In[390]:


ARTEAM = [wt[2]]
ARTEAM


# In[391]:


ARteam = WTeam_name[18:29]
ARteam


# In[392]:


arteam = ARTEAM + ARteam
arteam


# In[393]:


ARRA3 = [WR2[2]]
ARRA3


# In[394]:


ARRA1 = wra[18:29]
ARRA1


# In[395]:


arra = ARRA3 + ARRA1
arra


# In[397]:


ALLROUNDERWomen = pd.DataFrame({})
ALLROUNDERWomen['Name'] = ARname
ALLROUNDERWomen['Team'] = arteam
ALLROUNDERWomen['Rating'] = arra
ALLROUNDERWomen


# # Q7. ALL THE MOBILE PHONES UNDER RS.20,000 LISTED ON AMAZON.IN

# In[407]:


page7 = requests.get('https://www.amazon.in/best-mobile-under-20000/s?k=best+mobile+under+20000')
page7


# In[408]:


page7.content


# In[409]:


soup = BeautifulSoup(page7.content)
soup


# In[410]:


print(soup.prettify())


# In[468]:


model_name = []
model = soup.find_all('span', class_="a-size-medium a-color-base a-text-normal")

for i in model:
    model_name.append(i.text)
MODEL = model_name[0:15]
MODEL


# In[469]:


price = []

p = soup.find_all('span',class_="a-price-whole")

for i in p:
    price.append(i.text)
prices = price[0:15]
prices


# In[470]:


print(len(model_name),len(price))


# In[471]:


image = []

img = soup.find_all('img',class_="s-image")
                    
for i in img:
    image.append(i.get('src'))

images  = image[0:15]
images


# In[472]:


len(images)


# In[473]:


rating = []
r = soup.find_all('span',class_="a-declarative")

for i in r:
    rating.append(i.text.replace('\n','').strip())
ratings = rating[1:16]
ratings


# In[474]:


len(ratings)


# In[476]:


phone = pd.DataFrame({})
phone['MODEL NAME'] = MODEL
phone['PRICE'] = prices
phone['IMAGE URL'] = images
phone['RATING'] = ratings
phone


# # Q8. 7 DAY EXTENDED FORCAST DISPLAY FOR THE CITY

# In[483]:


page8 = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.77493000000004&lon=-122.41941999999995#.YQGSW-gzbIU')
page8


# In[484]:


page8.content


# In[485]:


soup8 = BeautifulSoup(page8.content)
soup8


# In[486]:


print(soup8.prettify())


# In[487]:


temp = soup8.find_all('div',class_="tombstone-container")
temp


# In[498]:


period = []

p = soup8.find_all('p',class_="period-name")
for i in p:
    period.append(i.text)
period


# In[499]:


short_desc = []
sd = soup8.find_all('p',class_="short-desc")
for i in sd:
    short_desc.append(i.text)
short_desc


# In[495]:


temphigh = []

t = soup8.find_all('p',class_="temp temp-high")
for i in t:
    temphigh.append(i.text)
temphigh


# In[496]:


templow = []

t = soup8.find_all('p',class_="temp temp-low")
for i in t:
    templow.append(i.text)
templow


# In[505]:


temperature = [temphigh[0],templow[0],temphigh[1],templow[1],temphigh[2],templow[2],temphigh[3],templow[3],temphigh[4]]
temperature


# In[500]:


description = []
sd = soup8.find_all('div',class_="col-sm-10 forecast-text")
for i in sd:
    description.append(i.text)
description


# In[502]:


desc = description[0:9]
desc


# In[507]:


weather = pd.DataFrame({})
weather['PERIOD'] = period
weather['SHORT DESCRIPTION'] = short_desc
weather['TEMPERATURE']= temperature
weather['DESCRIPTION'] = desc
weather


# # Q9. job listings from ‘https://internshala.com/’

# In[508]:


page = requests.get('https://internshala.com/fresher-jobs')
page


# In[509]:


page.content


# In[510]:


soup = BeautifulSoup(page.content)
soup


# In[511]:


print(soup.prettify())


# In[513]:


titles = soup.find_all('div',class_="heading_4_5 profile")
titles


# In[514]:


job_titles = []
for i in titles:
    job_titles.append(i.text.replace('\n',''))
job_titles


# In[515]:


companies = soup.find_all('div',class_="heading_6 company_name")
companies


# In[516]:


company_name = []
for i in companies:
    company_name.append(i.text.strip())
company_name


# In[517]:


CTC = soup.find_all('div',class_="item_body")
CTC


# In[518]:


CTC_LIST = []
for i in CTC:
    CTC_LIST.append(i.text.replace('\n',''))
CTC_LIST


# In[519]:


CTC_ = []
for i in range(1,len(CTC_LIST),3):
    CTC_.append(CTC_LIST[i])
CTC_


# In[520]:


apply_date = []
for i in range(2,len(CTC_LIST),3):
    apply_date.append(CTC_LIST[i])
apply_date


# In[523]:


print(len(job_titles),len(company_name),len(CTC_),len(apply_date))


# In[522]:


import pandas as pd
jobs = pd.DataFrame({})
jobs['TITLE'] = job_titles
jobs['COMPANY'] = company_name
jobs['CTC'] = CTC_
jobs['APPLY DATE'] =apply_date
jobs


# # Q10. house details from https://www.nobroker.in/

# In[524]:


page = requests.get('https://www.nobroker.in/property/sale/delhi/East%20Patel%20Nagar?searchParam=W3sibGF0IjoyOC42NDY4MTUxLCJsb24iOjc3LjE3MjExOTksInBsYWNlSWQiOiJDaElKVlpzejU1UUNEVGtSWFBtaW4ydUxXNkUiLCJwbGFjZU5hbWUiOiJFYXN0IFBhdGVsIE5hZ2FyIn1d&radius=2.0&type=BHK3&propertyAge=0')
page


# In[525]:


page.content


# In[528]:


soup = BeautifulSoup(page.content)
soup


# In[529]:


print(soup.prettify())


# In[547]:


house_title = []

ht = soup.find_all('span',itemprop="name")

for i in ht:
    house_title.append(i.text)
house_titles =house_title[2:12]
house_titles


# In[548]:


loc = []

l = soup.find_all('div',class_="nb__35Ol7")
for i in l:
    loc.append(i.text)
loc


# In[536]:


area = []

a = soup.find_all('div',class_="nb__3oNyC")
for i in a:
    area.append(i.text)
area


# In[539]:


house_info = []

e = soup.find_all('div',class_="font-semi-bold heading-6")
for i in e:
    house_info.append(i.text)
house_info


# In[540]:


emi = []
for i in range(1,len(house_info),3):
    emi.append(house_info[i])
emi


# In[541]:


price = []
for i in range(2,len(house_info),3):
    price.append(house_info[i])
price


# In[552]:


HOUSE = pd.DataFrame({})
HOUSE['HOUSE TITLE'] = house_titles
HOUSE['LOCATION'] = loc
HOUSE['AREA'] = area
HOUSE['EMI'] = emi
HOUSE['PRICE'] = price
HOUSE


# In[ ]:




