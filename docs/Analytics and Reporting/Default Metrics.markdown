<div id="monetate-product" data-products="interact mayberry">&nbsp;</div>

<div class="info">
<div class="info-title">Email Analytics</div>
<p>This document pertains to the default metrics available for  <strong>Monetate for Personalization</strong> and <strong>Monetate for Testing & Targeting</strong> clients. For default metrics relevant to <strong>Monetate for Email</strong>, please refer to the <a href="/http://support.monetate.com/hc/en-us/articles/201690639">Available Metrics for Email</a> documentation.</p>
</div>

Metrics are measurements used to determine the success of a campaign.

Monetate tracks and reports on a variety of metrics. For self-service **Monetate for Personalization** and **Monetate for Testing & Targeting** clients, the following KPIs work out of the box without any additional integration:

* <a href="#bounce">Bounce Rate</a>
* <a href="#view"> Average Page Views</a>
* <a href="#time">Average Time on Site</a>

For more information about the integration process, please refer to one of the following Self-Integration Guides:

* [Personalization](http://support.monetate.com/hc/en-us/articles/201657776)
* [Testing & Targeting](http://support.monetate.com/hc/en-us/articles/201449905)

###Default Metrics

"Default Metrics" for all of your campaigns can be configured by clicking **Settings** —>**Default Metrics**

![Settings](https://s3.amazonaws.com/elearning.monetate.net/images/src/default_metrics/i1.png)

The table below provides a definition and formula for all of system metrics that Monetate displays by default in any new campaign that you create. Metrics that require additional integration are denoted by a check mark (✓).

<table>
<thead>
<tr><th align="left">Metric</th><th align="left">Definition</th><th align="left">Formula</th><th align ="left">Requires Integration</tr>
</thead>
<tbody>

<tr>
<td align="left"><a name = "view"><strong>Bounce Rate</strong></a></td>
<td align="left">The percentage of visitors who view only one page in the session and then leave</td>
<td align="left">Sessions with Only One View / Total Sessions</td>
<td></td>
</tr>

<tr>
<td align="left"><a name = "view"><strong>Average Page Views</strong></a></td>
<td align="left">The average number of pages that visitors in the campaign view on the website per session.</td>
<td align="left">Total Page Views / Total Sessions</td>
<td></td>
</tr>

<tr>
<td align="left"><a name = "time"><strong>Average Time on Site</strong></a></td>
<td align="left">The average time spent browsing a site per session.</td>
<td align="left">Total Session Time / Total Sessions</td>
<td></td>
</tr>

<tr>
<td align="left"><strong>Conversion Rate</strong></td>
<td align="left">The percentage of visitors who make a purchase during their session.</td>
<td align="left">Sessions With Purchase / Total Sessions</td>
<td>✓</td>
</tr>
<tr>
<td align="left"><strong>New Customer Acquisition Rate</strong></td>
<td align="left">The percentage of first-time visitors (anyone not currently identified with a <a href="http://support.monetate.com/hc/en-us/articles/201214457-Monetate-ID">Monetate ID</a>) who make a purchase.</td>
<td align="left">New Visitor Sessions with Purchase / Total New Visitor Sessions</td>
<td>✓</td>
</tr>

<tr>
<td align="left"><strong>Add to Cart Rate</strong></td>
<td align="left">The percentage of visitors who view their cart with at least one item in it during their session.</td>
<td align="left">Sessions with Cart Item Viewed / Total Sessions</td>
<td>✓</td>
</tr>

<tr>
<td align="left"><strong>Cart Abandonment Rate</strong></td>
<td align="left">The percentage of visitors who view their cart with at least one item in it during their session, but do not make a purchase.</td>
<td align="left">Sessions with Cart Item Viewed and No Purchase / Total Sessions with Cart Item Viewed</td>
<td>✓</td>
</tr>

<tr>
<td align="left"><strong>Revenue Per Session (RPS)</strong></td>
<td align="left">The average spend per session.</td>
<td align="left">Total Revenue / Total Sessions</td>
<td>✓</td>
</tr>


<tr>
<td align="left"><strong>Average Order Value</strong></td>
<td align="left">The average amount spent on an order.</td>
<td align="left">Total Revenue for Orders / Total Number of Orders</td>
<td>✓</td>
</tr>


</tbody>
</table>

Any of these metrics can be set as the <a data-tooltip-large="">default goal</a>
 for all new campaigns by clicking the radio button next to the metric name in the "Goal" column.

![Goal](https://s3.amazonaws.com/elearning.monetate.net/images/src/default_metrics/i2.png)

You can prevent a metric from displaying in **Campaign Results** for all new campaigns by clicking the remove icon for that metric.

![Goal](https://s3.amazonaws.com/elearning.monetate.net/images/src/default_metrics/i3.png)

<div class="info">
<div class="info-title">Note on Removing Default Metrics</div>
<p>Removing a metric from this list only means the metric will not be displayed by default in the <strong>Campaign Results</strong> for all new campaigns. Monetate still collects data for these metrics and provides data for them in the raw .CSV or HTML files at the bottom of the <strong>Campaign Results</strong> page. If you have removed a system metric from your "Default Metrics" and you would like to track that metric by default for new campaigns, you can add it back using the "Add Metric" button. All system metrics that have been removed will appear at the top of the list. For more information on the .CSV and HMTL formats, please refer to the <a href="/hc/en-us/articles/202322108">Exporting Data</a> documentation.</p>
</div>

The following metrics are not displayed on the "Default Metrics" page, but may become visible  in **Campaign Results** under certain circumstances (for example, once Revenue per session reaches actionable confidence): 

<table>
<thead>
<tr><th align="left">Metric</th><th align="left">Definition</th><th align="left">Formula</th></tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Incremental Revenue</strong></td>
<td align="left">The amount of revenue change that is directly correlated with this <a href="http://support.monetate.com/hc/en-us/articles/201249767-Campaign">campaign</a>.</td>
<td align="left">Experiment Percent &times; Visitors &times; (Experiment Revenue Per Session - Control Revenue Per Session)</td>
</tr>
<tr>
<td align="left"><strong>Projected Yearly Income</strong></td>
<td align="left">The amount of revenue change that is directly correlated with this campaign, projected on an annualized basis.</td>
<td align="left">(Incremental Revenue &times; Annualized Traffic Multiplier) / Experiment Percent</td>
</tr>
</table>

###Custom Metrics

You can also add any metrics that you have created using EventBuilder as default metrics for any new campaigns. For more information about building custom metrics, please refer to the [EventBuilder](http://support.monetate.com/hc/en-us/sections/200355298) section of the Knowledge Base. To add a custom metric to your campaign, click the "Add Metric" button.

![Custom Metric](https://s3.amazonaws.com/elearning.monetate.net/images/src/default_metrics/i4.png)

You can search for metrics by metric name or by any tags that you associated with your metric during the creation process. Click the checkbox next to each metric that you would like to track by default for all new campaigns and then click the "Choose Selected" button.

![Adding Custom Metrics](https://s3.amazonaws.com/elearning.monetate.net/images/src/default_metrics/i5.png)


