book_rec1 = { 
    "_id" : 4, 
    "title" : "Flex 3 in Action", 
    "isbn" : "1933988746", 
    "pageCount" : 576, 
    "publishedDate" : { 
        "date" : "2009-02-02T00:00:00.000-0800" 
        }, 
    "thumbnailUrl" : "https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/ahmed.jpg", 
    "longDescription" : "New web applications require engaging user-friendly interfaces   and the cooler, the better. With Flex 3, web developers at any skill level can create high-quality, effective, and interactive Rich Internet Applications (RIAs) quickly and easily. Flex removes the complexity barrier from RIA development by offering sophisticated tools and a straightforward programming language so you can focus on what you want to do instead of how to do it. And now that the major components of Flex are free and open-source, the cost barrier is gone, as well!    Flex 3 in Action is an easy-to-follow, hands-on Flex tutorial. Chock-full of examples, this book goes beyond feature coverage and helps you put Flex to work in real day-to-day tasks. You'll quickly master the Flex API and learn to apply the techniques that make your Flex applications stand out from the crowd.    Interesting themes, styles, and skins  It's in there.  Working with databases  You got it.  Interactive forms and validation  You bet.  Charting techniques to help you visualize data  Bam!  The expert authors of Flex 3 in Action have one goal   to help you get down to business with Flex 3. Fast.    Many Flex books are overwhelming to new users   focusing on the complexities of the language and the super-specialized subjects in the Flex eco-system; Flex 3 in Action filters out the noise and dives into the core topics you need every day. Using numerous easy-to-understand examples, Flex 3 in Action gives you a strong foundation that you can build on as the complexity of your projects increases.", 
    "status" : "PUBLISH", 
    "authors" : [ 
        "Tariq Ahmed with Jon Hirschi", 
        "Faisal Abid" 
        ], 
    "categories" : [ "Internet" ] 
    }

book_rec2 = { 
    "_id" : 6, 
    "title" : "Collective Intelligence in Action", 
    "isbn" : "1933988312", 
    "pageCount" : 425, 
    "publishedDate" : { 
        "date" : "2008-10-01T00:00:00.000-0700" 
        }, 
    "thumbnailUrl" : "https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/alag.jpg", 
    "longDescription" : "There's a great deal of wisdom in a crowd, but how do you listen to a thousand people talking at once  Identifying the wants, needs, and knowledge of internet users can be like listening to a mob.    In the Web 2.0 era, leveraging the collective power of user contributions, interactions, and feedback is the key to market dominance. A new category of powerful programming techniques lets you discover the patterns, inter-relationships, and individual profiles   the collective intelligence   locked in the data people leave behind as they surf websites, post blogs, and interact with other users.    Collective Intelligence in Action is a hands-on guidebook for implementing collective-intelligence concepts using Java. It is the first Java-based book to emphasize the underlying algorithms and technical implementation of vital data gathering and mining techniques like analyzing trends, discovering relationships, and making predictions. It provides a pragmatic approach to personalization by combining content-based analysis with collaborative approaches.    This book is for Java developers implementing collective intelligence in real, high-use applications. Following a running example in which you harvest and use information from blogs, you learn to develop software that you can embed in your own applications. The code examples are immediately reusable and give the Java developer a working collective intelligence toolkit.    Along the way, you work with, a number of APIs and open-source toolkits including text analysis and search using Lucene, web-crawling using Nutch, and applying machine learning algorithms using WEKA and the Java Data Mining (JDM) standard.", 
    "status" : "PUBLISH", 
    "authors" : [ 
        "Satnam Alag" 
        ], 
    "categories" : [ 
        "Internet" 
        ] 
    }

book_rec3 = { 
    "_id" : 19, 
    "title" : "Jaguar Development with PowerBuilder 7", 
    "isbn" : "1884777864", 
    "pageCount" : 550, 
    "publishedDate" : { 
        "date" : "1999-08-01T00:00:00.000-0700" 
        }, 
    "thumbnailUrl" : "https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/barlotta2.jpg", 
    "shortDescription" : "Jaguar Development with PowerBuilder 7 is the definitive guide to distributed application development with PowerBuilder.", 
    "longDescription" : "Jaguar Development with PowerBuilder 7 is the definitive guide to distributed application development with PowerBuilder. It is the only book dedicated to preparing PowerBuilder developers for Jaguar applications and has been approved by Sybase engineers and product specialists who build the tools described in the book.    Jaguar Development with PowerBuilder 7 focuses on getting you up to speed on Jaguar and PowerBuilder, and it is packed with code samples to guide you every step of the way. It covers each step involved in application development, from setting up the development environment to deploying a production application.    Even a PowerBuilder developer with no experience in distributed technologies or Jaguar CTS will learn what it takes to build an application. Jaguar Development with PowerBuilder 7 covers:    Developing Component-centric Applications  Building Jaguar CTS Components/Clients  CORBA  Adaptive SQL Anywhere  Adaptive Server Enterprise  and lots more!", 
    "status" : "PUBLISH", 
    "authors" : [ 
        "Michael Barlotta" 
        ], 
    "categories" : [ 
        "PowerBuilder", "Client-Server" 
        ] 
    }

inv_rec1 = { 
    "_id" : 1,
    "book_id" : 4, 
    "quantity" : 10
    }

inv_rec2 = { 
    "_id" : 2,
    "book_id" : 6, 
    "quantity" : 0
    }

inv_rec3 = { 
    "_id" : 3,
    "book_id" : 19, 
    "quantity" : 70
    }

cust_rec1 = { 
    "_id" : 5, 
    "FirstName" : "Apple", 
    "LastName" : "Seed", 
    "address" : {
        "street": "123 Fake Street", 
        "city": "Faketon", 
        "state": "MA", 
        "zip": "12345"
        } , 
    "contact" : {
        "phone" : "111-111-1111" , 
        "email" : "apple@test.com"
        } 
    }
 
cust_rec2 = { 
    "_id" : 6, 
    "FirstName" : "Berry",
     "LastName" : "Seed", 
     "address" : {
         "street": "900 Fake Street", 
         "city": "Faketon", 
         "state": "NH", 
         "zip": "12345"
         }, 
    "contact" : {
        "phone" : 333-111-1111 , 
        "email" : "berry@test.com"
        }
    }
 
# order schema
order_rec1 = { 
    "_id" : 1002, 
    "customer_id" : 2 , 
    "ship_address" : {
        "FirstName" : "Guava", 
        "LastName" : "Seed", 
        "street": "123 Fake Street", 
        "city": "Faketon", 
        "state": "MA", 
        "zip": "12345"
        }  
    }

order_line_rec1 = { 
    "_id" : 1 , 
    "order_id" : 1002, 
    "book_id" : 765, 
    "quantity" : 2 
}

