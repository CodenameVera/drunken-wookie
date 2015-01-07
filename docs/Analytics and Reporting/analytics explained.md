###Interpreting the Analytics Page

The Analytics page for your campaign can be daunting. Having a clear understanding of what Monetate reports and why can help you to make more informed decisions from your campaign results.

![Analytics](https://s3.amazonaws.com/elearning.monetate.net/images/src/analytics_explained/i4.png)

###Observed vs Uncertainty 

One of the most common questions Monetate recieves about the native Analytics is "What do numbers in the lift column?" indicate?

![Analytics](https://s3.amazonaws.com/elearning.monetate.net/images/src/analytics_explained/i1.png)

These numbers represent the "Observed Lift" (larger number) and the "Uncertainty" value (smaller number). Think of these numbers as a way to verify the <a data-tooltip-large="">confidence</a> of your metric. If the absolute value of the "Uncertainty" is smaller than the absolute value of the "Observed Lift," your metric has exceeded confidence for this campaign. 

Monetate displays "Observed Lift" and "Uncertainty" for the following metrics:

* Lift
* Incremental Revenue
* Projected Yearly Revenue

###Revenue Per Session

"Revenue Per Session" is the amount of money your site visitors spend, on average, during a single session on your site. 

![Analytics](https://s3.amazonaws.com/elearning.monetate.net/images/src/analytics_explained/i5.png)

####Equation: 

**Total Revenue** / **Total Sessions**

Where:

**Total Revenue** = The total amount of money brought in through your site for this campaign

**Total Sessions** = The total number of Monetate sessions that have occured on your site

####Example:

If your site visitors account for a total of 20 sessions and the amount purchased during those sessions added up to $1,000, your total revenue per session is $50. 

###Incremental Revenue

Incremental revenue is the amount of revenue change that is directly correlated with your campaign. Incremental Revenue is based on the amount of revenue per session if that metric is significant. 

![Analytics](https://s3.amazonaws.com/elearning.monetate.net/images/src/analytics_explained/i2.png)

####Equation:

**Experiment Percent** * **Visitors** * (**Actual Experiment RPS** - **Actual Control RPS**)

Where:

**Experiment Percent** = The percentage of users in the experiment group for your campaign

**Visitors** = The number of users exposed to this campaign

**Actual Experiment RPS** = The revenue per session for the experiment group in your campaign

**Actual Control RPS** = The revenue per session for the control group in your campaign

####Example:

If your experimental percent is equal to 50% and you had a total of 25,200 visitors participate in the campaign and the visitors who were exposed to the experimental version of the campaign had an average revenue per session that was $3.7 dollars higher than those who were shown the control version of the campaign, your incremental revenue is approximately $46,805. 


###Projected Annual Revenue 

Projected Annual Revenue is based on incremental revenue and projected on an annualized basis. The yearly traffic multiplier is calculated by taking the amount of time in a full year compared to the amount of time that the campaign has run. The multiplier can also be adjusted for seasonality.

![Analytics](https://s3.amazonaws.com/elearning.monetate.net/images/src/analytics_explained/i3.png)
 
####Equation: 

**Incremental Revenue** * **Annualized Traffic Multiplier** / **Experiment Percent** 

Where:

**Incremental Revenue** = Amount of revenue change directly correlated with this campaign

**Annual Traffic Multiplier** = Amount of time campaign has been running compared to amount of time in a full year

**Experiment Percent** = The percentage of users who are put in the experiment group for your campaign

####Example:

If your incremental revenue is $46,805 and your traffic multiplier is 12.65 with a 50% split between the experiment group and the control group, your projected annual revenue is approximately $1,181,272 per year. 
