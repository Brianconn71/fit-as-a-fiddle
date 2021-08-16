
# Fit as a Fiddle E-commerce Store

![Live Project](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/Responsive-view-of-site.JPG)

[Live Site](https://ms4-fit-as-a-fiddle.herokuapp.com/)

## Milestone Project 4

* This project was built to showcase my abilites in designing and developing a full-stack web application using the django web framework, HTML, CSS, Javascript and Python.

* The website I have built is a full stack ecommerce web application for a fictional fitness and weight company which I have called Fit as a Fiddle. I took inspiration from a multitude of places for this project from various fitness supplies companies, weights distributors and even other e-commerce stores like MandMdirect.

* The application I have developed uses E-commerce functionality, payments are made using Stripe, a blog section for store owners to use to create SEO friendly blog posts to increase  organic traffic to the site and a comments section for users to add comments for interactivity with the store and leave comments on blog posts, Only registered users can leave comments and leave reviews, review section so that users can voice their own opinion on specific products, Confirmation emails, CRUD functionality for admin users to add, update and delete products reviews and blog posts, comments, CRUD functionality for users to create read update and delete their own reviews in the reviews section and the ability to delete comments they have left on blog posts, admin have authorisation to do anything on the site.

* For the assessor, the admin login details have been included in the comments section when submitting the project.

* Please note that this website is solely for educational purposes so Please don't attempt to enter real credit card details when using the stripe functionality. use the below details for testing purposes.

    * stripe card number: 4242 4242 4242 4242
    * Any card end date you wish
    * Anyy CVV number you wish


# Table of contents

# UX

## Strategy

* I created this site as a way for people who have an interest in all things fitness related to go and for fit as a fiddle to be a one stop shop for all things fitness related, from workout clothes, to weights to cardio equipment and workout plans, I also wanted to implelement a social aspect to the site which I believe was achieved through the use of comments being available on posts for logged in users and through the use of reviews on each of the individual product pages which shows an element of trust in the users and allows them to voice there opinion.
I set up a blog page for the site so that selected admin users can contribute articles to the site that are SEO friendly and lead to more organic traffic to the site and lead to increased revenue.
Admin users get the power to create update and delete everything on the site while users of the site get the power to add edit and delete the reviews they have left for various products and to delete their own comments on blog posts.

### User Stories

* I want to be able to quickly view the products that the site is selling.

* I want to be able to easily navigate throughout the site.

* I want to be able to find out more information about the company and see if they have a social media presence.

* I want to be able to contact the company.

* I would like to be able to search for a specific item using the search bar.

* I want to be able to search the site based on the different categories.

* I want to be able to see all product details before I choose to buy the item

* I want to be able to sort the items based on their price.

* I want to be able to see products price and sizes if they have any.

* I want to be able to add items to my shopping bag

* I would like to be notified when I add items to bag or interact with the site functionality.

* I want to be able to edit my shopping bag.

* I want the checkout process to be quick and painless.

* I want to be able to leave a review of certain products.

* I want to receive confirmation of my order.

* I want to be able to see previous order details.

* I want my details tto be saved to my account for faster purchases in future.

### Site Goals

* I want to be able to add, edit and delete products, blog posts and the ability to delete comments from blog posts easily.

* I want to be able to increase organic visitors to the site using SEO friendly blog posts.

* I want an admin section of the site and to have access to such.

* I want customers to have a relaxed and trouble free time on the site.

* I want the site to be fully mobile responsive.


## Scope

### Features

##### Navbar

![navbar]()

* The navbar contains the main links and navigation throughout the site. it remains consistent at the top of each page.

* The navbar is fully mobile responsive and reacts to changes in screen size. It also allows for collapsible menu on mobile screens.

* The navbar also contains all the categories of products on the site through the various drop downs.

* The search bar disappears on mobile view but still works when the search icon is clicked, my account and bag also work on mobile view.

![navbar mobile]()

##### Delivery Information Banner

![delivery]()

* The delivery information banner appears just below the navbar on each page, it is fully mobile responsive and reacts to the changes in screen size.

* The delivery banner provides a clear and concise message to the user about needing to spend 60 euro to get free delivery.

##### Footer

![footer]()

* The footer contains links to the social media channels of the company aswell the copyright. These links all open in a new tab on the relevant social media platform.

* The social media icons will have a hover transition in place. This transition changes the social media icon to the main color of that social media platforms site.

* The Footer is mobile responsive and reacts to changes in screen size.


## Structure

* The overall structure of the site will remain consistent throughout the project. A backgroung image with CTA will appear on the homepage which will provide the user with a clear intent on what it is That I want them to do on the site. This background image will then be covered with an overlay for the remainder of the site and content and data will be displayed on the overlay.

* Forms will be displayed using bootstrap styling in a similar manner throughout the site, Reviews form will be designed manually instead of using crispy forms which uses bootstrap styling. Only logged in users will be allowed to leave a review of a product of a comment on a blog post. Logged in admin will have full CRUD functionality over all aspects of the site.

* Navigation, navbars on mobile and desktop views will remain consistent throughout the site.

* Links and buttons will be used throughout the site to allow for easier navigation between pages and the functionality of the site.

## Skeleton

#### Wireframes

[Click here](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/wireframes.pdf) to see the Wireframes I used for this project.

![wireframes](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/wireframes.pdf)

#### Database Schema

![db schema](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/database%20schema.JPG)

##### Models

* blog
    * Post
        * This model contains information relating to the blog posts on the site.
    
    * Comment
        * This model contains information about comments on any of the blog posts on the site.

* Checkout
    * Order
        * This model contains information relating customers orders, their order details and any items they have ordered.
    
    * OrderLineItem
        * This model contains information the products in the customers order, quantity and total with or without a deliery charge

* Products
    * Product
        * This model contains information relating to all the products for sale on the site.
    
    * Categories
        * This model contains information about the various different categories of products on the site.

* Profiles
    * UserProfile
        * This model contains the default order details saved from customers previous orders which they can use for future orders.

* Reviews
    * Review
        * This model contains information relating to reviews that users have left for certain products.


## Surface

* Ultimately, There are differences in my wireframes look to the overall project. I created the homepage wireframes and I just lacked inspiration to create the other wireframes. I wanted the site to look similar to the Boutique Ado walkthrough project and I just lacked inspiratioon to create the Wireframes for the other pages. Initially, I had planned a different background image and a different style of button on the homepage header but once it was set up I didn't like it so I changed it to the way that it is currently set up.

* Once I had the homepage set up in the wireframes I wanted it to be consistent coloring, fonts etc throughout the project so I started to make the project based on the homepage wireframes.

#### Colors

* The colors that I used in this project were sourced using [paletton](https://paletton.com/#uid=1000u0kllllaFw0g0qFqFg0w0aF). I sepnt a lot of time trying to find the best color scheme for the site, I wanted a custom scheme so I spent a lot of time chopping and changing the colors on paletton.

* There are two main colors used throughout the project and they are listed below.
    * #61988E - this is the turquise color used on buttons, text in the header setc
    * #493843 - this is the dark purple/brown color used in the header and footer as well as border colors fonts etc.
    * #f5f5f5 - this is the off-white color used in the modal, forms, all auth etc. I wanted to have a nice easy to read white color and this was my preferred choice.
    * The below are the arrow colors, taken from the walkthrough project as I liked them.
        * #007bff
        * #6c757d
        * #28a745
        * #dc3545
        * #ffc107
        * #17a2b8
        * #f8f9fa
        * #343a40
    * The colors used for the hover over the social media links in my footer are below.
        * instagram - #C13584
        * twitter - #1DA1F2
        * facebook - #4267B2
    * #f9a602 - this is the gold color of the stars in the reviews section.

#### Images

* Images are credited below in the media section.

#### Fonts

* The two fonts used mainly throughout this project are Roboto and Ubuntu. The were sourced using [Google fonts](https://fonts.google.com/). Ubuntu was used mainly as heading text wehereas Roboto was used mainly for paragraph text. The default font was sans-serif.

* I chose these fonts together as it was recommended by google to use these two together and from what I saw they looked very visually appealing together so I chose to uise them together on my site.

# Technologies Used

* [HTML](https://html.com/)

    * HTML was used to create the content and base of each page.

* [CSS](https://en.wikipedia.org/wiki/CSS)

    * CSS was used to then style the page and make it responsive through media queries, and interactive through using CSS transitions.

* [JavaScript](https://www.javascript.com/)

    * JavaScript was used throughout the website to make the site interactive.

* [jQuery](https://jquery.com/)

    * jQuery was used throughout the website to aid with thefunctionality of certain poages and the features avaliable to end users, Blog, Reviews etc..

* [Python](https://www.python.org/)

    * Python was used to build the backend functionality of the web app.

* [Django](https://www.djangoproject.com/)

    * Django was used to create my project.

* [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/)

    * Django AllAuth  was used to create the sign-in and register account functionality of the project.

* [Django Countries](https://pypi.org/project/django-countries/)

    * Django Countries was used to select countries in the order form.

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

    * Django Crispy Forms was used to style form elements

* [Stripe](https://stripe.com/ie)

    * stripe was useed as the payment section of the site.

* [Heroku](https://signup.heroku.com/)

    * Heroku was used to deploy the site and host it.

* [AWS](https://aws.amazon.com/)

    * Amazon Aws was used to store the images on the site and the static files.

* [Gunicorn](https://gunicorn.org/)

    * Gunicorn was used to deploy the site to Heroku

* [Github](https://github.com/)

    * Github was used to host and store the source code of the project.

* [Gitpod](https://gitpod.io/)

    * Gitpod was the IDE that was used to create this project.

* [Git](https://git-scm.com/)

    * Git is the version control software used on the site. it was used to add, commit and push the code changes to github.

* [Figma](https://www.figma.com/)

    * Figma was used to create the wireframes of the site.

* [Font Awesome](https://fontawesome.com/)

    * Font Awesome was used to source and find the icons used on the site.

* [Favicon](https://favicon.io/)

    * Favicon was used to create and add a favicon to the site.

* [Google Fonts](https://fonts.google.com/)

    * Fonts used on the site were found. fonts used on site were, Roboto and Ubuntu

* [Canva](https://canva.com/)

    * Canva was used to create the favicon design for the site.

* [Paletton](https://paletton.com/)

    * Paletton was used to source the colors that were used on the site.

* [Techsini](https://techsini.com/multi-mockup/)

    * Techsini is a mockup generator and It was used to get the mock up image of the site in the Readme.

* [W3](https://www.weschools.com/)

    * W3 Schools was used to troubleshoot issues regarding html css and python throughout the course of thye project.

* [Autoprefixer](https://autoprefixer.github.io)

    * Autoprefixer was used to parse my css file and add the vendor prefixes.

* [Chrome dev tools](https://www.google.com/chrome/dev/)

    * Google chrome tools were used for debugging purposes and to test different css styles and layouts of features.

* [Bootstrap 5](https://getbootstrap.com/)

    * Bootstrap was used to add html/css components to the site and to make the site more visually appealing to the user.

* [Quick Database Diagrams](https://www.quickdatabasediagrams.com/)

    * Quick Database Diagrams was used to make diagram of database schema

* [Box shadow generator](https://cssgenerator.org/box-shadow-css-generator.html)

    * Box shadow generator was used to apply a box shadow to blog posts in the blog page.

# Testing

# Deployment

* This project was setup on GitHub using the Code Institute Gitpod Template.

* I sourced the code institute github page and then clicked on the green use this as templsate button in the repository.

* Then, i named my repository and created it. upon, creattion, I then clicked on the green gitpod button at the top of the repository to open the template in Gitpod.

* I then used the terminal window in gitpod to create files and folders and to add changes to the version contreol in Github.

* to commit I added the files to the staging area using the following commands:
    * `git add .`
    * `git commit -m "commit message"`
    * `git push`

#### Deployment to Heroku

Once app was setup and ready to go I deployed to Heroku by following the steps below:

* I created an app on the heroku website which i called ms4-fit-as-a-fiddle

    * I clicked on the new button.
    * I then clicked on the create a new app link.
    * I then gave my app the name of ms4-fit-as-a-fiddle and chose europe as my closest region.
    * Finally, I selected to create my app.

* Next, I set up the postgres database.

    * in Heroku,
        * Go to app resources section, search for postgres
        * then I chose to add to project and chose the free plan for my project.
        * In order to use Postgres, I had to install two dependecies in gitpod, dj_database_url and psycopg2
    
    * in Gitpod
        * I installed both dj_database_url and psycopg2 using the command:
            * `pip install`
        * then, using the command: pip3 freeze > requirements.txt, I added the dependencies to the requirements file which is needed by Heroku.
        * Then in settings.py I imported dj_database_url:
            * `import dj_database_url`
        * then, I commented out the current database settings and replaced it with the settings of the postgres database:
        ```
        DATABASES = {
            'default': dj_database_url.parse('DATABASE_URL')
        }
        ```
        * DATABASE_URL above is an environmental variable and as such should not be shown  in version control. The database url can be found from your app config settings in heroku.
        * Once the above method is set up, models need to be migrated to the new database using the command below:
            * `python3 manage.py migrate`
        * I then created a new superuser for my site on heroku using the command below:
            * `python3 manage.py createsuperuser`
        * When that was done I then commited my changes and made sure not to include environmnet variables in the version control.
        * Then, I created an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and otherwise use the default database in gitpod.
        ```
        if "DATABASE_URL" in os.environ:
                DATABASES = {
                    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
          else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
        ```
        * The postgres database should now be ready for use.

    * Gunicorn
        * For the app to work on heroku we need a way for heroku to tell that the app is a web application, which is where Gunicorn comes in.
        * Installing Gunicorn
            * `pip3 install Gunicorn`
        * A Procfile then needs to be created to tell heroku how to run our app. this is acheieved below:
            * `touch Procfile`
        * In the Procfile we need to tell it to use a webserver, this is achieved by placing the below code in the procfile:
            * `web: gunicorn <appname>.wsgi:application`
    
    * We now need to connect to Heroku in the terminal on gitpod
        * use the following command
            * `heroku login -i`
        * Login using your email and password that you used to create an account with on heroku website.
        * then, I disabled the collection of static files temporarily until AWS has been set up.
            * `heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>`
            * the --app command is used when you have more than one app in your heroku account
        * Now, in settings I added heroku into my list of allowed hosts, and localhost so the project can still b run locally using the following settings.
            * `ALLOWED_HOSTS = ["<heroku appname>.herokuapp.com", "localhost"]`
        * changes were then pushed to Github
        * Then I needed to set up pushing to heroku achieved below
            * `heroku git:remote -a <heroku appname>`
        * then the project gets pushed to github using:
            * `git push heroku master`
        * Heroku now builds the app.
    
    * On the Heroku Website
        * Go to the deploy section of the app.
        * I searched for the app being used in github
        * When it was found I connected and then clicked on enable Automatic deploys
        * Now any changes pushed to Github will automatically be pushed to Heroku too.
    
    * Amazon AWS
        * Amazon AWS was used to store both static and media files of my project
        * I created an AWS account and worked through the process of signing-in. Once my account was setup I was able to set my project up on aws.
        * first, I needed to create a bucket.
            * search for aws s3 service.
            * click on the Create Bucket button.
            * Give the bucket a unique name and then select the region.
            * uncheck the block public access and acknowledge that the bucket will now be public.
            * click create bucket.
        * Bucket settings
            * Properties
                * Go to the bucket Properties section
                * Turn on static website hosting
                * in the index and error text inputs, add index.html and error.html.
                * then, click save.
        * Permissions
            * Go to the bucket Permissions section.
            * In the cors config paste in the below code:
                * ```
                    [
                        {
                            "AllowedHeaders": [
                                "Authorization"
                            ],
                            "AllowedMethods": [
                                "GET"
                            ],
                            "AllowedOrigins": [
                                "*"
                            ],
                            "ExposedHeaders": [

                            ]
                        }
                    ]
                  ```
            * In the bucket policy, click on the generate policy
        * Policy
            * Select S3 bucket policy
            * Add * to the principal field to select all principals
            * select action to get object
            * Paste in your ARN which can be found on the bucket policy page.
            * click add statement
            * then, click on the generate policy button
            * then, copy and paste the new policy into your bucket policy
            * also, add /* onto the end of the resources key
            * and, click save.
        * Access Control List
            * Go to the Access Control List section.
            * set list objects permission to everyone.
    
    * Create a new user

        * On the admin page for aws search for IAM to add a new user
        * Create a group
            * We need to create a group to put our user in
            * Click create a new group and name it.
            * click through to the end and save the group.
            * create a group policy
                * click policy and the click create policy
                * select the JSON tab and then import managed policies.
                * search s3 and select on Amazons3fullaccess and import.
                * in the resources section, paste in the ARN that was used above.
                * click through to review policy.
                * fill in the name and description and then click generate policy.
            * back into the group, click on permission and attach the policy.
            * find the policy you have just created and attach it.

        * Create the user
            * select users from the sidebar and then click on add user
            * create a username and then select programmatic access then click on next.
            * select the group to add your user too
            * click through to the end and then click create user.
            * Download the CSV file containing the user keys needed to access the app
    
    * Connect bucket to Django
        * first install two packages in the IDE, boto 3 and django storages, seen below:
            * ```
                pip3 install boto3
                pip3 install django-storages
              ```
        * Now we need to add this to our requirements.
            * `pip3 freeze > requirements.txt`
        * storages then needs to be added to installed apps in settings.py
        * an environment variable called USE_AWS needs to be set up to run the code on heroku.
        * The settings needed for the project in the settings.py file are below:
            * ```
                if "USE_AWS" in os.environ:
                    # Bucket configurations
                    AWS_STORAGE_BUCKET_NAME = "<bucket name>"
                    AWS_S3_REGION_NAME = "<bucket region>"
                    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") # taken from downloaded csv file
                    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") # taken from downloaded csv file
                    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                    # static and media files
                    STATICFILES_STORAGE = "custom_storages.StaticStorage"
                    STATICFILES_LOCATION = "static"
                    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
                    MEDIAFILES_LOCATION = "media"

                    # now need to override static and media Urls for production
                    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
              ```
        * Back in heroku click on settings tab and then click reveal config vars.
        * Then set up the environmental variables as required.
        * Back in the IDE, we need to create a custom storages.py to tell django that in production we want to use Amazon S3 to store our static and media files
        * import S3Boto3Storage at the top of the custom_storages.py file.
        * Set up classes to tell django where to store the files as shown below:
            * ```
                class StaticStorage(S3Boto3Storage):
                    location = settings.STATICFILES_LOCATION
                
                class MediaStorage(S3Boto3Storage):
                    location = settings.MEDIAFILES_LOCATION
              ```
        * push all the changes to Github from the IDE
    
    * Add Media files to AWS
        * in your AWS bucket, create a new folder called media
        * select upload and then upload all your image files
        * select to grant public access
        * finally, click to upload your files.
    
    * Setting the project up locally

        * Find your github repo, on the code dropdown click on Download Zip as seen below.
            * ![download Zip](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/download_zip.JPG)
        * then choose to extract files to your respository.
        * open the IDE of your choice and open the folder contaoining the code using your IDE.
        * Once this is done, you can now download the requirements needed to run the project using the below command in your IDE terminal:
            * ` pip3 install -r requirements.txt `
        * You can also choose to clone your files from github to your repository in the IDE by again, choosing the code dropdown in tour github repo and copying the HTTPS url that is provided in the dropdown as seen below:
            * ![https code](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/download_zip.JPG)
        * then when the url has been copied return to your terminal and use the code below:
            * ` git clone https://github.com/Brianconn71/fit-as-a-fiddle.git`
        * once this is done, you then need to set up the below environment variables to use full functionality of the site:
            * DJANGO_SECRET_KEY = your secret key
            * STRIPE_PUBLIC_KEY = your stripe public key
            * STRIPE_SECRET_KEY = your stripe secret key
            * STRIPE_WH_SECRET = your stripe webhook secret
            * IN_DEVELOPMENT = True
            * Your stripe variables which can be found on your stripe dashboard
            * You need a Django secret key which can be found [here](https://miniwebtool.com/django-secret-key-generator/)
        * Then you need to migrate the database models to set up your own database.
            * first check for migrations:
                `python3 manage.py makemigrations --dry-run`
            * then make migrations:
                * `python3 manage.py makemigrations`
            * check to see how migrations will work out:
                * `python3 manage.py migrate --plan `
            * lastly, if all looks good, migrate:
                * `python3 manage.py migrate`
        * Now, a superuser account needs to be created to access the admin section, so follow the step below to create a superuser
            * ` python3 manage.py createsuperuser `
        * enter your own username and password
        * finally, we need to run the project to ensure working order and we are good to go.
            * ` python3 manage.py runserver`


# Credits

### Content

* The idea for my project was taken from my own inspiration on how I would personally like a fitness website to be setup. It is a simple application but it does the job That is asked of it and I am happy with the outcome. I wanted the site to appear minimaslist so as to appeal to every generation and make it a one stop shop for all fitness needs.

* [bootstrap 5](https://getbootstrap.com/) was used to style the site and to make it more visually appealing for the reader and user.

* Some of the backend code was taken from the walkthrough project of Boutique Ado and some frontend bootstrap classes are similar to what was used in the walthrough project as I wanted a similar feel for my site.

* All Images on the site were taken from either [unspalsh](https://unsplash.com/) or [pexels](https://www.pexels.com/).

* all written content on the site including products and their descriptions are my own words. some of the blog posts uses Lorem Ipsum text which I sourced from [here](https://loremipsum.io/)

* Got help with testing using StringIo for adding products [here](https://gist.github.com/drillbits/5432699)

* used pagination in my project, got help [here](https://www.youtube.com/watch?v=wmYSKVWOOTM)

### Media

* Product images

    * Running shorts [Image](https://www.pexels.com/photo/running-man-1578384/) by [pexels user](https://www.pexels.com/@runffwpu)
    * swimming shorts [Image](https://www.pexels.com/photo/topless-man-near-beach-1574898/) by [pexels user](https://www.pexels.com/@thfotodesign)
    * womens gym shorts [Image](https://www.pexels.com/photo/sportive-woman-with-fitness-ball-6453572/) by [pexels user](https://www.pexels.com/@marta-wave)
    * mens gym shorts [Image](https://www.pexels.com/photo/young-man-sitting-on-fitness-equipment-3764010/) by [pexels user](https://www.pexels.com/@olly)
    * mens grey shirt [Image](https://www.pexels.com/photo/man-in-grey-shirt-and-black-bottom-lifting-barbell-812746/) by [pexels user](https://www.pexels.com/@frame-kings-255818)
    * mens navy shirt [Image](https://www.pexels.com/photo/man-carrying-barbel-on-his-back-looking-down-812733/) by [pexels user](https://www.pexels.com/@frame-kings-255818)
    * mens white shirt [Image](https://www.pexels.com/photo/man-wearing-white-crew-neck-t-shirt-806626/) by [pexels user](https://www.pexels.com/@frame-kings-255818)
    * female crop top [Image](https://www.pexels.com/photo/woman-in-pink-crop-top-and-jogging-pants-practicing-yoga-7346634/) by [pexels user](https://www.pexels.com/@kool-shooters)
    * superman stringer [Image](https://www.pexels.com/photo/blue-and-red-superman-print-tank-top-shirt-38630/) by [pexels user](https://www.pexels.com/@pixabay)
    * white tank top [Image](https://www.pexels.com/photo/strong-asian-man-training-biceps-in-gym-6550866/) by [pexels user](https://www.pexels.com/@pixabay)
    * 5kg dumbbells [Image](https://www.pexels.com/photo/crop-man-exercising-with-dumbbell-in-gym-6550838/) by [pexels user](https://www.pexels.com/@pixabay)
    * 50kg Barbell [Image](https://www.pexels.com/photo/photo-of-man-lifting-barbell-1552106/) by [pexels user](https://www.pexels.com/@leonardho)
    * 100kg Barbell [Image](https://www.pexels.com/photo/person-holding-black-and-silver-steel-barbell-photography-949126/) by [pexels user](https://www.pexels.com/@victorfreitas)
    * Spin Bike [Image](https://www.pexels.com/photo/modern-stationary-bicycles-in-gym-4254902/) by [pexels user](https://www.pexels.com/@mvdheuvel)
    * treadmill [Image](https://www.pexels.com/photo/tired-man-walking-on-treadmill-in-gym-6455846/) by [pexels user](https://www.pexels.com/@julia-larson)
    * rowing machine [Image](https://www.pexels.com/photo/man-using-a-rowing-machine-7690218/) by [pexels user](https://www.pexels.com/@cottonbro)
    * 6 week fat burn [Image](https://www.pexels.com/photo/black-sneakers-and-gym-tools-on-gray-floor-6740822/) by [pexels user](https://www.pexels.com/@mikhail-nilov)
    * fighting fit [Image](https://www.pexels.com/photo/determined-black-boxer-hitting-heavy-bag-during-training-in-gymnasium-6998875/) by [pexels user](https://www.pexels.com/@gabby-k)
    * Yoga [Image](https://www.pexels.com/photo/woman-doing-yoga-exercise-in-the-morning-7592740/) by [pexels user](https://www.pexels.com/@miriam-alonso)
    * Weight Bench [Image](https://www.pexels.com/photo/photo-of-woman-raising-dumbbells-2475878/) by [pexels user](https://www.pexels.com/@823sl)
    * 9kg [Image](https://www.pexels.com/photo/person-holding-black-dumbbells-1032117/) by [pexels user](https://www.pexels.com/@micah-boerma-327482)
    * Home Gym [Image](https://www.pexels.com/photo/woman-kneeling-with-barbel-on-shoulders-3076514/) by [pexels user](https://www.pexels.com/@jonathanborba)
    * Weight Belt [Image](https://www.pexels.com/photo/barbell-near-belt-949132/) by [pexels user](https://www.pexels.com/@victorfreitas)
    * Weight plates [Image](https://www.pexels.com/@victorfreita) by [pexels user](https://www.pexels.com/@victorfreitas)
    * Baseball cap [Image](https://www.pexels.com/photo/man-wearing-blue-and-black-crew-neck-shirt-1103831/) by [pexels user](https://www.pexels.com/@ollivves)

* Homepage background image

    * Homepage background image [Image](https://unsplash.com/photos/0Wra5YYVQJE) by [unsplash user](https://unsplash.com/@karsten116)

### Code Snippets

* Got a hand with unittesting in django using this [Youtube series](https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=7) and some other [resources](https://tech.people-doc.com/django-unit-test-your-views.html) [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)

* got help with my comment model from this youtube series [here](https://www.youtube.com/watch?v=OuOB9ADT_bo&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=46)

* Got a hand with calculating average reviews from users ratings [here](https://stackoverflow.com/questions/28607727/how-to-calculate-average-with-django)

* Used code from this [codepen](https://codepen.io/AdamCCFC/pen/WvzBKq) to help style the social media icons in my footer.

* [stack Overflow](https://stackoverflow.com/questions/40457680/how-do-you-slugify-a-url) helped me to automatically set up the slug for a new blog post.

* When testing out my project, I ran into one particular bug that I needed helping figuring out, I got an answer to my query [here](https://stackoverflow.com/questions/37525075/what-does-tests-module-incorrectly-imported-mean)

* When working on the checkout process with Stripe I ran into another bug which I solved with help from [stack overflow](https://stackoverflow.com/questions/59542045/getting-attributeerror-in-django)

* when creating the reviews app I got help from this series of youtube [videos](https://www.youtube.com/watch?v=lSX8nzu9ozg)

* I also used this article from [medium](https://medium.com/django-rest/lets-build-a-basic-product-review-backend-with-drf-part-1-652dd9b95485) to help in the development of the reviews model and this [webpage](https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a) to help in my understanding.

* When working on the delete products, reviews and blog posts I used a bootstrap modal to confirm deletion. I used this [website](https://www.codegrepper.com/code-examples/python/django+loop+index) to help with for loop counters in django.

* In making my site more responsive, I ran into an issue with button height, this was resolved using and inline-flex display which I found [here](https://stackoverflow.com/questions/51256154/how-to-make-button-same-height)


### Acknowledgements

* Various Slack users, too many to mention, for the help along my journey and helping me to get this project set up.

* Brian - Slack user for help structuring my project and organising my database schema

* My mentor Adegbenga Adeye for his help and guidance throughout the project.

