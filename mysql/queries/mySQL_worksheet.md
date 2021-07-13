Understanding how to write basic SQL queries is extremely important.  Please find someone else in your cohort to work on the following challenges.  Please write down the appropriate SQL query on this worksheet and turn this in (before the end of the day).

![](./Capture.PNG)
1. Basic 4 Queries
For the ERD above, how would you:
1. Get all users whose age is greater than 35?


2. Insert a new user whose first name is ‘Jonathan’ and last name is ‘Smith’?  Have created_at be the current time.


3. Delete all users whose user records were created after August 1st 2010?


4. Update user record (id: 3) so that first_name is ‘Coding’ and last name ‘Dojo’.  Also update it so that the age is set as 7.  Have updated_at automatically update to the current time.

Once you do the four queries above, please check with at least one or two other groups before working on the following assignments.

2. MySQL Countries
1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)



2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)


3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)


4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)


5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)


6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)


7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)


8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)



3. Sakila SQL query assignment
1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.


2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).


3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.

Page 2 -  Your Name: _______________________________


4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.



5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.



6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.



7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, special features, and genre (category).



8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.



4. Lead Gen Business
1. What query would you run to get the total revenue for March of 2012?


2. What query would you run to get total revenue collected from the client with an id of 2?



3. What query would you run to get all the sites that client=10 owns?



4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?


5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?



6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?



7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?



8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.



9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.



10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

