<div id="monetate-product" data-products="interact ">&nbsp;</div>

<div class="info">
<div class="info-title">Countdown Ticker Actions Built By Monetate</div>
<p>Please note, this document is for countdown-ticker actions built by Monetate engineers prior to the existence of "Countdown Timer" actions in ActionBuilder. For more information on "Countdown Timer" actions, please refer to the <a href="http://support.monetate.com/hc/en-us/articles/203103935">"How to Build a Countdown Timer Action"</a> screencast.</p>
</div>

<a name="top"></a>

*  [Overview](#1)
*  [Using a Countdown Ticker in a Campaign](#2)

### <a name="1"></a> Overview

Countdown tickers inform site visitors about the
months, days, or seconds before a notable event begins or ends. Some example uses for countdown tickers include
informing a visitor about how many shopping
days remain in a holiday season, or how much time remains before a sale
ends.

To use a countdown ticker in one of your
<a data-tooltip-large="">campaign</a>s,
you must first contact Monetate Support or your Client Success team to
have the request added to the development queue. This is contingent upon
the products in your contract. To submit your
<a data-tooltip-large="">action</a>
request, you must specify the location of your countdown ticker on your page. Please note, standard development time will
apply.

Once a Monetate engineer builds your action, there are few things
things that you will need before creating a campaign that utilizes a
countdown ticker:

*  An image that is the appropriate dimensions for the area on your
    site where it will live.

    *  Within the image, there should be appropriate blank space for
        the dynamic countdown text.
*  Style information for how the countdown ticker should look (i.e.
    font size, colors, etc.)

    *  [Here](http://www.w3schools.com/cssref/css_colornames.asp) is a good resource for HEX color values used in
        <a data-tooltip-large="">CSS</a>.
        
      

**Sample countdown ticker image:**

![Countdown Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i1.png)

[Back to Top](#top)

### <a name="2"></a>Using a Countdown Ticker in a Campaign

Once you receive your action
<a data-tooltip-large="">action</a> it will be available for use in
any
<a data-tooltip-large="">campaign</a>. You can add your countdown ticker through the **What** part
of the Monetate sentence.

![Countdown
Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i2.png "Image: https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i2.png")

There are several required and optional inputs that you will need to
consider while configuring your ticker action:

Required Inputs
---------------

#### Upload and Configure Image


To begin, upload the image for the backdrop of your
countdown ticker by clicking the “Upload image” link pictured below.

**Note**: 
*This can also be an appropriately sized blank 

placeholder if
you do not have any additional graphics that you would like to display
with your ticker.*

![Countdown Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i3.png)

Once you have uploaded your image (or generated your blank
placeholder), you must create a clickzone on your image to denote where
the actual countdown ticker will display. Select the “Clickzones” link
pictured below.

![Countdown Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i4.png)

On the following screen, create a clickzone by
clicking and dragging a rectangle to match the blank space where your
countdown ticker will display. In the URL text box, include the text
“\#ticker.”

![Countdown Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i5.png "Image: https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i5.png")

**Note**: *You can reposition Clickzones by clicking the light blue
header and moving them to the desired location. You can also resize them
by clicking and dragging the handle at the bottom right corner to the
desired size.*

#### End Time

Once you have uploaded your image and defined your **\#ticker**
clickzone, it 
is 
necessary to set the end time for your countdown
ticker. 
You can adjust time in 
15 minute increments from 12:00am to
11:45pm. You can adjust month and year by clicking the up and down
arrows next to each. To set your desired date, click the number for the
corresponding day. You will need to set the values for to a
future date in order for the your countdown ticker to function.

![Countdown Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i6.png)

**Note**: *If you need to adjust the end time for your countdown ticker
after you have activated your campaign, you can do so within the
[**What**](http://support.monetate.com/hc/en-us/articles/201249857-Understanding-the-What-Predicate)
part of your Monetate campaign sentence structure.*

#### Countdown mode

Adjusting this function allows you to define whether your ticker
deadline should use GMT or localized time. Using **GMT** will cause
your countdown ticker action to have one deadline, regardless of a
visitor’s local timezone, while the **User’s Local** setting will set
the end time relative to a visitor’s timezone. By default this is set to
GMT.

#### Largest Unit

Adjusting 
this function 
designates the largest time increment
to display in your countdown ticker. For example, if
you select **hours**, "2 days" will be displayed as "**48 hours**."

![Countdown
Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i7.png)

#### Smallest Unit

Adjusting this
 function designates the smallest time increment
to display in your countdown ticker. This must be set
less than or equal to your setting in **Largest Time Unit**. For
example, if you select hours as your smallest time unit, "**1 Hour and
20 Minutes"** will display as "**1 Hour**."

#### Ticker Format

Utilizes the format **{01 : 01 : 01}** to designate the format for your
countdown ticker. There should be the same number of units included in
your format to represent all of the units specified in your **Largest
Time Unit** and **Smallest Time Unit** settings. For example, if you set
“days” as your largest time unit and “seconds” as your smallest time
unit, your ticker format should look like **{01 : 01 : 01 : 01}**. The
leading zeros before each unit will designate how many digits appear at
all times. 
For example, "**02 Days 05 Hours 12 Minutes**." This is
used in conjunction with the **Set Zero Values** setting.

![Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i15.png)

Optional Inputs
---------------

#### Set Zero Values

You can adjust this function to designate whether or not the countdown
ticker will display a zero value for any of the units of time measured.
For example, in the case of "**0 Hours 2 Minutes and 0 Seconds**,"
disabling this feature would only display "**2 Minutes**."

#### Add “s” for plural units?

This function determines whether or not your countdown ticker will
display plural units.

#### Preceding Text

You can include optional text that appears before the countdown ticker.
For example, including the text “Time remaining before the sale ends“ in
the text box would display your message inline prior to your countdown
ticker.

**Note**: *To make sure your text appears as expected and
without any formatting or line break issues, be sure to test and preview
your countdown ticker action across multiple browsers and platforms.*

#### Following Text

You can include optional text that appears after the countdown ticker.
For example, including the text “Order before it’s too late!“ in the
text box would display your message inline after your countdown ticker.

**Note**: *In order to make sure your text appears as expected and
without any formatting or line break issues, be sure to test and preview
your countdown ticker action across multiple browsers and platforms.*

#### Hide the banner when loaded after the deadline?

This function determines whether or not to hide your countdown ticker banner 
if it 
loads after the value you have set for “End Time.” If you enable
this function and a site visitor is viewing the banner when
the countdown ticker reaches zero, the banner will remain visible until they reload the page.

#### Time’s Up Message

You can include optional text that will appear once the countdown ticker
has reached the ending time defined for the countdown ticker in **End
Time**. For example, “The sale has now ended.” If you do not include any
text in this field, your timer will display zeros for the time
increments if the time frame set in the **When** part of your campaign
is later than the **End Time** for your ticker action.

#### Time’s Up Style

You can include
<a data-tooltip-large="">CSS</a>
here to define the style for your “Time’s Up” message.

#### Countdown Ticker Style

You can include CSS here to define the style for your countdown ticker
text.

**Note**: *You should only edit these values if you are knowledgeable in
CSS.*

Some common properties are:

|  Property    |         Description           |    Example |

|————---------—|———————------------------------|—---------—--|
  | **text-align**  | Used to set the horizontal alignment for countdown ticker text. You can make text centered, aligned left, aligned right, or justified. |                                                            text-align: center; |
 | **color**  |  Used to set the color for text in your countdown ticker.  | color: \#000000;|
 | **font-weight**   |   Used to set bold or normal emphasis for your text. You can set text to be normal, bold, bolder, or lighter.  You can also set numeric weights from 100 to 900, with 400 equal to normal and 700 equal to bold. |  font-weight: bold; **or** font-weight: 700; |
|  **font-size**   |     Used to set the size of the font for your countdown ticker. |   font-size: 15px; |
 | **text-transform** |  Used to standardize the capitalization for your countdown ticker text. Text can be set at none, capitalize, uppercase, or lowercase. | text-transform:uppercase;  |

#### Banner Div Style

You can adjust the CSS on the `<div>` that for the countdown ticker.


#### Image Element Style

You can adjust the CSS for the image that you inserted for your
countdown ticker. This may include adjusting the cell padding or
borders.

#### Apply this when

Used to apply action conditions to your countdown ticker action. For
example, you can use this to define which pages your countdown ticker
will display on. For more information on using action conditions, please
see the "[Using Action
Conditions](http://support.monetate.com/hc/en-us/articles/201831118-Using-Action-Conditions)"
documentation.

![Countdown Ticker](https://s3.amazonaws.com/elearning.monetate.net/images/src/countdown_ticker/i8.png)

[Back to Top](#top)

<div id="monetate-product" data-products="interact mayberry">&nbsp;</div>

<p><a name="top"></a></p>

<ul>
<li><a href="#7">Why Masking is Used</a></li>
<li><a href="#1">When to Use Masking</a></li>
<li><a href="#2">How Masking Works</a></li>
<li><a href="#3">When Masks are Applied</a></li>
<li><a href="#4">URL Diagram</a></li>
<li><a href="#5">Mask Examples</a></li>
<li><a href="#6">Viewing Masks</a></li>
</ul>

<h3><a name="7"></a>Why Use Masking?</h3>

<p>Content Masking is a method to hide an element or containing element on
a page until after Monetate’s <a data-tooltip-large="">action</a>s complete. You can use Content Masking to hide
elements or containing elements to provide a consistent experience for
all site visitors.</p>

<p><img src="https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i1.png" alt="ActionBuilder Mask
Tab" /></p>

<p><strong>Note</strong>: <em>To utilize masking on a page, you must use the synchronous tag for that page.</em></p>

<h3><a name="1"></a>When to Use Masking</h3>

<p>There are a few instances where it makes sense to use content
masking:</p>

<ul>
<li>If you are currently using the <a href="http://support.monetate.com/hc/en-us/articles/201255843-The-Monetate-Tag#2">synchronous
tag</a>
to run Monetate on your site, you should use Content
Masking on all hide/show actions to create an optimized site
experience for your customers.</li>
<li>Depending on the specifics of your site, it may be beneficial to use
content masking with hide/show
<a data-tooltip-large="">actions</a>
when using the <a href="http://support.monetate.com/hc/en-us/articles/201255843-The-Monetate-Tag#2">asynchronous
tag</a>
as well.</li>
<li>In addition, if you are using a combination of actions that includes
hiding content in one area and then inserting content in another, it
is important to make sure you have masks applied to all areas involved.</li>
</ul>

<p><strong>Example:</strong> </p>

<p>If you are using an action that replaces an element in the
main navigation bar, it makes sense to mask the entire navigation bar
rather than just the part where the action takes place so that all
navigation items appear to load at the same time.</p>

<p><a href="#top">Back to Top</a></p>

<h3><a name="2"></a>How Masking Works</h3>

<p>Once you have enabled content masking in the <strong>Masks</strong> tab, the element
selector will include the specified details for the
element you are looking to mask. The element selector does not allow
CSS3 selectors, sizzle selectors (such as &#35;menu &#62; li.nav:eq(2) ), or
pseudo selectors (such as &#35;menu &#62; li.nav:nth-child(3)). If you use one of these, a warning will show under your selector. This warning
indicates that you must alter the text in your
<a data-tooltip-large="">CSS</a>
selector before applying a mask.</p>

<p><img src="https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i2.png" alt="ActionBuilder CSS
Selector" /></p>

<p>If you are not comfortable editing the text yourself or if you have
further questions about what selectors to use, please contact
Monetate support.</p>

<p><a href="#top">Back to Top</a></p>

<h3><a name="3"></a>Applying Masks</h3>

<p>Monetate applies masks as soon as the tag fires and before anything is
known about the page content or the visitor. Consequently, you cannot use <a href="http://support.monetate.com/hc/en-us/articles/201250106-Understanding-Who-Targeting"><strong>Who</strong>
targets</a>
and <a href="http://support.monetate.com/hc/en-us/articles/201831118-Using-Action-Conditions">action
conditions</a> to determine when to apply masks. Instead, use
URL/path matching. Keep in mind, you should limit content masking to pages where actions occur. To enable content masking,
navigate to the “Mask” tab and check the box labeled “Enable Content
Masking.”</p>

<p><img src="https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i3.png" alt="ActionBuilder Mask
Tab" /></p>

<p><strong>Note</strong>: After you have created your mask, you may experience an initial delay before your mask is visible on your site. If you do not pause your campaign first, this delay may increase. This will only occur for newly created masks. </p>

<p><a href="#top">Back to Top</a></p>

<h3><a name="4"></a>URL Diagram</h3>

<p>To understand where to instruct ActionBuilder to apply a mask, you must
first understand the URL or path that determines when to apply a mask.
Below is a diagram of a URL with parameters to illustrate each section that determines when to apply a mask.</p>

<p><img src="https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i4.png" alt="URL
Diagram" /></p>

<p><a href="#top">Back to Top</a></p>

<h3><a name="5"></a>Mask Examples</h3>

<p>The table below shows five examples of masking rules applied at different times based on their paths and
URLs.</p>

<p><img src="https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i5.png" alt="ActionBuilder Masking Rules
Table" /></p>

<p><a href="#top">Back to Top</a></p>

<h3><a name="6"></a>Viewing Masks</h3>

<p>You can add an action to a  <a data-tooltip-large="">campaign</a> once a mask is set.
On the <strong>Actions Page</strong>, you will be able to see if an action has a mask by
looking for a mask icon. If an action has a black mask
icon, it currently has a mask applied. If there is no mask icon present, it does not have a mask.</p>

<p><img src="https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i6.png" alt="Action Masks
Icon" /></p>

<p>After 30 minutes, you can view the mask for your action.  You must view the mask within the campaign to assure that the mask is functional.
The default preview functionality will not display the mask.</p>

<p><a href="#top">Back to Top</a></p>

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

