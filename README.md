COMP225-Project
===

[Frontend Link](https://comp-225-project.vercel.app/)  
[Backend API Link](https://comp-225-project-backend.vercel.app/)

This repo contains the code for Read & Sip. Read & Sip is an app that pairs books 
books with alcoholic beverages. 

# To Start

**Clone the project**  

```Bash
git clone https://github.com/ShengyuanWang/COMP225-Project.git
```

**Download the packages**

```Bash
pip install -r requirements.txt
```

**Start Backend Env**

```Bash
cd backend
flask run
```

**Start Frontend Env**

```Bash
npm init vue@latest
cd frontend
npm install
npm run dev
```


## Backend

**Framework**: `Flask`
The backend uses flask. It pulls book data from the Google Books API and genre data from Open Library API in order to make pairings. Pairings are calculated by finidng the drink that has the most genres in common with a book. Drink key genres are weighted higher in this schema. If there are ties, the book's description is analyzed for its sentiment and thatis compared with the drink. All drink data was custom made for Read & Sip and is found in the book-alcohol-pairings.json file. Due to our hosting platform, there must be two versions of that file, one in backend and one in backend/api. 


## Frontend

**Framework**: `Vue3`

The frontend uses vue3. Images are stored on firebase. To display a pairing for the user, the frontend queries the backend with the user input and the backend sends back a json object representing the pairing.  
