.. raw:: html

   <div id="monetate-product" data-products="interact mayberry">
==============================
Building An Action
==============================

Technical Considerations
========================

-  In order to use ActionBuilder you'll need to be a site administrator
   or have "Action Building" privileges.
-  You can use ActionBuilder with the latest versions of Chrome,
   Firefox, Safari, and Internet Explorer browsers.

.. raw:: html

   <hr>

Accessing ActionBuilder
=======================

To get started with ActionBuilder, find your "Components" tab in the UI
navbar, and then click on “Actions.” Finally, click the “Create Action”
button to launch ActionBuilder.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i1.png
   :alt: ActionBuilder

   ActionBuilder

.. raw:: html

   <hr>

ActionBuilder Interface
=======================

With ActionBuilder you can create new actions on any page of your
website.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i2.png
   :alt: ActionBuilder

   ActionBuilder

In the top right corner you will find some helpful icons. Here, you can
pin ActionBuilder to the top or bottom of your screen, minimize, or
close it entirely. If you need additional help, click the question mark
icon to send an email to Monetate Support.

.. raw:: html

   <hr>

Using Element Selectors
=======================

All Monetate actions use element selectors to determine where an action
happens, and what site elements an action affects.

You'll notice that after choosing an action type, when you move across
your website a blue selector box will appear around the current element.
This box is called the DOM selector tool.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i6.png
   :alt: ActionBuilder

   ActionBuilder

With the DOM selector tool, you can choose any element or element
container on your site. You can adjust when you want an action to appear
in relation to the selected element using the selector drop down. These
options include:

-  First child of the selected element
-  Last child of the selected element
-  Before selected element
-  After selected element
-  Replace the selected element

If you choose the wrong element don't worry, you can use the undo button
to select a different element.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i7.png
   :alt: ActionBuilder

   ActionBuilder

Once you have decided on where you want your action to happen, you can
customize it even further using the ActionBuilder tabs. To do this, look
under the **Details** tab for the "Element Selector" text box.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i26.png
   :alt: ActionBuilder

   ActionBuilder

Here, you can type a new element selector path to change or alter which
site element your action affects. Some examples of valid Element
Selector paths include:

-  parentElement > nextChildElement
-  .className > .nextClassname
-  #element\ *ID*\ Name > nextChildElement

You can use the "Select All Elements" toggle to select all elements that
match your element selector or only the first one.

Use the "Poll for Matched Elements" toggle to turn polling on or off. If
polling is on, ActionBuilder will continue to check for the selected
element even if it does not initially appear on the page. This is a good
option if you have certain elements that do not fire right when the page
loads. If polling is turned off ActionBuilder will only do one check for
the element when your page loads.

For additional information about the types of selectors supported by
ActionBuilder, please refer to the "`Types of CSS
Selectors <http://support.monetate.com/hc/en-us/articles/202655236>`__\ "
documentation.

.. raw:: html

   <hr>

Action Types
============

All actions fall into one of three categories: Insert actions, Edit
actions, and Hide/Show actions.

Insert actions let you add the following elements to your site:

-  Image
-  HTML
-  JavaScript
-  CSS
-  Background Image
-  Lightbox
-  Countdown Timer

Edit actions let you edit the following site elements:

-  Image
-  HTML
-  Move (a current site element)
-  Swap (two current site elements)

Hide/Show actions allow you to hide a site element your already have, or
show a site element you have hidden.

The sections below will tell you more about how to use each action type.

.. raw:: html

   <hr>

Inserting or Editing Images
===========================

There are three ways to add an image in ActionBuilder: you can choose an
existing image, generate a placeholder image, or upload a new image.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i3.png
   :alt: ActionBuilder

   ActionBuilder

If you pick “Choose existing image,”
`ContentManager <http://support.monetate.com/hc/en-us/articles/202505308>`__
will launch.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i4.png
   :alt: ActionBuilder

   ActionBuilder

If you pick “Generate image,” a window will open that asks for the
height and width (in pixels) of your placeholder image. Later on, you
can replace your placeholder image with the image you want to use for
your action.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i5.png
   :alt: ActionBuilder

   ActionBuilder

If you pick “Upload image,” a window will open that allows you to browse
your computer for the image that you want to use.

Once you choose an image, you can use the element selector to pick the
where you want your action to happen.

.. raw:: html

   <div class="info">

.. raw:: html

   <div class="info-title">

Responsive Clickzones

.. raw:: html

   </div>

.. raw:: html

   <p>

All clickzones on responsive image actions are also responsive. This
means that if your image is designed to scale to the size of the site
visitor’s browser window, clickzones contained within that image will
also scale without any additional work from you. Pretty neat, huh?

.. raw:: html

   </p>

.. raw:: html

   </div>

.. raw:: html

   <hr>

Inserting a Countdown Timer
===========================

With ActionBuilder you can create and insert a countdown timer anywhere
on your site. To do this, click **Insert** -—> **Countdown Timer**.

Start buidling your countdown timer by picking an image to use as your
background. This works just like the insert image option by allowing you
to choose an existing image, generate a new image, or upload an image
from your computer.

Once you have picked an image, use the element selector to choose where
you want your countdown timer to appear. All of the other options for
how your countdown timer works can be set up in the "Details" tab. For
more information, please refer to the `Completing an
Action <http://support.monetate.com/hc/en-us/articles/202200978>`__
documentation.

Inserting or Editing HTML
=========================

ActionBuilder lets you insert or edit HTML on your site, without having
to do any hardcoding (unless you want to.) There are two ways to do
this:

-  You should choose “Insert HTML” if you want to include additional
   HTML on your site.
-  You should choose “Edit HTML” if you want to replace or modify
   existing HTML on your site.

Just like placing an image, you can select the placement of your HTML
using the selector tool. Once you have determined where you want your
HTML to go, you can edit your HTML using the HTML editor tab.

There are two views for the HTML editor.

The HTML WYSIWYG view gives you:

-  Standard formatting options
-  Linking capabilities
-  Special character insertions
-  And more, without having to under stand any code.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i8.png
   :alt: ActionBuilder

   ActionBuilder

The “Source” editor allows you to edit plain HTML. You can switch to the
“Source” view by clicking the “Source” button. If you need to expand the
viewable area of your HTML, click the triangle in the bottom right
corner of the window.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i9.png
   :alt: ActionBuilder

   ActionBuilder

.. raw:: html

   <hr>

Inserting or Editing CSS
========================

With ActionBuilder you can add your own CSS into a textbox. Anything you
add here will be appended to the current stylesheet for your site. For
this particular action, you will need to have some knowledge of code and
how CSS is written.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i10.png
   :alt: ActionBuilder

   ActionBuilder

.. raw:: html

   <hr>

Inserting a Lightbox
====================

ActionBuilder lets you add a lightbox to one or many pages of your site
with "Lightbox" actions.

To create a lightbox start by choosing an image. After you choose an
image, the lightbox specific options will show up in the “Details” tab.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i13.png
   :alt: ActionBuilder

   ActionBuilder

**Lightbox Options**

The table below explains each available lightbox option and what it
does. For more information on lightboxes, please refer to the
"`Lightboxes <http://support.monetate.com/hc/en-us/articles/201788687>`__\ "
and "`Lightboxes: Common
Questions <http://support.monetate.com/hc/en-us/articles/201788707>`__\ "
docs.

.. raw:: html

   <table style="width: 600px;" border="1">

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

Option

.. raw:: html

   </th>

.. raw:: html

   <th>

Description

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Lightbox ID

.. raw:: html

   </li>

.. raw:: html

   </td>

.. raw:: html

   <td>

The ID determines the grouping of the lightbox with lightboxes you have
created in the past. All IDs must be a number from 0-31. If you want to
group the display frequency of this lightbox with other lightboxes, set
your lightbox ID to the same one that is used by those lightboxes.
Otherwise, make sure the ID for this lightbox is unique.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Display Frequency

.. raw:: html

   </li>

.. raw:: html

   </td>

.. raw:: html

   <td>

Display frequency determines how often a visitor sees a lightbox. Your
options include: "Once per user," "Once per user per session," and
"Every page for all users."

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Lightbox Container Class

.. raw:: html

   </td>

.. raw:: html

   <td>

If your stylesheet contains lightbox class information, you can
reference that here. This will make it so that your lightbox inherits
the same styling, and therefore looks like any other lightboxes on your
site.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

.. raw:: html

   <hr>

Moving an Element
=================

The "Move" action allows you to move a current element on your site to a
new place. To do this, select "Edit" --> "Move."

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i29.png
   :alt: ActionBuilder

   ActionBuilder

Next, select the element that you want to move and click the forward
button.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i30.png
   :alt: ActionBuilder

   ActionBuilder

Then, select the element whose position you want your first element to
move into and then click the forward button.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i31.png
   :alt: ActionBuilder

   ActionBuilder

.. raw:: html

   <hr>

Swapping Two Elements
=====================

The "Swap" action allows you to swap the position of two elements on
your site. To do this, select "Edit" --> "Swap."

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i32.png
   :alt: ActionBuilder

   ActionBuilder

Next, select the first element you want to swap and then click the
forward button.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i33.png
   :alt: ActionBuilder

   ActionBuilder

Then, select the second element you want to swap and then click the
forward button.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i34.png
   :alt: ActionBuilder

   ActionBuilder

.. raw:: html

   <hr>

Hiding an Element
=================

The "Hide" action allows you to hide a preexisting element on your site.
To do this Select "Hide/Show" --> "Hide Element."

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i35.png
   :alt: ActionBuilder

   ActionBuilder

Next, use the element selector to highlight which site element you want
to hide.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i36.png
   :alt: ActionBuilder

   ActionBuilder

When you click on the element, it will be hidden.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_builder/i37.png
   :alt: ActionBuilder

   ActionBuilder

.. raw:: html

   <hr>

Showing an Element
==================

The "Show" action allows you to show an element on your site that is
currently hidden based on your site's code. For example, if you have
discounted shipping rates that are normally hidden, you can show them in
an upcoming Monetate campaign.

.. raw:: html

   <hr>
