# Testing

### Testing was required as part of MS4

#### Responsive Testing

In testing my site for mobile responsiveness I was constantly checking the site using Chrome Dev Tools on the various screen resolutions on offer. I aimed to make the site responsive down as far  as a 280px screen which was achieved through the use of media queries.

friends and family members also tested the site out on their relevant devices and it all worked as expected.

Please see below for a list of all screen sizes that my site was found to be mobile responsive on:

* Galaxy Fold

![Galaxy Fold](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/galaxy%20fold%20screen.JPG)

* Moto G4

![Moto G4](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/moto%204%20screen.JPG)

* Iphone 4

![Iphone 4](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/iphone4%20screen.JPG)

* Galaxy s5

![Galaxy s5](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/galaxy%20s5%20screen.JPG)

* pixel 2

![pixel 2](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/pixel%202%20screen.JPG)

* pixel 2 xl

![pixel 2 xl](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/pixel%202%20xl.JPG)

* iphone 5

![iphone 5](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/iphone%205.JPG)

* iphone 6

![iphone 6](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/iphone%206.JPG)

* iphone 6 plus

![iphone 6 plus](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/iphone%206%20plus.JPG)

* iphone x

![iphone x](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/iphone%20x.JPG)

* ipad

![ipad](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/ipad.JPG)

* ipad pro

![ipad pro](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/ipad%20pro.JPG)

* surface duo

![surface duo](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/surface%20duo.JPG)


### Lighthouse

* I ran my site throught Lighthouse which generated reports for mobile and desktop views.

* Initially, there were some issues regarding alt text of images but I made the changes necessary and please see below for the lightouse reports for both desktop and mobile.

* Desktop
    * ![lighthouse-desktop](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/lighthouse-desktop.JPG)

* Mobile
    * ![lighthouse-mobile](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/lighthouse-mobile.JPG)

### Code validation

#### HTML

* I used W3C Markup validation for my HTML validation and my code passed this test.

![html validation]()

#### CSS

* I used W3C Markup validation for my CSS validation and my code passed this test.

![css validation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/css%20validation.JPG)

#### JavaScript

* I used jshint validation for my JavaScript validation and my code passed this test.

![JavaScript validation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/javascript%20validation.JPG)

#### Python

* I used pep8 validation for my Python validation and my code passed this test.

![python validation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/python%20validation.JPG)

### Manual Testing of site

* The functionality of the site was manually tested to ensure that all worked as expected.

#### Bag App Functionality

* to test the bag, I navigated to the products page, clicked on a product and chose "add to bag"

![add-to-bag](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-to-bag.JPG)

* This worked, so I then went to the bag page and tried to edit the qty of the product in my bag.

![update-bag-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/update-bag-page.JPG)

* I also then tried to remove the item from my bag to test delete functionality.

![delete-bag-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-bag-page.JPG)

#### Checkout App Functionality

* In order to test checkout functionality of the site, I first added an item to my bag and proceeded to secure checkout.

![secure-checkout](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/secure-checkout.JPG)

* Then proceeded to the checkout page and fill in the orderform using stripe.

![orderform](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/orderform.JPG)

* When the order was successful I was redirected to the checkout success page with a summary of my order information

![order success](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/order-success.JPG)

* I then checked my email to ensure I received a confirmation email.

![order-confirmation-email](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/order-confirmation-email.JPG)

* Then i logged into stripe to ensure payment was successful, which it was as seen below.

![stripe confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/stripe-confirmation.JPG)

* I also checked in the admin section of the website to ensure the orderform was created. as seen below it was successful.

![admin-order-confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/admin-order-confirmation.JPG)

#### Products App Functionality

* To test product app functionality, I first had to login as an admin user. To add a product, I clicked on my account at the top of the page and clicked on the product management dropdown.

![product-mgmt](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/product-mgmt.JPG)

* I arrived on the add product page to an empty product item form which I filled in to add a new item to the database.

![add-product-form](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-product-form.JPG)

* Product got added successfully

![successfully-aded-product](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/successfully-aded-product.JPG)

* Only admin users will be able to edit and delete products, which can be seen below.

![add-edit-btns](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-edit-btns.JPG)

* Then I tried to edit the item by clicking edit, This brought me to the edit product page which allowed me to edit the product

![edit-product-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/edit-product-page.JPG)

![edit-confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/edit-post-successful.JPG)

* Finally, I attempted to delete my product from the site, delete confirmation should appear before product gets deleted

![delete-product-modal](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-product-modal.JPG)

![delete-confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-product-confirmation.JPG)

#### Reviews Functionality

* I logged into my account.

* I navigated to the products page and clicked on any product, Then scroll to the bottom of the details page, to find the revies section.

![reviews section](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/reviews_section.JPG)

* I clicked on the add a review header, a review form drop down will then appear.

![leave a review](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/leave-a-review.JPG)

* I filled in the review for the product in question and then clicked add review.

* I then was redirected back to the product detail page, to confirm the review was submitted I clicked on the reviews heading and could see my review.

![review-for-product](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/review%20for%20product.JPG)

* Then I edited the review by clicking on edit. Then went and clicked on reviews again to ensure the review was successfully edited which it was

![edit-review-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/edit-review-page.JPG)

![edited-review](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/edited-review.JPG)

* Then I tested the delete functionality by deleting my review. Delete modal confirmation also popped up for defensive programming reasons

![delete-review-modal](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-review-modal.JPG)

![delete-review-confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-review-confirmation.JPG)

#### Blog Functionality

* I needed to login as an admin user to test the blog functionality.

* I navigated to the blog page and clicked on the add blog post button only visible to admin users.

![add-blog-post-btn](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-blog-post-btn.JPG)

* I was then taken to the add blog post page where i added a new blog post in the form provided.

![add-blog-post-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-blog-post-page.JPG)

![add-post-confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-post-confirmation.JPG)

* I then clicked on the edit button to edit the blog post and was taken to the edit blog post page.

![edit-blog-post-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/edit-blog-post-page.JPG)

![edit-post-successful](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/edit-post-successful.JPG)

* Then I tried to delete the blog post, delete confirmation appearing first however. and confirmation of deletion

![delete blog modal](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-blog-modal.JPG)

![blog-post-deleted](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/blog-post-deleted.JPG)

* I then tried to leave a comment on a blog post, all users have this functionality by clicking on the blog post and scrolling to the comments section at the bottom of the page.

![add-comment](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/add-comment.JPG)

* I then deleted the comment so to test the delete comment is working sufficiently.

![delete-comment-modal](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-comment-modal.JPG)

![delete-comment](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-comment.JPG)

#### contact us Functionality

* To test thye contact form I navigated to the contact us page in the nav bar 

![contact-us-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/contact-us-page.JPG)

* I filled in the contact form and clicked the submit button to send the form.

![contact-us-confirmation](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/contact-us-confirmation.JPG)

![contact-us-admin](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/contact-form-admin.JPG)

#### Profiles Functionality

* To test profiles I needed to be logged in.

* to test profiles functionality, I clicked on my account and clicked my profile.

* I made sure any previous orders were displayed on the right and default customer information was displayed in the form oif the user chose to save their information.

![profile-page](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/profile-page.JPG)

#### Form Functionality

* All forms have been checked to ensure incorrect or blank inputs give errors to the user if aa blank field is empty.

![invalid-forms](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/invalid-forms.JPG)


### Unit Testing

* I did unit tests for each app in my project using Django Unit testing.

* I wrote tests to test for Urls, Models, Apps, Forms and Views.

* All Unit tests were achieved for Models, Forms, Urls and Apps.

* I ran out of time and I had lots of confusion over testing Views so Unfortunately I didn't get the chance to fully test for views but I did tast the Get functionality with unit tests.

* You can see the tests I wrote in the apps tests folder.

* To run the tests from the terminal use the command below with the name of any app in the project e.g. Blog, Bag etc.

    ```python3 manage.py test <appname>```


### Bugs during development

* Navbar placement

    * In testing my site using Google Chrome tools I saw that when the search bar icon was clicked the search bar drop down veered offscreen.

    * I spent a large amount of time trying to understand why this was happening, I tried everything that I could think of and use a vast array of channels e.g Slack, stack overflow etc.

    * I eventually, figured out the issue was that the dropdown menu was using position: absolute which I eventually saw using Google Chrome dev tools, to fix the issue and make the navbar responsive I added the below css class to the dropdown menu.
        ```
            .menu-position-mobile{
                left: 0;
            }
        ```

* Quantity of products in bag app

    * I noticed in the bag app that the user could enter a quantity of the product for under 1 and click update, the website would crash to a 500 error.

    * To fix this I spent a large amount of time trying to understand why this was happening in the first place. I spent time on stack overflow and googling up possible solutions but nothing seemed to work, I went on the slack channels and eventually I found an adequate solution.

    * The solution is below. I didn't want the site to crash for the user if they put in a number below one, If they have the product in the bag then the minimun quantity therefoire has to be one so I added "or 1" to where the function looks for the quantity of items so that the site won't crash and they will have at least one quantity of the item in the bag in case of mistakes, accidents etc.
        ``` quantity = int(request.POST.get('quantity') or 1) ```

* Test Error

    * When I first started to create and run the unit tests for my project I ran into an error regarding the tests module.

    * I spent a lot of time researching this error and It was eventually found that I had not deleted the tests.py file before I ran the tests, My tests are stored in the tests folder for each app and django was trying to run tests from the empty tests.py file.

    * [here](https://stackoverflow.com/questions/37525075/what-does-tests-module-incorrectly-imported-mean) is where I found my solution to the problem.

* Styling issues

    * There were a lot of styling issues I found whilst attempting to change the styling of some of my elements in chrome dev tools.

    * Buttons were turning white on click, when image files were added the site was turning unresponsive on mobile devices etc.

    * To fix the styling and coloring issues I had to use !important to override the bootstrap elements in certain places. To stop the filename from veering offscreen and turning my site unresponsive on mobile I added the text-break class to the paragraph element that held the filename.


## User Story Testing

#### User Story 1

* I want to be able to quickly view the products that the site is selling.

##### Action

* The user will see and be made aware what the site is about and selling via homepage imagery, header cta and navigation links. Navigate to the homepage or by using the navbar to move across the site.

##### Expectation

* The site makes it very clear straight away to the user what the site sells and also clear navigation to understand the categories of products for sale on the site

##### Result

#### User Story 2

##### Action

##### Expectation

##### Result

#### User Story 3

##### Action

##### Expectation

##### Result

#### User Story 4

##### Action

##### Expectation

##### Result

#### User Story 5

##### Action

##### Expectation

##### Result

#### User Story 6

##### Action

##### Expectation

##### Result

#### User Story 7

##### Action

##### Expectation

##### Result

#### User Story 8

##### Action

##### Expectation

##### Result

#### User Story 9

##### Action

##### Expectation

##### Result

#### User Story 10

##### Action

##### Expectation

##### Result

#### User Story 11

##### Action

##### Expectation

##### Result

#### User Story 12

##### Action

##### Expectation

##### Result

#### User Story 13

##### Action

##### Expectation

##### Result

#### User Story 14

##### Action

##### Expectation

##### Result

#### User Story 15

##### Action

##### Expectation

##### Result

#### User Story 16

##### Action

##### Expectation

##### Result

#### User Story 17

##### Action

##### Expectation

##### Result