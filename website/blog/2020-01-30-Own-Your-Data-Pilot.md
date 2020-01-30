---
title: Update #1 - Pilot project (Tally Zoo) with OwnYourData
author: Dixon Siu
authorURL: https://twitter.com/dixon_siu
---

During the winter vacation, [OwnYourData](https://www.ownyourdata.eu/)'s chief engineer had been working hard understanding Personium APIs and finally Tally Zoo [Documentation](http://bit.ly/TallyZoo_with_CEPS ) can access Personium user's data store (Box). We achieved the followings in current implementation:  

1. Personium user authentication from TallyZoo  
1. Retrieve Personium Cell access token to access the data store  
1. Store and remove JSON files  

Even though our goal (interoperability of personal data store) is still far away, [MyData](https://mydata.org) movement continues to drive collabrations among subject matter experts and passionate participants. Persererance will finally lead us to our goal.  

We will provide the following improvements for the next stage.  

1. Add a launcher from Personium's HomeApp  
1. Retrieve Personium Box access token to access the data store  
1. Create/Delete OData table  
1. Add/Delete OData table entry  

<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/ownyourdata.png" width="150px" >  
Original news here: https://personium.io/blog/2019/12/09/Own-Your-Data-Pilot/  

<!--truncate-->
## Demo  
1. Access http://tally.oydapp.eu/ and select Personium from the dropdown menu (Type:)  
Fill in the authentication information.  
<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/TallyZoo-Update01-img01.png" width="150px" >  
1. Default screen of TallyZoo when you authenticate successfully.  
<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/TallyZoo-Update01-img02.png" width="150px" >  
1. Personium user data store shows the corresponding JSON files.  
<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/TallyZoo-Update01-img03.png" width="150px" >  
1. Add a New Topic (Happy) and click it.  
<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/TallyZoo-Update01-img04.png" width="150px" >  
1. Happy.json is added to Personium usr data store.  
<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/TallyZoo-Update01-img05.png" width="150px" >  
1. Click the wrench icon to access the Delete menu.   
<img src="https://dixonsiu.demo-jp.personium.io/MyData/images/TallyZoo-Update01-img06.png" width="150px" >  

