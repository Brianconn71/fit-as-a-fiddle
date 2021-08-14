
# Fit as a Fiddle E-commerce Store

![Live Project](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/Responsive-view-of-site.JPG)

[Live Project](https://ms4-fit-as-a-fiddle.herokuapp.com/)

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

## Scope

### Features

## Structure

## Skeleton

## Surface

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

    * Quick Database Diagrams was used to make diagram of database schems

# Testing

# Deployment

* This project was setup on GitHub using the Code Institute Gitpod Template.

* I sourced the code institute github page and then clicked on the green use this as templsate button in the repository.

* Then, i named my repository and created it. upon, creattion, I then clicked on the green gitpod button at the top of the repository to open the template in Gitpod.

* I then used the terminal window in gitpod to create files and folders and to add changes to the version contreol in Github.

* to commit I added the files to the staging area using the following commands:
> git add .
> git commit -m "commit message"
> git push

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
        > pip install
        * then, using the command: pip3 freeze > requirements.txt, I added the dependencies to the requirements file which is needed by Heroku.
        * Then in settings.py I imported dj_database_url:
        > import dj_database_url
        * then, I commented out the current database settings and replaced it with the settings of the postgres database:
        > DATABASES = {
            'default': dj_database_url.parse('DATABASE_URL')
        }
        * DATABASE_URL above is an environmental variable and as such should not be shown  in version control. The database url can be found from your app config settings in heroku.
        * Once the above method is set up, models need to be migrated to the new database using the command below:
        > python3 manage.py migrate
        * I then created a new superuser for my site on heroku using the command below:
        > python3 manage.py createsuperuser
        * When that was done I then commited my changes and made sure not to include environmnet variables in the version control.
        * Then, I created an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and otherwise use the default database in gitpod.
        > if "DATABASE_URL" in os.environ:
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
        * The postgres database should now be ready for use.

    * Gunicorn
        * For the app to work on heroku we need a way for heroku to tell that the app is a web application, which is where Gunicorn comes in.
        * Installing Gunicorn
        `pip3 install Gunicorn`

# Credits

### Content

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


### Acknowledgements

* Various Slack users, too many to mention, for the help along my journey and helping me to get this project set up.

* Brian - Slack user for help structuring my project and organising my database schema

* My mentor Adegbenga Adeye for his help and guidance throughout the project.

