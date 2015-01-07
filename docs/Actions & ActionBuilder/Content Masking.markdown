<div id="monetate-product" data-products="interact mayberry">&nbsp;</div>

<a name="top"></a>

*  [Why Masking is Used](#7)
*  [When to Use Masking](#1)
*  [How Masking Works](#2)
*  [When Masks are Applied](#3)
*  [URL Diagram](#4)
*  [Mask Examples](#5)
*  [Viewing Masks](#6)

### <a name="7"></a>Why Use Masking?

Content Masking is a method used to hide an element or containing element on
a page until after Monetate’s <a data-tooltip-large="">action</a>s complete. You can use Content Masking to hide
elements or containing elements to provide a consistent experience for
all site visitors.

![ActionBuilder Mask
Tab](https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i1.png)

### <a name="1"></a>When to Use Masking

There are a few instances where it makes sense to use content
masking:

*  If you are currently using the [synchronous
    tag](http://support.monetate.com/hc/en-us/articles/201255843-The-Monetate-Tag#2)
    to run Monetate on your site, you should use Content
    Masking on all hide/show actions to create an optimized site
    experience for your customers.
*  Depending on the specifics of your site, it may be beneficial to use
    content masking with hide/show
    <a data-tooltip-large="">actions</a>
    when using the [asynchronous
    tag](http://support.monetate.com/hc/en-us/articles/201255843-The-Monetate-Tag#2)
    as well.
*  In addition, if you are using a combination of actions that includes
    hiding content in one area and then inserting content in another, it
    is important to make sure you have masks applied to all areas involved.

**Example:** 

If you are using an action that replaces an element in the
main navigation bar, it makes sense to mask the entire navigation bar
rather than just the part where the action takes place so that all
navigation items appear to load at the same time.

[Back to Top](#top)

### <a name="2"></a>How Masking Works

Once you have enabled content masking in the **Masks** tab, the element
selector will include the specified details for the
element you are looking to mask. The element selector does not allow
CSS3 selectors, sizzle selectors (such as \#menu \> li.nav:eq(2) ), or
pseudo selectors (such as \#menu \> li.nav:nth-child(3)). If you use one of these, a warning will show under your selector. This warning
indicates that you must alter the text in your
<a data-tooltip-large="">CSS</a>
selector before applying a mask.

![ActionBuilder CSS
Selector](https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i2.png)

If you are not comfortable editing the text yourself or if you have
further questions about what selectors to use, please contact
Monetate support.

[Back to Top](#top)

### <a name="3"></a>Applying Masks 

Monetate applies masks as soon as the tag fires and before anything is
known about the page content or the visitor. Consequently, you cannot use [**Who**
targets](http://support.monetate.com/hc/en-us/articles/201250106-Understanding-Who-Targeting)
and [action
conditions](http://support.monetate.com/hc/en-us/articles/201831118-Using-Action-Conditions) to determine when to apply masks. Instead, use
URL/path matching. Keep in mind, you should limit content masking to pages where actions occur. To enable content masking,
navigate to the “Mask” tab and check the box labeled “Enable Content
Masking.”

![ActionBuilder Mask
Tab](https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i3.png)

**Note**: After you have created your mask, you may experience an initial delay before your mask is visible on your site. If you do not pause your campaign first, this delay may increase. This will only occur for newly created masks. 

[Back to Top](#top)

### <a name="4"></a>URL Diagram

To understand where to instruct ActionBuilder to apply a mask, you must
first understand the URL or path that determines when to apply a mask.
Below is a diagram of a URL with parameters to illustrate each section that determines when to apply a mask.

![URL
Diagram](https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i4.png)

[Back to Top](#top)

### <a name="5"></a>Mask Examples

The table below shows five examples of masking rules applied at different times based on their paths and
URLs.

![ActionBuilder Masking Rules
Table](https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i5.png)

[Back to Top](#top)

### <a name="6"></a>Viewing Masks

You can add an action to a  <a data-tooltip-large="">campaign</a> once a mask is set.
On the **Actions Page**, you will be able to see if an action has a mask by
looking for a mask icon. If an action has a mask
icon, it currently has a mask applied. If there is no mask icon present, it does not have a mask.

![Action Masks
Icon](https://s3.amazonaws.com/elearning.monetate.net/images/src/content_masking/i6.png)

After 30 minutes, you can view the mask for your action.  You must view the mask within the campaign to assure that the mask is functional.
The default preview functionality will not display the mask.

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
