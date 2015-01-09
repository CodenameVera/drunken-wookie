.. raw:: html

   <div id="monetate-product" data-products="interact mayberry">

 

.. raw:: html

   </div>

==============================
Lightboxes
==============================

What are lightboxes?
====================
A lightbox is an image overlay that takes control of the rest of your
site when a user exhibits a certain behavior or arrives on a certain
page type. Lightboxes are also an effective way to direct your visitor’s
attention to a specific site element or image. Monetate offers
lightboxes as prebuilt actions configured using the sentence based
campaign builder.

In the example below, a lightbox alerts a visitor that the items in
their cart are still available to purchase before the holidays.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i1.png
   :alt: Lightbox

   Lightbox

.. raw:: html

   <hr>

Types of Lightboxes
===================

There are four types of lightboxes that can be created with Monetate:

You can create four types of lightboxes with Monetate:

-  **Image:** The standard lightbox that comes included in
   ActionBuilder. An image lightbox can contain CSS) but focuses on an
   image.
-  HTML: A Monetate assisted action customized by the client. Here, a
   lightbox contains html instead of an
   image(http://support.monetate.com/hc/en-us/articles/201586313-Hypertext-Markup-Language-HTML-).
-  **All in One:** A Monetate assisted action customized by the client.
   All in one lightboxes allow for HTML and JavaScript together within a
   lightbox. For more information, please refer to the `All in One
   action
   documentation <http://support.monetate.com/hc/en-us/articles/201525707>`__.
-  **Lightbox On-Click:** An assisted action lightbox that customized by
   the client. On-click lightboxes open on a click of an element instead
   of on a page open. You will need to define the element that, when
   clicked, will launch the lightbox.

.. raw:: html

   <hr>

Lightbox IDs
============

The lightbox ID, which can be any number between zero and 31, determines
the grouping for the lightbox. If you want to group the display
frequency of your lightbox with other Monetate lightboxes, you should
choose an ID that matches those lightboxes. If a user qualifies for more
than one campaign with the same ID, the campaign with the highest
`priority <http://support.monetate.com/hc/en-us/articles/201855363>`__
will show. If you want your lightbox to be independent of any grouping,
make sure the ID for this lightbox is different from all other Monetate
lightboxes.

.. raw:: html

   <hr>

Display frequency
=================

Display frequency determines how often user sees a particular lightbox.
The settings include once per user, once per user per session, and every
page for all users.

**Once per user:** This setting means that a user will only see a
lightbox one time, ever. Use this setting sparingly due to its
implications with the lightbox ID. If you set any lightbox to show only
once per user, then the user will never see that lightbox, along with
any other lightboxes sharing that ID, again.

If you were to use this setting one time with every available lightbox
ID (0-31), and a user qualified to see every lightbox one time, then
they would never see any other lightbox you create, because you have
already used all the IDs.

**Once per user, per session:** This is the most commonly used lightbox
display frequency setting. It means that a user will see a lightbox one
time per lightbox session. For more information on what constitutes a
lightbox session, please refer to the `Lightboxes: Common
Questions <http://support.monetate.com/hc/en-us/articles/201788707-Lightboxes-Common-Questions>`__
documentation.

**Every page for all users:** This display frequency means that a site
visitor who qualifies for the lightbox campaign will see it on every
page if no other guidelines are set. You should set guidlines at the
campaign level for this frequency This display frequency so that site
visitors are not overwhelmed by a lightbox on every page of your site.

**Note:** *When referring to “user” or "site visitor" in Display
Frequency, the Monetate ID determines the user. If the user clears their
cookies, they will be considered a new user and will qualify for the
lightbox once again.*

.. raw:: html

   <hr>

Using Lightboxes in Campaigns
=============================

To add a lightbox to a campaign, click the **What** predicate and then
click "Add Action."

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i4.png
   :alt: Add to Campaign

   Add to Campaign

Select the "Lightboxes" Action Type.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i5.png
   :alt: Add to Campaign

   Add to Campaign

Next, select a lightbox action that is appropriate for your purposes.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i6.png
   :alt: Lightbox Action

   Lightbox Action

You have three options for adding a creative to your Lightbox action:

-  **Choose**: Allows you to select a previously uploaded creative using
   ContentManager
-  **Upload**: Allows you to upload a new creative from your computer
-  **Generate**: Allows you to generate a placeholder image with a
   custom height and width

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i7.png
   :alt: Add Creative

   Add Creative

After you have added your creative, you can add a close link for your
lightbox. Click "Edit" to launch ContentBuilder.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i8.png
   :alt: Add Creative

   Add Creative

In ContentBuilder, click "Add Layer" and then click "Clickzone."

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i9.png
   :alt: Add Creative

   Add Creative

Drag and resize your clickzone on your background image. If you have
added a close button to your creative, drag your clickzone over the
button.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i10.png
   :alt: Clickzone

   Clickzone

Add "#close" to the "URL" textbox in the **Link** panel for your
clickzone.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i11.png
   :alt: Close

   Close

Click "Save" and then click "Close and return" to return to the Campaign
creation screen.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/lightboxes/i12.png
   :alt: Save

   Save
