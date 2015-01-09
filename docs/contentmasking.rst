.. raw:: html

   <div id="monetate-product" data-products="interact mayberry">

 

.. raw:: html

   </div>
   
==============================
Content Masking
==============================   

Why Use Masking?
================

Content Masking is a method used to hide an element or containing
element on a page until after Monetate’s actions complete. You can use
Content Masking to hide elements or containing elements to provide a
consistent experience for all site visitors.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i1.png
   :alt: ActionBuilder Mask Tab

   ActionBuilder Mask Tab

.. raw:: html

   <hr>

When to Use Masking
====================

There are a few instances where it makes sense to use content masking:

-  If you are currently using the `synchronous
   tag <http://support.monetate.com/hc/en-us/articles/201255843-The-Monetate-Tag#2>`__
   to run Monetate on your site, you should use Content Masking on all
   hide/show actions to create an optimized site experience for your
   customers.
-  Depending on the specifics of your site, it may be beneficial to use
   content masking with hide/show actions when using the `asynchronous
   tag <http://support.monetate.com/hc/en-us/articles/201255843-The-Monetate-Tag#2>`__
   as well.
-  In addition, if you are using a combination of actions that includes
   hiding content in one area and then inserting content in another, it
   is important to make sure you have masks applied to all areas
   involved.

**Example:**

If you are using an action that replaces an element in the main
navigation bar, it makes sense to mask the entire navigation bar rather
than just the part where the action takes place so that all navigation
items appear to load at the same time.

.. raw:: html

   <hr>

How Masking Works
==================

Once you have enabled content masking in the **Masks** tab, the element
selector will include the specified details for the element you are
looking to mask. The element selector does not allow CSS3 selectors,
sizzle selectors (such as #menu > li.nav:eq(2) ), or pseudo selectors
(such as #menu > li.nav:nth-child(3)). If you use one of these, a
warning will show under your selector. This warning indicates that you
must alter the text in your CSS selector before applying a mask.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i2.png
   :alt: ActionBuilder CSS Selector

   ActionBuilder CSS Selector

If you are not comfortable editing the text yourself or if you have
further questions about what selectors to use, please contact Monetate
support.

.. raw:: html

   <hr>

Applying Masks
==============

Monetate applies masks as soon as the tag fires and before anything is
known about the page content or the visitor. Consequently, you cannot
use `**Who**
targets <http://support.monetate.com/hc/en-us/articles/201250106-Understanding-Who-Targeting>`__
and `action
conditions <http://support.monetate.com/hc/en-us/articles/201831118-Using-Action-Conditions>`__
to determine when to apply masks. Instead, use URL/path matching. Keep
in mind, you should limit content masking to pages where actions occur.
To enable content masking, navigate to the “Mask” tab and check the box
labeled “Enable Content Masking.”

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i3.png
   :alt: ActionBuilder Mask Tab

   ActionBuilder Mask Tab

**Note**: After you have created your mask, you may experience an
initial delay before your mask is visible on your site. If you do not
pause your campaign first, this delay may increase. This will only occur
for newly created masks.

.. raw:: html

   <hr>

URL Diagram
===========

To understand where to instruct ActionBuilder to apply a mask, you must
first understand the URL or path that determines when to apply a mask.
Below is a diagram of a URL with parameters to illustrate each section
that determines when to apply a mask.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i4.png
   :alt: URL Diagram

   URL Diagram

.. raw:: html

   <hr>

Mask Examples
=============

The table below shows five examples of masking rules applied at
different times based on their paths and URLs.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i5.png
   :alt: ActionBuilder Masking Rules Table

   ActionBuilder Masking Rules Table

.. raw:: html

   <hr>

Viewing Masks
=============

You can add an action to a campaign once a mask is set. On the **Actions
Page**, you will be able to see if an action has a mask by looking for a
mask icon. If an action has a mask icon, it currently has a mask
applied. If there is no mask icon present, it does not have a mask.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i6.png
   :alt: Action Masks Icon

   Action Masks Icon

After 30 minutes, you can view the mask for your action. You must view
the mask within the campaign to assure that the mask is functional. The
default preview functionality will not display the mask.

.. raw:: html

   <hr>
