"""Verified portfolio content and the editorial illustrations used on the site."""

PROJECTS = [
    {
        "slug": "agrisense",
        "title": "AgriSense",
        "subtitle": "Smart Agriculture Management System",
        "full_title": "AgriSense — Smart Agriculture Management System",
        "category": "Full-stack / Smart agriculture",
        "stack": ["Java", "Spring Boot", "MySQL", "HTML", "CSS", "JavaScript"],
        "summary": "A farm management application that recommends crops and fertilizer based on soil information.",
        "context": "Choosing what to grow and how to nourish it starts with the soil. AgriSense brings both decisions into one web application, so a grower can use the same soil information to explore crop and fertilizer recommendations.",
        "workflow": [
            ("Soil information", "The soil details provide the starting point for a recommendation."),
            ("Crop selection", "The application recommends crops based on those details."),
            ("Fertilizer guidance", "The grower can also see fertilizer recommendations for the soil."),
        ],
        "plate": "farm",
        "caption": "Soil & crop patterns",
        "alt": "Cultivated rows crossed by a fine soil-sampling grid.",
    },
    {
        "slug": "smartcityx",
        "title": "SmartCityX",
        "subtitle": "Smart City Management System",
        "full_title": "SmartCityX — Smart City Management System",
        "category": "Smart city / Full-stack",
        "stack": ["Java", "Spring Boot", "MongoDB", "HTML", "CSS", "JavaScript"],
        "summary": "A city management platform for citizen complaints about traffic, waste, water and streetlights.",
        "context": "A broken streetlight and a water complaint concern different services, but both need a place to be recorded. SmartCityX brings complaints across four areas of city life into a single web platform.",
        "workflow": [
            ("Citizen complaint", "A reported problem provides the starting point for a city service record."),
            ("Service area", "The platform covers traffic, waste, water and streetlights."),
            ("Complaint management", "City service complaints can be managed together within the application."),
        ],
        "plate": "city",
        "caption": "Urban service network",
        "alt": "An architectural cityscape with a coral network connecting points across the skyline.",
    },
    {
        "slug": "pathfinder",
        "title": "PATHFINDER",
        "subtitle": "Career Guidance Chatbot",
        "full_title": "PATHFINDER — Career Guidance Chatbot",
        "category": "AI / Chatbot development",
        "stack": ["Python", "Tkinter"],
        "summary": "A desktop chatbot that helps students explore career options through their skills and interests.",
        "context": "For a student exploring careers, a useful starting point is what they already enjoy and do well. PATHFINDER uses a conversational interface to connect those interests and skills with possible career directions.",
        "workflow": [
            ("Start a conversation", "The student interacts with the chatbot through a Tkinter desktop interface."),
            ("Explore interests", "The conversation draws on the student's interests and skills."),
            ("Consider directions", "The chatbot helps the student explore career options related to that input."),
        ],
        "plate": "pathfinder",
        "caption": "Paths of possibility",
        "alt": "A coral wireframe landscape with several intersecting paths on charcoal.",
    },
    {
        "slug": "certificate-authentication",
        "title": "Certificate Authentication",
        "subtitle": "Blockchain-based academic certificate verification",
        "full_title": "Blockchain-Based Academic Certificate Authentication and Verification System",
        "category": "Blockchain / Web development",
        "stack": ["Blockchain", "Solidity", "Ethereum", "Web3.js", "Smart Contracts", "HTML", "CSS", "JavaScript"],
        "summary": "A decentralized application that uses blockchain records and QR codes to verify academic certificates.",
        "context": "An institution or employer needs a way to check whether a certificate is authentic. This application connects academic records with QR-based verification, using blockchain technology to help protect the integrity of the records.",
        "workflow": [
            ("Academic record", "The application stores certificate information using blockchain technology."),
            ("QR code", "A QR code gives the verifier a route to the certificate check."),
            ("Authenticity check", "Institutions and employers can use the application to verify a certificate."),
        ],
        "plate": "certificate",
        "caption": "Layers of verification",
        "alt": "Translucent coral blocks form a stack of linked records around a verification mark.",
    },
    {
        "slug": "smart-vehicle-parking",
        "title": "Smart Vehicle Parking",
        "subtitle": "Smart Vehicle Parking Management System",
        "full_title": "Smart Vehicle Parking Management System",
        "category": "Smart infrastructure / Full-stack",
        "stack": ["Java", "Spring Boot", "MySQL", "HTML", "CSS", "JavaScript"],
        "summary": "A parking management system that records vehicle entries and exits and shows which spaces are available.",
        "context": "Knowing whether a space is free depends on knowing which vehicles have arrived and left. This application connects vehicle movement with slot availability, bringing both into one parking management system.",
        "workflow": [
            ("Vehicle entry", "The system manages vehicles entering the parking area."),
            ("Slot availability", "The application displays available parking spaces."),
            ("Vehicle exit", "Departure information helps the system keep track of available slots."),
        ],
        "plate": "parking",
        "caption": "Space & occupancy",
        "alt": "An architectural parking structure paired with a diagram of marked parking bays.",
    },
]

EXPERTISE = [
    ("code", "Programming languages", "Java, Python, C, C++"),
    ("layers", "Web technologies", "HTML, CSS, JavaScript"),
    ("grid", "Frameworks", "Spring Boot, JDBC"),
    ("network", "AI, ML & data science", "Artificial intelligence, machine learning, data science"),
    ("database", "Databases", "MySQL, SQL"),
    ("braces", "Core concepts", "Object-oriented programming, data structures and algorithms, database management systems"),
    ("tools", "Tools & platforms", "VS Code, IntelliJ IDEA, Git, GitHub, XAMPP, Figma, Canva"),
    ("people", "Soft skills", "Problem-solving, communication, teamwork"),
]

EDUCATION = [
    ("2024–2028", "B.E. — Artificial Intelligence and Machine Learning", "PSNA College of Engineering and Technology", "CGPA 8.29 / 10"),
    ("2024", "HSC — 12th Standard", "Lakshmi Matriculation Higher Secondary School", "73.5%"),
    ("2022", "SSLC — 10th Standard", "Lakshmi Matriculation Higher Secondary School", "84.6%"),
]

TRAINING = [
    ("2026", ["Master in Full Stack in Java", "Entrepreneurship and Small Business", "Chatbot in Python", "Use AI for Everyday Tasks"]),
    ("2025", ["Generative AI", "AI/ML – Dreams Unlock"]),
    ("Additional training", ["AI Data Strategy with MongoDB", "RAG with MongoDB"]),
]

STUDIES = [
    ("volume", "Stacked volume", "Translucent cubes study how one surface changes the colour of the next."),
    ("wave", "Wave field", "A grid of fine lines bends across a continuous surface."),
    ("steps", "Stepped light", "A staircase turns a single light source into bands of coral, blush and graphite."),
]
