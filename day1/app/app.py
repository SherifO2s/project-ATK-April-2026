from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    profile = {
        "name": "Sherif Adebola Otufowora",
        "title": "Software Engineer",
        "email": "sherif.otufowora@gmail.com",
        "linkedin": "https://www.linkedin.com/in/sherif-o-a91a25171/",
        "github": "https://github.com/sherifotufowora",
        "tagline": "Building robust, scalable systems with clean code and thoughtful design.",
        "about": (
            "I'm a passionate software engineer with experience building full-stack applications, "
            "APIs, and data-driven products. I enjoy tackling complex problems and turning ideas "
            "into reliable, well-crafted software. When I'm not coding, I'm exploring new "
            "technologies and sharpening my skills."
        ),
        "skills": {
            "Languages": ["Python", "JavaScript", "TypeScript", "SQL"],
            "Frameworks": ["Flask", "React", "Node.js", "Express"],
            "Tools & Cloud": ["Git", "Docker", "AWS", "PostgreSQL", "MongoDB"],
            "Practices": ["REST APIs", "Agile / Scrum", "CI/CD", "TDD"],
        },
        "experience": [
            {
                "role": "Software Engineer",
                "company": "Your Company",
                "period": "2023 – Present",
                "bullets": [
                    "Designed and shipped RESTful APIs serving thousands of daily active users.",
                    "Led migration of legacy monolith to microservices, reducing deploy time by 40%.",
                    "Mentored junior engineers and conducted code reviews to uphold quality standards.",
                ],
            },
            {
                "role": "Junior Software Developer",
                "company": "Previous Company",
                "period": "2021 – 2023",
                "bullets": [
                    "Built and maintained React front-end components integrated with Flask backends.",
                    "Optimised database queries, reducing average API response time by 35%.",
                    "Collaborated cross-functionally with design and product teams in an Agile workflow.",
                ],
            },
        ],
        "projects": [
            {
                "name": "Portfolio Site",
                "description": "This very site — a Flask-powered personal portfolio with the Dark Pond colour palette.",
                "tech": ["Python", "Flask", "HTML/CSS", "JavaScript"],
                "link": "#",
            },
            {
                "name": "Project Alpha",
                "description": "A full-stack web application with real-time features and a PostgreSQL backend.",
                "tech": ["React", "Node.js", "PostgreSQL", "WebSockets"],
                "link": "#",
            },
            {
                "name": "Data Pipeline Tool",
                "description": "Automated ETL pipeline that ingests, transforms, and loads data at scale.",
                "tech": ["Python", "Airflow", "AWS S3", "Pandas"],
                "link": "#",
            },
        ],
        "education": [
            {
                "degree": "B.Sc. Computer Science",
                "institution": "Your University",
                "year": "2021",
            }
        ],
    }
    return render_template("index.html", p=profile)


if __name__ == "__main__":
    app.run(debug=True)
