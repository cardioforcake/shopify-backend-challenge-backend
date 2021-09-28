## Stan Chao | Shopify Backend Challenge

[Heroku deployment](https://image-repository-challenge.herokuapp.com/)

#### Full Disclaimer

The application does not function as intended. I decided to try building a separate Django Backend (I have previous experience using Django Views). The app fully functions on the localhost. However, it was not until after I deployed the website that I discovered issues with trying to access the database from Heroku.

I discovered that Heroku does not allow an outisde source to access the embedded SQLite/Postgresql database. In order to access that database, I would need to create a SSL certificate for my frontend. However, the free Heroku account does allow for the creation of SSL certificates.

With additional time, I will implement a SSL certificate to allow my frontend to access my Heroku postgresql database. I have more experience working with Express/MongoDB backend, However, I decided to use Django/Pythong/SQLite3 as I understand that it is similar to Ruby on Rails which is used by Shopify.

See list of features below.

#### Features

- separate [frontend](https://image-repository-challenge.netlify.app/) and [backend](https://image-repository-challenge.herokuapp.com/)
- [Frontend Github](https://github.com/cardioforcake/shopify-backend-challenge-frontend)
- Backend is built using Django and SQLite3 Database
- Backend is configered for Amazon AWS S3 image hosting
- Frontend is built using React and borrows code (repurposed) from my other projects including the [Shopify Frontend Challenge](https://stanchao-shopifychallenge.netlify.app/)
- Features Google Firebase authentication through the frontend
- (Query User Images)User is able to upload images (with "title" and "creator" properties). If images are uploaded while logged in, the use is then able to query the backend to pull up all the images that they added. However the user does not need to be logged in, in order to upload anoynmous images.
- (Delete) While logged in, the user is also able to delete the images that they added. The data for the image passed to the frontend does not include the ID of the user who added to image (however this information is stored in the back end via relationship between User and Image model). A deletion request is sent to the backend with the id of the logged in user. The image is only deleted if the id matches the id stored in the connection table)
- (Query All) A user is able to also see all the uploaded images

