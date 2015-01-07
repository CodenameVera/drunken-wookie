<div id="monetate-product" data-products="interact mayberry">&nbsp;</div>

<a name="top"></a>

*  [Details](#1)
*  [Images](#2)
*  [Countdown Timers](#9)
*  [HTML](#3)
*  [Styles](#4)
*  [Mask](#5)
*  [Conditions](#6)
*  [Inputs](#7)
*  [Naming Your Action](#8)

You can further define and configure your action by entering optional
information in the corresponding tabs that appear in ActionBuilder. The
available tabs are contingent upon the action you are creating. They
include:

*  Details
*  Creatives
*  <a data-tooltip-large="">HTML</a>
*  Styles
*  Conditions
*  Inputs

### <a name="1"></a>Details

In the “Details” tab, you can configure available options for your
action. The options for this tab are dependent on the action
type, illustrated in the examples below.

**Example 1**: 

An image action gives you the options for element selector, selecting all elements, and polling for matched elements. 
![ActionBuilder](http://techdocs.monetate.com/images/action_builder/i26.png)

**Example 2**: 

A
[lightbox](http://support.monetate.com/hc/en-us/articles/201788687)
action gives you the options for [lightbox
ID](http://support.monetate.com/hc/en-us/articles/201788687-Lightboxes#3),
[Display
Frequency](http://support.monetate.com/hc/en-us/articles/201788687-Lightboxes#4),
and Lightbox Container Class.

![ActionBuilder](http://techdocs.monetate.com/images/action_builder/i13.png)

[Back to Top](#top)

### <a name="2"></a>Images

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i14.png)

Within the “Creatives” tab, you have the ability to further define your
action and edit your image with [ContentBuilder](http://support.monetate.com/hc/en-us/articles/203080877). To edit your image click the "edit" button. This will launch ContentBuilder with your image asset, along with any preexisting dynamic text and clickzones included. 

Keep in mind, the “Creatives” tab only appear when you insert or editing an image, background image, or lightbox.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i15.png)

For more information on how to edit your image in ContentBuilder, please refer to the [ContentBuilder](http://support.monetate.com/hc/en-us/sections/200460743) documentation section. 

<div class="info">
<div class="info-title"> Responsive Clickzones </div>
<p> All clickzones on responsive image actions are responsive. If your image is designed to scale to the size of the site visitor’s browser window, clickzones contained within that image will also scale without any additional work.</p>
</div>

[Back to Top](#top)
### <a name="9"></a>Countdown Timers

You will find all of your options for adjusting the appearance of your countdown timer within the "Details" tab. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i38.png)

These options include:

* **End Time**: Determines the time that the counter counts down to 
* **Left Position**: Adjust the timer's horizontal position on the background image
* **Top Position**: Adjusts the timer's vertical position on the background image
* **Time Format**: Determines the timer format in days, hours, minutes, and seconds
* **Countdown ends in**: Determines the timezone that the countdown will end in
   * You can use your timezone, or set a rolling deadline that corresponds to the timezone of your site visitors 
* **Element Selector**: Allows manual adjustment of the element selector
* **Insert Function**: Determines where, in relation to the selected element, the timer will be inserted 
* **Digit Style Options**: Allows adjustments to the font and size of the timer numbers
* **Labels Style Options**: Allows adjustments to the font and size of the timer letters
* **Re-check for Elements**: Allows for polling to look for AJAX site elements

[Back to Top](#top)

### <a name="3"></a>HTML

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i16.png)

**Note:** *The HTML tab displays only when inserting or editing an HTML action.*

[Back to Top](#top)

### <a name="4"></a>Styles

The “Styles” tab allows you to set the styling of an action. You can
specify the alignment, margins, and padding  of your action. You can also define these attributes in the
<a data-tooltip-large="">CSS</a> by
clicking the “edit as raw CSS” link. If the CSS changes in
this step, it appends inline to the element or the container.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i17.png)

[Back to Top](#top)

### <a name="5"></a>Mask

With the “Mask” tab selected, you have the ability to enable Content
Masking on your site.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i18.png)

**Note:** *Content Masking is important to allow certain actions to function as expected. Any hide/show actions that you or your team create should use Content Masking, especially if your site uses the synchronous tag. For more
information, please refer to the
“[Content
Masking](http://support.monetate.com/hc/en-us/articles/201461016)”
documentation.*

[Back to Top](#top)

### <a name="6"></a>Conditions

With the Conditions tab selected, you can define rules
for when the action should appear on your site based on the following
parameters:

*  Page type
*  URL
*  Time
*  Cart Value
*  Landing Page
*  Page breadcrumb
*  Page category
*  On product page
*  On index page

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i19.png)

You can add many conditions to an <a data-tooltip-large="">action</a> for more specific targeting or to only show under certain circumstances.

[Back to Top](#top)

### <a name="7"></a>Inputs

Within the “Inputs” tab, you can customize what parts of the action you can
change at the
<a data-tooltip-large="">campaign</a>
level. This is an important step if you want
to make your action reusable. 

In this example, you can change the image when adding the action to new campaigns. You cannot change the element selector, placement, image style, and image container styles. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i21.png)

Keep in mind, the available inputs depend on
the action type. Different action types display different
inputs that you can select to make the action reusable in the future.

**Note:** *You can only edit inputs while the action is being built. Once the action is created, you will not be able to change which inputs are avaliable for editing in the future.*

[Back to Top](#top)

### <a name="8"></a>Naming your Action

Once you finish adjusting options within the action tabs, you will
need to give your action a unique name, description, category, and
subcategory. After you complete this step, click the “Create” button to
add your action to your Actions page for testing.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i22.png)
[Back to Top](#top)

<p><hr />
<h2>Frequently Asked Questions&nbsp;</h2>
<h3 class="faq">What is the difference between Monetate-created actions and client-created actions?</h3>
<h3 class="faq">What are your Quality Assurance (QA) standards and processes for Actions?</h3>
<h3 class="faq">How do I load external JavaScript files into an ActionBuilder Javascript action?</h3>
<h3 class="faq">How do I change the URL of a link on my page using ActionBuilder?</h3>
<h3 class="faq">What is the difference between using an "Insert" action that replaces an element versus an "Edit" action?</h3>
<h3 class="faq">Are actions reusable in multiple campaigns?</h3>
<hr />
<p><a style="background-color: #ffffff;" href="/hc/en-us/sections/200334758-Actions-ActionBuilder">Return to Category: Actions and ActionBuilder</a></p></p>
