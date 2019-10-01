# Url-Shortener
1. I have created this project to create shorter url from original url.
2. I had two approaches for project.One is with database and another is simple view-template no database.
   For the first one ,you need to have database where will store both urls i.e. short as well original one.When user enters original url with the use of random library it will create random code for same url and will store it into database.
   When user clicks on short url,it will direct with original with the use of data that is stored into database against short
   one.
   Second approach that I have used is similar to first one except for database,I am not storing any data into database,rather
   whenever user submit original url i create random code or short url and pass both urls to html in anchor tag .

3.To deploy this,clone into your system.create python virtual environment,with the help of requirements.txt file install all the packages .
