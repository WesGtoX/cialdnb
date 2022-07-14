# Technical Overview

- Python and Scrapy were used to create a web crawler.  
- Due to the project requirements, `xpath` was used to perform the general data search:  
> `logo`: a search was carried out for the most common types of files (`.png`, `.jpg`, `.jpeg` and `.svg`), to guarantee the complete link of the image, an `add_logo` method was created to perform the validation in the way that the image is extracted and complete the image link.  
> `phones`: A search was carried out in the entire body of the site, through `Regex`, matching the largest type of recognized phone numbers possible. As it is a list of numbers, and because it is a regex, the text is treated to ensure the correct format. Python's `set()` function was also used to guarantee unique numbers.  
> `website`: was extracted through `response.url`.  
- For a better extraction, the `Items` were used as fields and the `Item Loader` for input and output validation of the data.   
- To generate a json file and save the extracted data, always overwriting the data, a `customexport.py` was created to override the default Scrapy configuration.
