<div id="monetate-product" data-products="interact ">&nbsp;</div>

<a name="top"></a>

*  [Overview](#1)
*  [Adding the All In One HTML/CSS/JS action to a campaign](#2)
*  [Configuring the All In One HTML/CSS/JS
    action](#3)
*  [Sample All In OneHTML/CSS/JS Action](#4)

### <a name="1"></a>Overview

The All-In-One <a data-tooltip-large="">HTML</a>/<a data-tooltip-large="">CSS</a>/<a data-tooltip-large="">JavaScript</a> <a data-tooltip-large="">action</a> allows you to insert HTML, CSS styles,
and JavaScript into the same action in your <a data-tooltip-large="">campaign</a>. All-In-One actions are ideal
when the action requires HTML and JavaScript to
work together. To have the All-In-One HTML/CSS/JS action added to your
account, contact your Monetate support team.

Only someone with a knowledge of Javascript, HTML, and CSS and how each
can affect a website should configure this type of action.
After creating an All-In-One action, it is important to test the action in different browsers and browser versions.

<div class="info">
<div class="info-title"> Action Testing</div>
<p>Monetate will not test changes that you or your
team make to your site using the All-In-One action.</p>
</div>

[Back to Top](#top)

### <a name="2"></a>Adding the All In One HTML/CSS/JS Action to a Campaign

To add the All-In-One HTML/CSS/JS action to your campaign:

*  Create a new campaign or click a campaign to which you would like to
    add the action
*  Select the **What** part of your campaign setup
*  Click the "Add Action" link
*  Click "Other"
*  Click the "All In One HTML/CSS/JS action" link listed under the "Any
    Page" heading

![All In One HTML/CSS/JS
Actions](https://s3.amazonaws.com/elearning.monetate.net/images/src/all_in_one/i1.png)

For more information about creating a campaign, please refer to
the [Campaign
Overview](http://support.monetate.com/hc/en-us/articles/201205673)
screencast.

[Back to Top](#top)

### <a name="3"></a>Configuring the All In One HTML/CSS/JS Action

The All In One HTML/CSS/JS action is highly configurable and has several
required and optional inputs.

#### Required Inputs

![All In One HTML/CSS/JS
Actions](https://s3.amazonaws.com/elearning.monetate.net/images/src/all_in_one/i2.png)

**HTML Creative**

You can use existing HTML for this action by clicking
"Choose existing HTML." You can use new HTML by clicking
 "Upload HTML."

Any Javascript included in your HTML creative will not run as a
result of how browsers interpret code inserted into a webpage. Insert this code into your JavaScript creative instead.

Javascript and CSS running on your site can affect any elements in your HTML creative that have the same ID or class name. Use different ID and class names for the
elements in your HTML creative to prevent this from occurring.

**CSS3 Selector**

This is the HTML element that will be searched to input your HTML
creative. For example, to target the tag inside of a tag, the CSS3
Selector would be *\#box \> span*. For more information on CSS3
Selectors, please consult the W3C Documentation on [CSS3
Selectors](http://www.w3schools.com/cssref/css_selectors.asp).

**Insert Function**

This specifies, based on the CSS3 selector that you have chosen, what
the Monetate script should do to insert your content on the page. The
 options include:

*  **After**: Adds the content after the CSS3 selector
*  **Before**: Adds the content before the CSS3 selector
*  **Replace**: Hides the original CSS3 selector and inserts a new
    selector in its place
*  **First Child**: Adds the element into the first part of a bulleted
    or numbered list
*  **Last Child**: Adds the element to the last part of a bulleted or
    numbered list
*  **Takeover**: Replaces the content inside the CSS3 selector with
    your image

#### Optional Inputs

![All In One HTML/CSS/JS
Actions](https://s3.amazonaws.com/elearning.monetate.net/images/src/all_in_one/i3.png)

**JavaScript Creative**

You can use existing JavaScript creatives by
clicking "Select JavaScript." You can use new JavaScript creatives by
clicking  "Upload JavaScript."

**CSS Style Properties**

Allows you to insert the specific styles related to HTML creatives in
this action.

**Apply this when**

Provides conditions for when this action should or should not run.

[Back to Top](#top)

### <a name="4"></a>Sample All In OneHTML/CSS/JS Action

![All In One HTML/CSS/JS
Actions](https://s3.amazonaws.com/elearning.monetate.net/images/src/all_in_one/i4.png)

To add the following interactive box to your site, use the following
inputs for your All-In-One HTML/JS/CSS action:

**HTML Creative**

![All In One HTML/CSS/JS
Actions](https://s3.amazonaws.com/elearning.monetate.net/images/src/all_in_one/i5.png)

**CSS3 Selector**

body

**Insert Function**

after

**JavaScript Creative**

<pre>

// Show Coupon Message
document.getElementById('coupon').style.display = 'block'; 

// Reveal the Coupon
function exitCoupon() {
	document.getElementById('sale-coupon').innerHTML = 'Get 20% Off with Coupon Code <div class="coupon-code">Monetate123</div>';
}
	
</pre>

**CSS Style Properties**

Included in the \<head /\> of the stylesheet:

<pre>
#coupon {
	width: 300px;
	border: 1px dashed #252525;
	padding: 10px;
	text-align: center;
	display: none;
}
.coupon-code {
	padding: 20px;
	margin-top: 10px;
	background-color: #66c2ff;
	font-size: 25px;
}
</pre>

Included inline to set the style for your banner \<div\>:


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
