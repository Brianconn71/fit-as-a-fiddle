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

![add-to-bag]()

* This worked, so I then went to the bag page and tried to edit the qty of the product in my bag.

![update-bag-page]()

* I also then tried to remove the item from my bag to test delete functionality.

![delete-bag-page]()

#### Checkout App Functionality

* In order to test checkout functionality of the site, I first added an item to my bag and proceeded to secure checkout.

![secure-checkout]()

* Then proceeded to the checkout page and fill in the orderform using stripe.

![orderform]()

* When the order was successful I was redirected to the checkout success page with a summary of my order information

![order success]()

* I then checked my email to ensure I received a confirmation email.

![order-confirmation-email]()

* Then i logged into stripe to ensure payment was successful, which it was as seen below.

![stripe confirmation]()

* I also checked in the admin section of the website to ensure the orderform was created. as seen below it was successful.

![admin-order-confirmation]()

#### Products App Functionality

* To test product app functionality, I first had to login as an admin user. To add a product, I clicked on my account at the top of the page and clicked on the product management dropdown.

![product-mgmt]()

* I arrived on the add product page to an empty product item form which I filled in to add a new item to the database.

![add-product-form]()

* Product got added successfully

![successfully-aded-product]()

* Only admin users will be able to edit and delete products, which can be seen below.

![add-edit-btns]()

* Then I tried to edit the item by clicking edit, This brought me to the edit product page which allowed me to edit the product

![edit-product-page]()

![edit-confirmation]()

* Finally, I attempted to delete my product from the site, delete confirmation should appear before product gets deleted

![delete-product-modal]()

![delete-confirmation]()

#### Reviews Functionality

* I looged into my account.

* I navigated to the products page and clicked on any product, Then scroll to the bottom of the details page, to find the revies section.

![reviews section](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/reviews_section.JPG)

* I clicked on the add a review header, a review form drop down will then appear.

![leave a review](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/leave-a-review.JPG)

* I filled in the review for the product in question and then clicked add review.

* I then was redirected back to the product detail page, to confirm the review was submitted I clicked on the reviews heading and could see my review.

![review-for-product]()

* Then I edited the review by clicking on edit. Then went and clicked on reviews again to ensure the review was successfully edited which it was

![edit-review-page]()

![edited-review]()

* Then I tested the delete functionality by deleting my review. Delete modal confirmation also popped up for defensive programming reasons

![delete-review-modal]()

![delete-review-confirmation]()

#### Blog Functionality

* I needed to login as an admin user to test the blog functionality.

* I navigated to the blog page and clicked on the add blog post button only visible to admin users.

![add-blog-post-btn]()

* I was then taken to the add blog post page where i added a new blog post in the form provided.

![add-blog-post-page]()

![add-post-confirmation]()

* I then clicked on the edit button to edit the blog post and was taken to the edit blog post page.

![edit-blog-post-page]

![edit-post-successful]()

* Then I tried to delete the blog post, delete confirmation appearing first however. and confirmation of deletion

![delete blog modal](https://github.com/Brianconn71/fit-as-a-fiddle/blob/master/Readme%20Images/delete-blog-modal.JPG)

![blog-post-deleted]()

* I then tried to leave a comment on a blog post, all users have this functionality by clicking on the blog post and scrolling to the comments section at the bottom of the page.

![add-comment]()

* I then deleted the comment so to test the delete comment is working sufficiently.

![delete-comment-modal]()

![delete-comment]()

#### contact us Functionality

* To test thye contact form I navigated to the contact us page in the nav bar 

![contact-us-page]()

* I filled in the contact form and clicked the submit button to send the form.

![contact-us-confirmation]()