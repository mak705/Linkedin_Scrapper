#Due to securuty issue I am not showing asy user info just show how to do 

elems = driver.find_elements_by_xpath("//div[@class='mn-connection-card__details']//a[@data-control-name='connection_profile'][@href]")
list_email =[]
for elem in elems:
    list_email.append(elem.get_attribute("href"))
#Take the first element from the list and do the below operations

url = 'https://www.linkedin.com/in/xxxxx/'
name_soup = driver.find_element_by_xpath("//h1[@class='pv-top-card-section__name inline t-24 t-black t-normal']").get_attribute("innerHTML")
name = BeautifulSoup(title_find,'lxml')
print (name.text)
>> 
designation_find = driver.find_element_by_xpath("//h2[@class='pv-top-card-section__headline mt1 t-18 t-black t-normal']").get_attribute("innerHTML")
print ('Desination:',designation_find.format().split('at')[0])
print ('Company:', designation_find.format().split('at')[1])
>>    Desination: XXXXX 
      Company:  XXXXXX
designation = BeautifulSoup(designation_find,'lxml')
print (designation.text)
>>Sr XXXX at XXX Technology

contact_info_URL = url + 'detail/contact-info/'
contact_info_URL
>>https://www.linkedin.com/in/xxxxx/detail/contact-info/'
driver.get(contact_info_URL)
linkedin_URL =  driver.find_element_by_xpath("//a[@class='pv-contact-info__contact-link t-14 t-black t-normal']").get_attribute("innerHTML")
print (linkedin_URL.format())
>>linkedin.com/in/xxxxxx
phone =  driver.find_element_by_xpath("//span[@class='t-14 t-black t-normal']").get_attribute("innerHTML")
print (phone.format())
>> xxxxxxxxxxxx
contact_info_single = driver.find_element_by_xpath("//artdeco-modal/artdeco-modal-content/section/div").get_attribute("innerHTML")
contact_soup = BeautifulSoup(contact_info_single, 'html.parser')
xpath = contact_soup.findAll('a')
contact_url = [ link.get('href', None) for link in xpath]
phone = contact_soup.find('span',{'class':'t-14 t-black t-normal'})
contact_url.append(phone.text)
#print([s.lstrip('mailto') for s in links])
contact_info_all = ([s.replace('mailto:', '') for s in contact_url]) 
print (contact_info_all)
>>['https://www.linkedin.com/in/xxxxx', 'xxxx@gmail.com', 'https://twitter.com/xx', 'xxxxx']
phone = contact_soup.find('span',{'class':'t-14 t-black t-normal'})
phone.text
>> 'xxxx'
contact_inf  = {}
contact_inf['user_info'] = contact_info_all
contact_inf
{'user_info': ['https://www.linkedin.com/in/xxx',
  'xx@gmail.com',
  'https://twitter.com/xxx',
  'xxx']}



