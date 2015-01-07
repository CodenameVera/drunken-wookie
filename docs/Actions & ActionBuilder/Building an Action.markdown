<div id="monetate-product" data-products="interact mayberry">&nbsp;</div>

<a name="top"></a>

<div class="summary">

<div class="summary-title">Is this the doc you're looking for?</div>
<p>In this doc you will find everything you need to know to get started with your first action.</p> 

<p> Want to know who on your team is allowed to build actions? Wondering how the element selector works? Looking for a rundown of different action types? The sections below answer each of these questions and get you well on your way to building your first Monetate action. </p>
</div>

*  [Technical Considerations](#1)
*  [Accessing ActionBuilder](#2)
*  [ActionBuilder Interface](#9)
*  [Using the Element Selector](#5)
*  [Action Types](#3)
*  [Adding Images](#4)
*  [Adding a Countdown Timer](#14)
*  [Adding or Editing HTML](#6)
*  [Adding or Editing CSS](#7)
*  [Adding a Lightbox](#8)
*  [Moving an Element](#10)
*  [Swapping Two Elements](#11)
*  [Hiding an Element](#12)
*  [Showing an Element](#13)

### <a name="1"></a>Technical Considerations

*  In order to use ActionBuilder you'll need to be a site administrator or have "Action Building" privileges. 
*  You can use ActionBuilder with the latest versions of Chrome, Firefox, Safari, and Internet Explorer browsers.

[Back to Top](#top)

### <a name="2"></a>Accessing ActionBuilder

To get started with ActionBuilder, find your "Components" tab in the UI navbar, and then click on “Actions.” Finally, click the “Create <a data-tooltip-large="">Action</a>” button to launch ActionBuilder.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i1.png)

[Back to Top](#top)

### <a name="9"></a>ActionBuilder Interface

With ActionBuilder you can create new actions on
any page of your website.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i2.png)

In the top right corner you will find some helpful icons. Here, you can pin ActionBuilder to the top or bottom of your screen, minimize, or close it entirely. If you need additional help, click the question mark icon to send an email to Monetate Support.

[Back to Top](#top)

### <a name="5"></a>Using Element Selectors

All Monetate actions use element selectors to determine where an action happens, and what site elements an action affects. 

You'll notice that after choosing an action type, when you move across your website a blue selector box will appear around the current element. This box is called the <a data-tooltip-large="">DOM</a>
selector tool.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i6.png)

With the DOM selector tool, you can choose any element or element
container on your site. You can adjust when you want an action to appear in relation to the selected element using the selector drop down. These options include:

* First child of the selected element
* Last child of the selected element
* Before selected element
* After selected element 
* Replace the selected element

If you choose the wrong element don't worry, you can use the undo button to select a different element.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i7.png)

Once you have decided on where you want your action to happen, you can customize it even further using the ActionBuilder tabs. To do this, look under the **Details** tab for the "Element Selector" text box. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i26.png)

Here, you can type a new element selector path to change or alter which site element your action affects. Some examples of valid Element Selector paths include:

*  parentElement \> nextChildElement
*  .className \> .nextClassname
*  \#element*ID*Name \> nextChildElement

You can use the "Select All Elements" toggle to select all elements that match your element selector or only the first one. 

Use the "Poll for Matched Elements" toggle to turn polling on or off. If polling is on, ActionBuilder will continue to check for the selected element even if it does not initially appear on the page. This is a good option if you have certain elements that do not fire right when the page loads. If polling is turned off ActionBuilder will only do one check for the element when your page loads. 

For additional information about the types of selectors supported by ActionBuilder, please refer to the "[Types of CSS Selectors](http://support.monetate.com/hc/en-us/articles/202655236)" documentation. 

[Back to Top](#top)

### <a name="3"></a>Action Types

All actions fall into one of three categories: Insert actions, Edit actions,
and Hide/Show actions. 

Insert actions let you add the following elements to your site:

* Image
* HTML
* JavaScript
* CSS
* Background Image
* Lightbox
* Countdown Timer

Edit actions let you edit the following site elements: 

* Image
* HTML
* Move (a current site element)
* Swap (two current site elements)

Hide/Show actions allow you to hide a site element your already have, or show a site element you have hidden. 

The sections below will tell you more about how to use each action type. 

[Back to Top](#top)

### <a name="4"></a>Inserting or Editing Images

There are three ways to add an image in ActionBuilder: you can choose an existing image, generate a placeholder image, or upload a new image.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i3.png)

If you pick “Choose existing image,” [ContentManager](http://support.monetate.com/hc/en-us/articles/202505308) will launch.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i4.png)

If you pick “Generate image,” a window will open that asks for the
height and width (in pixels) of your placeholder image. Later on, you can replace your placeholder image with the image you want to use for your action.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i5.png)

If you pick “Upload image,” a window will open that allows you to browse your computer for the image that you want to use.

Once you choose an image, you can use the element selector to pick the where you want your action to happen. 

<div class="info">
<div class="info-title"> Responsive Clickzones </div>
<p> All clickzones on responsive image actions are also responsive. This means that if your image is designed to scale to the size of the site visitor’s browser window, clickzones contained within that image will also scale without any additional work from you. Pretty neat, huh?</p>
</div>

[Back to Top](#top)

### <a name="14"></a> Inserting a Countdown Timer

With ActionBuilder you can create and insert a countdown timer anywhere on your site. To do this, click **Insert** -—> **Countdown Timer**.

Start buidling your countdown timer by picking an image to use as your background. This works just like the insert image option by allowing you to choose an existing image, generate a new image, or upload an image from your computer. 

Once you have picked an image, use the element selector to choose where you want your countdown timer to appear. All of the other options for how your countdown timer works can be set up in the "Details" tab. For more information, please refer to the [Completing an Action](http://support.monetate.com/hc/en-us/articles/202200978) documentation. 

### <a name="6"></a>Inserting or Editing HTML

ActionBuilder lets you insert or
edit <a data-tooltip-large="">HTML</a> on
your site, without having to do any hardcoding (unless you want to.) There are two ways to do this:

*  You should choose “Insert HTML” if you want to include additional HTML on your
    site.
*  You should choose “Edit HTML” if you want to replace or modify existing HTML on your site.

Just like placing an image, you can select the placement of your HTML using the selector tool. Once you have determined where you want your HTML to go, you can edit your HTML using the HTML editor tab.

There are two views for the HTML editor. 

The HTML WYSIWYG view gives you:

* Standard formatting options 
* Linking capabilities 
* Special character insertions 
* And more, without having to under stand any code. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i8.png)

The “Source” editor allows you to edit plain HTML. You can switch to the “Source” view by clicking the “Source” button. If you need to expand the viewable area of your HTML, click the triangle in the bottom right corner of the window.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i9.png)

[Back to Top](#top)

### <a name="7"></a>Inserting or Editing CSS

With ActionBuilder you can add your own CSS into a textbox. Anything you add here will be appended to the current stylesheet for your site. For this particular action, you will need to have some knowledge of code and how CSS is written. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i10.png)

[Back to Top](#top)

### <a name="8"></a>Inserting a Lightbox

ActionBuilder lets you add a lightbox to one or many pages of
your site with "Lightbox" actions. 

To create a lightbox start by choosing an image. After you choose an image, the lightbox specific options will show up in the “Details” tab.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i13.png)

**Lightbox Options**

The table below explains each available lightbox option and what it does. For more
information on lightboxes, please refer to the
"[Lightboxes](http://support.monetate.com/hc/en-us/articles/201788687)"
and "[Lightboxes: Common
Questions](http://support.monetate.com/hc/en-us/articles/201788707)"
docs.

<table style="width: 600px;" border="1">
<tbody>
<tr>
<th>
Option
</th>
<th>
Description
</th>
</tr>
<tr>
<td>
<a href="http://support.monetate.com/hc/en-us/articles/201788687-Lightboxes#3">Lightbox ID</a></li>
</td>
<td>
The ID determines the grouping of the lightbox with lightboxes you have created in the past. All IDs must be a number from 0-31. If you want to group the display frequency of this lightbox with other lightboxes, set your lightbox ID to the same one that is used by those lightboxes. Otherwise, make sure the ID for this lightbox is unique.
</td>
</tr>
<tr>
<td>
<a href="http://support.monetate.com/hc/en-us/articles/201788687-Lightboxes#4">Display
Frequency</a></li>
</td>
<td>
Display frequency determines how often a visitor sees a lightbox. Your options include:
"Once per user," "Once per user per session," and "Every page for all
users."
</td>
</tr>
<tr>
<td>
Lightbox Container Class
</td>
<td>
If your stylesheet contains lightbox class information, you can
reference that here. This will make it so that your lightbox inherits the same styling, and therefore looks like any other lightboxes on your site. 
</td><strikes</strike>
</tr>
</tbody>
</table>
[Back to Top](#top)

### <a name="10"></a>Moving an Element

The "Move" action allows you to move a current element on your site to a new place. To do this, select "Edit" --> "Move." 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i29.png)

Next, select the element that you want to move and click the forward button. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i30.png)

Then, select the element whose position you want your first element to move into and then click the forward button. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i31.png)

Back to Top](#top)

### <a name="11"></a>Swapping Two Elements 

The "Swap" action allows you to swap the position of two elements on your site. To do this, select "Edit" --> "Swap."

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i32.png)

Next, select the first element you want to swap and then click the forward button. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i33.png)

Then, select the second element you want to swap and then click the forward button. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i34.png)

[Back to Top](#top)
### <a name="12"></a>Hiding an Element 

The "Hide" action allows you to hide a preexisting element on your site. To do this Select "Hide/Show" --> "Hide Element."

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i35.png)

Next, use the element selector to highlight which site element you want to hide.

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i36.png)

When you click on the element, it will be hidden. 

![ActionBuilder](https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i37.png)

[Back to Top](#top)
### <a name="12"></a>Showing an Element 

The "Show" action allows you to show an element on your site that is currently hidden based on your site's code. For example, if you have discounted shipping rates that are normally hidden, you can show them in an upcoming Monetate campaign. 

[Back to Top](#top)
<hr />
<h2>Frequently Asked Questions&nbsp;</h2>
<h3 class="faq">What is the difference between Monetate-created actions and client-created actions?</h3>
<h3 class="faq">What are your Quality Assurance (QA) standards and processes for Actions?</h3>
<h3 class="faq">How do I load external JavaScript files into an ActionBuilder Javascript action?</h3>
<h3 class="faq">How do I change the URL of a link on my page using ActionBuilder?</h3>
<h3 class="faq">What is the difference between using an "Insert" action that replaces an element versus an "Edit" action?</h3>
<h3 class="faq">Can I upload a .gif image for use in Monetate campaigns?</h3>
<hr />
<p><a style="background-color: #ffffff;" href="/hc/en-us/sections/200334758-Actions-ActionBuilder">Return to Category: Actions and ActionBuilder</a></p>
