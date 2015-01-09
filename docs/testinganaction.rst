.. raw:: html

   <div id="monetate-product" data-products="interact mayberry">

 

.. raw:: html

   </div>
==============================
Testing An Action
==============================

Background
==========

After you build an action in ActionBuilder, it is important to test it
in the context of a campaign before you make it live on your site. This
document outlines several guidelines to begin the testing process.

**Note:** *Monetate does not provide QA testing for client-built
actions. It is important that someone on your team tests any actions
that you create.*

.. raw:: html

   <hr>

Use Action Conditions
=====================

While Monetate does not consider action conditions as a method for
testing, they can help to ensure that your action performs as you
intended when you test it. Action conditions are rules applied at either
the action or campaign level that determine when and where your action
will run. For example, if your action is meant to run only on product
pages, apply an action to "show only when page type = product." The
image below demonstrates how to apply the condition at the Action level.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_testing/i1.png
   :alt: Testing Actions

   Testing Actions

Keep in mind, action conditions that rely on page type require
integration. Once you have integrated, you can use the Inspector to
determine the reported page for the pages on your own website.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_testing/i2.png
   :alt: Testing Actions

   Testing Actions

For more information about the integration process, please refer to the
`Understanding the Monetate Integration Process for Premier
Service <http://support.monetate.com/hc/en-us/articles/201786113>`__ or
`Understanding the Monetate Integration Process for Self
Service <http://support.monetate.com/hc/en-us/articles/201949483>`__
guides.

.. raw:: html

   <hr>

Test and Compare Pages With and Without An Action Running
=========================================================

One way to test your action and how it interacts with other page
elements is to compare the appearance of pages with and without an
action running. To do this, open the page on which the action will run.
If you have the action set to run on multiple page types (such as home,
product, and cart pages) open a browser window for each page type.

Now, open those same pages with the action currently running on each.
You can do this by creating a campaign that uses the action, and
clicking the "Preview" button.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_testing/i3.png
   :alt: Testing Actions

   Testing Actions

Compare the two versions of the page to make sure everything looks as
you intended. If you quickly toggle back and forth between the two
versions of the page you can establish if there are any discrepancies.

.. figure:: https://s3.amazonaws.com/elearning.monetate.net/images/src/action_testing/i4.png
   :alt: Testing Actions

   Testing Actions

.. raw:: html

   <hr>

Resize Windows
===============

Make sure to test your action in browser windows of different sizes. Try
resizing the window with your cursor. Zoom in and then zoom back out
again.

.. raw:: html

   <hr>

Test Across Different Browsers
===============================

Because different web browsers tend to differ in how they render content
, it is recommended that you test your new action using different
browser types and versions. Test your action in all major browsers
including Chrome, Firefox, Safari, and Internet Explorer. If possible,
test your action in multiple versions of each browser and not just the
newest version or the version that you have on your own computer.

.. raw:: html

   <hr>

Test Functionality of Site Elements
====================================

Even if your action does not directly interact with individual elements
on your site, it can still affect their functionality. To avoid any
unforeseen interactions, be sure to test all elements of your site that
exist on the same page as the action while the action is running. These
can include:

-  Drop-down menus
-  Tooltips or other hover prompted messaging
-  Add-to-cart buttons
-  Ads or other links to external sites
-  Thumbnail sorting features

.. raw:: html

   <hr>

Test Pages When Logged in and Logged Out
=========================================

If your site includes the ability to log in to an account, test the site
with the action running while logged in and logged out. Compare the
pages when you are logged in to those when you are logged out to ensure
everything appears as intended, and that your action functions in both
environments.

.. raw:: html

   <hr>

Test Clickzones
================

If you added clickzones to an image in your action, test to make sure
that they are clickable and that they redirect to the appropriate
destination URL. Click inside and outside of your clickzone and make
sure that it behaves as intended in both instances.

.. raw:: html

   <hr>

Final Note
===========

If you have any issues with how your actions display at any point during
the testing process or if you see an older version of your action, clear
your browser cache and click "Refresh."

If you continue to have trouble, please contact Monetate support for
further assistance.
