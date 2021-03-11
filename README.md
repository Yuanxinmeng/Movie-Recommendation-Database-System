# Movie-Recommendation-Database-System
The project is about constructing a movie recommendation database system

A.Background
Plenty of movies on the Internet, and many people prefer to see movies online rather than in the cinema. When there are too much files, but people do not have certain movie that want to see. They can refer the list of grade of movies. Meanwhile, many people have the habit to grade the movies, so these grade can help people to see the popular rate and the quality of the movies. In this way, people can according to these grade datas to choose the movie to watch.  The high grade will be recommended on the first, then ranks down by the grade.

B. Initial process
The design about movie recommendation database system is organized in two secitons. The first is database design. Mongodb is our first choies to store dataset, then the usage of dataset is about having and parsing movies and rating data into Spark RDDs. Python and Flask are used to constructed a web application. The second concerns the construction and usage of the recommender and its continuous use of our collaborative filtering framework. There is a backup option, using AWS service to build a Statistical Recommendation Module,like a factorization machines on Amazon SageMaker.

C. Resources 
1. Yi, N., Li, C., Feng, X., & Shi, M. (2017, November). Design and implementation of movie recommender system based on graph database. In 2017 14th Web Information Systems and Applications Conference (WISA) (pp. 132-135). Retrieved from https://www.semanticscholar.org/paper/Design-and-Implementation-of-Movie-Recommender-on-Yi-Li/746a81aa26d3ebfb81acfd6af958d6a21603cd21
2. Yongfeng Zhang, X. Chen, Qingyao Ai, Liu Yang, W. Croft (2018). Towards Conversational Search and Recommendation: System Ask, User Respond. Retrieved from https://www.semanticscholar.org/paper/Towards-Conversational-Search-and-Recommendation%3A-Zhang-Chen/3ae5bef6b0c8317603a2deab2527383580904fd8
3. 12 top MongoDB project ideas &amp; topics for beginners. (2020, July 17). Retrieved February 12, 2021, from https://www.upgrad.com/blog/mongodb-project-ideas-topics-for-beginners/
