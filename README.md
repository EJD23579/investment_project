# investment_project


Warren Buffet is an incredibly successful value investor and a household name for many investors. His strategy involves looking over the financial statements of a company to glean information on if the company is likely to succeed in the future, and grow its value. His strategy differs from what a lot of people think investment is, as the approach does not involve frequent trading.

His approach is reminicent of the phrase; 'Keep it simple, stupid!' as he advocates that you should not invest in industries you do not fully understand. As well as this, the idea that by looking at the profits of a company, comparing these figures with other companies in the industry and making decisions based on this seems suprisingly simple.

The complicated part (at least for those of us with limited accounting experience) is attempting to understand what all the terms mean, such as what falls into short term debt and what is long term debt. Of course we can easily search this, but finding this out as well as then trying to follow the rules put down by Mr Buffett can be quite a lot of work to do, for just one company. 

My solution to this, as a semi-financially literate budding programmer, is to automate the process.

By webscraping the financials using the Yfinance API, uploading this to a PostgreSQL database, and then running the individual values through functions based upon Warren Buffetts rules, the program will output a score based upon these rules, which will then be aggregated with other scores based on other rules, to then provide an overall value which will determine if the stock would be one that Warren Buffett would be interested in purchasing ('What would Warren Buffett do?')

This project is also being used to showcase my abilities with Python and PostgreSQL. I will look to add extra functionalities in the future, such as a ranking system between companies in a similar market, a market ranking system based on aggregate scores of companies within said market, as well as potentially some data analytics and deep learning, using Python.

This is not a professional investment analysis tool and is not intended to be used as such, please invest responsibily!
