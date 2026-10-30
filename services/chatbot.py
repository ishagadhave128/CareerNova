
def career_chatbot(user_message):

    message = user_message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii"]:
        return (
            "Hello! Welcome to CareerNova Smart Assistant.\n"
            "I can help you with Data Analytics, Web Development, "
            "Data Science and Software Development."
        )

    # Excel vs Power BI
    elif "difference" in message and "excel" in message and "power bi" in message:
        return (
            "Excel vs Power BI:\n\n"
            "Excel:\n"
            "1. Used for data entry and calculations.\n"
            "2. Uses formulas and Pivot Tables.\n"
            "3. Suitable for spreadsheets and basic analysis.\n\n"
            "Power BI:\n"
            "1. Used for data visualization and dashboards.\n"
            "2. Uses DAX and Power Query.\n"
            "3. Suitable for interactive reports.\n\n"
            "Example: Excel calculates sales, while Power BI "
            "creates interactive sales dashboards."
        )
        # Python vs Excel
    elif "difference" in message and "python" in message and "excel" in message:
        return (
            "Python vs Excel:\n\n"
            "Python is a programming language used for automation, "
            "data analysis and software development.\n\n"
            "Excel is a spreadsheet application used for data entry, "
            "calculations and reporting.\n\n"
            "Python uses code and libraries like Pandas and NumPy, "
            "while Excel uses formulas and Pivot Tables.\n\n"
            "Example: Python can automate large data analysis tasks, "
            "while Excel is useful for spreadsheet-based analysis."
        )

    # Frontend vs Backend
    elif "difference" in message and "frontend" in message and "backend" in message:
        return (
            "Frontend vs Backend:\n\n"
            "Frontend is the visible part of a website that users interact with. "
            "It uses HTML, CSS and JavaScript.\n\n"
            "Backend handles server-side operations, databases and application "
            "logic. It uses Python, Java, PHP and other technologies.\n\n"
            "Example: A login button is frontend, while verifying login details "
            "is a backend task."
        )

        # HTML vs CSS
    elif "difference" in message and "html" in message and "css" in message:
        return (
            "HTML vs CSS:\n\n"
            "HTML (HyperText Markup Language) creates the structure "
            "of a webpage. It adds headings, paragraphs, images and links.\n\n"
            "CSS (Cascading Style Sheets) controls the appearance "
            "of a webpage, including colors, fonts, spacing and layouts.\n\n"
            "Example: HTML creates a heading, while CSS changes "
            "its color, size and style."
        )

    # HTML
    elif "html" in message:
        return (
            "HTML stands for HyperText Markup Language.\n"
            "It is used to create the structure of web pages.\n"
            "It helps add headings, paragraphs, images, links and buttons.\n"
            "HTML is the skeleton of a webpage."
        )

    # CSS
    elif "css" in message:
        return (
            "CSS stands for Cascading Style Sheets.\n"
            "It is used to style web pages by adding colors, fonts, "
            "spacing, layouts and responsive designs."
        )

    # JavaScript
    elif "javascript" in message:
        return (
            "JavaScript is a programming language used to make websites "
            "interactive.\n"
            "It handles actions such as button clicks, form validation, "
            "menus and dynamic content."
        )

    # Web Development
    elif "web development" in message or "web developer" in message:
        return (
            "Skills required for Web Development:\n"
            "1. HTML\n2. CSS\n3. JavaScript\n4. Python\n"
            "5. MySQL\n6. Git and GitHub\n7. Flask or Django\n\n"
            "Start with HTML, CSS and JavaScript."
        )
    
        # Data Analyst vs Data Scientist
    elif "difference" in message and "data analyst" in message and "data scientist" in message:
        return (
            "Data Analyst vs Data Scientist:\n\n"
            "Data Analyst analyzes existing data to find trends, "
            "prepare reports and support business decisions.\n"
            "Common tools: Excel, SQL and Power BI.\n\n"
            "Data Scientist uses statistics, programming and "
            "Machine Learning to build predictive models.\n"
            "Common tools: Python, SQL and Machine Learning.\n\n"
            "Example: A Data Analyst studies past sales, while "
            "a Data Scientist predicts future sales."
        )

    # Data Analyst
    elif "data analyst" in message or "data analytics" in message:
        return (
            "A Data Analyst collects, cleans and analyzes data "
            "to help organizations make better decisions.\n\n"
            "Important skills:\n"
            "1. Excel\n2. SQL\n3. Python\n4. Power BI\n"
            "5. Statistics\n6. Data Visualization\n\n"
            "Practical projects help improve analytical skills."
        )

    # Data Scientist
    elif "data scientist" in message or "data science" in message:
        return (
            "A Data Scientist uses statistics, programming and machine "
            "learning to analyze data and build predictive models.\n\n"
            "Important skills:\n"
            "1. Python\n2. SQL\n3. Statistics\n4. Mathematics\n"
            "5. Pandas and NumPy\n6. Machine Learning\n"
            "7. Data Visualization"
        )

    # Machine Learning
    elif "machine learning" in message:
        return (
            "Machine Learning is a branch of Artificial Intelligence.\n"
            "It allows computers to learn patterns from data and make "
            "predictions without being explicitly programmed for every task.\n\n"
            "Examples include spam detection, recommendation systems "
            "and price prediction."
        )

    # Software Developer
    elif "software developer" in message or "software development" in message:
                return (
            "A Software Developer designs, builds, tests and maintains "
            "software applications.\n\n"
            "Main responsibilities:\n"
            "1. Understand user requirements.\n"
            "2. Write and maintain code.\n"
            "3. Find and fix software bugs.\n"
            "4. Test applications.\n"
            "5. Update and improve software.\n\n"
            "Important skills include Python, Java, SQL, "
            "OOP, Git and Problem Solving."
        )

    # Python
    elif "python" in message:
        return (
            "Python is a beginner-friendly, high-level programming language.\n\n"
            "Important topics:\n"
            "1. Variables and Data Types\n2. Conditions and Loops\n"
            "3. Functions\n4. Lists and Dictionaries\n"
            "5. Object-Oriented Programming\n6. Pandas and NumPy\n\n"
            "Python is used in web development, data analysis and AI."
        )

    # SQL
    elif "sql" in message or "mysql" in message:
        return (
            "SQL stands for Structured Query Language.\n"
            "It is used to store, retrieve and manage data in relational databases.\n\n"
            "Important topics:\n"
            "1. SELECT and WHERE\n2. ORDER BY\n3. GROUP BY\n"
            "4. JOINS\n5. Subqueries\n6. CTEs\n"
            "7. Window Functions"
        )

    # Excel
    elif "excel" in message:
        return (
            "Microsoft Excel is a spreadsheet application used for "
            "data entry, calculations and data analysis.\n\n"
            "Important skills:\n"
            "1. VLOOKUP and XLOOKUP\n2. Pivot Tables\n"
            "3. IF and COUNTIF\n4. Conditional Formatting\n"
            "5. Data Validation\n6. Power Query"
        )

    # Power BI
    elif "power bi" in message:
        return (
            "Power BI is a Business Intelligence tool by Microsoft.\n"
            "It is used to transform data into interactive reports "
            "and dashboards.\n\n"
            "Important skills:\n"
            "1. Data Cleaning\n2. Power Query\n3. Data Modeling\n"
            "4. DAX\n5. Visualizations\n6. Dashboard Development"
        )

    # Interview
    elif "interview" in message:
        return (
            "Interview Preparation Tips:\n"
            "1. Prepare your self-introduction.\n"
            "2. Practice SQL queries.\n"
            "3. Revise Python basics.\n"
            "4. Learn Excel and Power BI.\n"
            "5. Prepare project explanations.\n"
            "6. Practice communication skills."
        )

    # Default response
    else:
        return (
            "Sorry, I don't have a specific answer for this question yet.\n\n"
            "I can help you with:\n"
            "1. Data Analyst\n2. Web Developer\n"
            "3. Data Scientist\n4. Software Developer\n"
            "5. Python, SQL, Excel and Power BI\n"
            "6. HTML, CSS and JavaScript\n"
            "7. Interview Preparation\n\n"
            "Please try asking a question about these topics."
        )
