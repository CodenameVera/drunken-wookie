<div id="monetate-product" data-products="interact mayberry">&nbsp;</div>

#Types of CSS Selectors

**Note:** *Element Selectors in ActionBuilder support both
[CSS3](http://www.w3.org/TR/css3-selectors/#selectors) and
[Sizzle](https://github.com/jquery/sizzle/wiki/Sizzle-Documentation#selectors)
selector syntax.*

<table>
  <tr>
    <th style="width:22%">Selector</th>
    <th style="width:17%">Example</th>
    <th style="width:56%">Example description</th>
    <th>CSS</th>
  </tr>
	<tr>
    <td>.<i>class</i></td>
    <td class="notranslate">.intro</td>
    <td>Selects all elements containing the class=&quot;intro&quot;</td>
    <td>1</td>
  </tr>
	<tr>
    <td>#<i>id</i></td>
    <td class="notranslate">#firstname</td>
    <td>Selects the element containing the id=&quot;firstname&quot;</td>
    <td>1</td>
  </tr>  <tr>
    <td>*</td>
    <td class="code notranslate">*</td>
    <td>Selects all elements</td>
    <td>2</td>
  </tr>
  <tr>
    <td><i>element</i></td>
    <td class="notranslate">p</td>
    <td>Selects all paragraph elements</td>
    <td>1</td>
  </tr>
  <tr>
    <td><i>element,element</i></td>
    <td class="notranslate">div, p</td>
    <td>Selects all div elements and all paragraph elements</td>
    <td>1</td>
  </tr>
  <tr>
    <td><i>element</i> <i>element</i></td>
    <td class="notranslate">div p</td>
    <td>Selects all paragraph elements inside div elements</td>
    <td>1</td>
  </tr>
  <tr>
    <td><i>element</i>&gt;<i>element</i></td>
    <td class="notranslate">div &gt; p</td>
    <td>Selects all paragraph elements where the parent is a div element</td>
    <td>2</td>
  </tr>
  <tr>
    <td><i>element</i>+<i>element</i></td>
    <td class="notranslate">div + p</td>
    <td>Selects all paragraph elements that are placed immediately after div elements</td>
    <td>2</td>
  </tr>
	<tr>
    <td><i>element1</i>~<i>element2</i></td>
    <td>p ~ ul</td>
    <td>Selects every unordered list element that are preceded by a paragraph element</td>
    <td>3</td>
  </tr>
	<tr>
    <td>[<i>attribute</i>]</td>
    <td class="notranslate">a[target]</td>
    <td>Selects hyperlink elements with a target attribute</td>
    <td>2</td>
  </tr>
	<tr>
    <td>[<i>attribute</i>=<i>value</i>]</td>
    <td class="notranslate">a[target =_blank]</td>
    <td>Selects hyperlink elements with target=&quot;_blank&quot;</td>
    <td>2</td>
  </tr>
	<tr>
    <td>[<i>attribute</i>~=<i>value</i>]</td>
    <td class="notranslate">a[title ~= flower]</td>
    <td>Selects hyperlink elements with a title attribute containing the word &quot;flower&quot;</td>
    <td>2</td>
  </tr>
	
	<tr>
    <td>[<i>attribute</i>*=<i>value</i>]</td>
    <td>a[src *= &quot;monetate&quot;]</td>
    <td>Selects hyperlink elements whose src attribute value contains the substring 
	&quot;monetate&quot;</td>
    <td>3</td>
  </tr>

  <tr>
    <td>p:first - child</td>
    <td class="notranslate">p:first - child</td>
    <td>Selects every paragraph element that is the first child of its parent</td>
    <td>2</td>
  </tr>
	
	<tr>
    <td>p:last - child</td>
    <td>p:last - child</td>
    <td>Selects every paragraph element that is the last child of its parent</td>
    <td>3</td>
  </tr>
	
	<tr>
    <td>:not(<i>selector</i>)</td>
    <td>div:not(p)</td>
    <td>Selects every paragrapgh element in a div that is not a paragraph element</td>
    <td>3</td>
  </tr>

</table>

For a complete list of <a data-tooltip-large="">CSS</a> selectors, please refer to [W3 Schools](http://www.w3schools.com/cssref/css_selectors.asp). For an example of various CSS selectors, please refer to the [Selector Tester](http://www.w3schools.com/cssref/trysel.asp) application on W3 Schools.

**Note**: *Some CSS selectors are not supported by earlier versions of Internet Explorer. For a more in-depth list, please refer to the compatibility chart available on [Quirksmode](http://www.quirksmode.org/css/selectors/).*

<p><hr />
<h2>Frequently Asked Questions&nbsp;</h2>
<h3 class="faq">What is the difference between Monetate-created actions and client-created actions?</h3>
<h3 class="faq">What are your Quality Assurance (QA) standards and processes for Actions?</h3>
<h3 class="faq">How do I load external JavaScript files into an ActionBuilder Javascript action?</h3>
<h3 class="faq">How do I change the URL of a link on my page using ActionBuilder?</h3>
<h3 class="faq">What is the difference between using an "Insert" action that replaces an element versus an "Edit" action?</h3>
<hr />
<p><a style="background-color: #ffffff;" href="/hc/en-us/sections/200334758-Actions-ActionBuilder">Return to Category: Actions and ActionBuilder</a></p></p>
