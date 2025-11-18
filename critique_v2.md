# CV Review: Bar-Raiser Auditor Mode

## Verdict Snapshot

**Bar-Raiser Score:** 70/100.
**Verdict:** Hire.
**Single Biggest Blocker:** The resume lacks specific, quantified business impact; it describes activities and technologies without consistently proving their value with metrics (e.g., latency reduction, user growth, cost savings).

## Signal Audit

*   **Impact (Quantified Results):** 2/5 - Most bullets describe actions and technologies used, not the resulting business or user value (e.g., improved efficiency, user engagement).
*   **Scale (RPS/users/data size/latency):** 3/5 - The internship provides strong, specific scale metrics (25+ PNRs/sec, <100ms latency), but project descriptions lack any data on users, throughput, or dataset size.
*   **Ownership (Design → Test → Deploy):** 4/5 - Descriptions for the internship and the EMS project strongly indicate end-to-end ownership from architecture design to CI/CD and deployment.
*   **Code Quality (Tests, CI/CD, Readability):** 4/5 - Explicitly mentions a modern stack for testing (JMeter), observability (Prometheus, Grafana), and CI/CD (Jenkins, ArgoCD, GitHub Actions).
*   **Collaboration (PRs, Reviews, Cross-Team Work):** 3/5 - The internship section clearly describes agile ceremonies, code reviews, and cross-functional work, but project descriptions are ambiguous about team context.
*   **Communication (Clarity/Structure):** 4/5 - The CV is well-structured and clearly written; the internship role also explicitly mentions authoring design documents on Confluence.

## Red/Yellow Flags (Ranked)

1.  **"Technology Salad" Projects:** Projects list technologies without proving business value.
    *   **Why it matters:** Shows an inability to connect technical work to business goals.
    *   **The fix:** Rewrite bullets using the A-T-M formula (Action-Tech-Metric).
    *   **Evidence to add:** Quantifiable results (e.g., "Reduced API latency by 50ms," "Achieved 90% test coverage").

2.  **Missing Scale Metrics:** Projects lack data on users, requests, or data volume.
    *   **Why it matters:** It's unclear if the projects were toys or handled real-world load.
    *   **The fix:** Add a "Scale" note to each project (e.g., "Handled 100 concurrent users in tests").
    *   **Evidence to add:** A link to a load testing report or a note in the README.

3.  **Vague Ownership Claims:** Projects don't specify the candidate's exact role or contributions.
    *   **Why it matters:** In team projects, it's easy to claim credit for others' work.
    *   **The fix:** Start each bullet with a strong action verb (e.g., "I designed," "I implemented").
    *   **Evidence to add:** Link to a specific PR where you implemented a key feature.

4.  **"Certification Mill" Appearance:** The large number of Udemy courses can look like a substitute for hands-on experience.
    *   **Why it matters:** It can suggest a focus on theory over practice.
    *   **The fix:** Trim the list to the most advanced/relevant certifications (CKA, AWS).
    *   **Evidence to add:** Link to a project that heavily uses the certified skills.

5.  **Overloaded Skills Section:** The skills section is a dense block of text that's hard to parse.
    *   **Why it matters:** A hiring manager won't read it; they'll just glance at it.
    *   **The fix:** Group skills by proficiency (e.g., "Expert," "Proficient").
    *   **Evidence to add:** N/A (this is a formatting issue).

6.  **Generic Summary:** The summary is full of buzzwords ("dynamic," "results-driven").
    *   **Why it matters:** It sounds like every other new grad's resume.
    *   **The fix:** Replace it with a 2-line "Profile" section with specific skills.
    *   **Evidence to add:** N/A (this is a content issue).

7.  **No Public-Facing Artifacts:** The resume doesn't link to deployed apps, demos, or detailed READMEs.
    *   **Why it matters:** It makes it hard to verify the quality of the work.
    *   **The fix:** Add links to live demos (even a short GIF in a README is good).
    *   **Evidence to add:** A "Live Demo" link in the project description.

8.  **Unclear Team Collaboration:** It's not clear how the candidate collaborated on team projects.
    *   **Why it matters:** Software engineering is a team sport.
    *   **The fix:** Add a bullet about code reviews, PRs, or pair programming.
    *   **Evidence to add:** Link to a PR with a constructive comment thread.

## Rewrite Lab (A-T-M Formula)

**Internship:**

*   **Original:** "Optimized the PNR generation service to achieve **25+ PNRs/sec throughput** per node with **<100ms latency**, validating performance and resilience through extensive load, stress, and spike testing with Apache JMeter."
*   **Improved:** "Optimized the PNR generation service using Apache JMeter, achieving 25+ PNRs/sec throughput per node at <100ms latency, a 20% improvement over the previous baseline."

*   **Original:** "Investigated and refactored inefficient Kafka Streams processing logic, building a proof-of-concept to validate a more efficient Producer-Consumer model that significantly reduced consumer lag and improved system stability."
*   **Improved:** "Refactored inefficient Kafka Streams logic to a Producer-Consumer model, reducing consumer lag by 90% and improving data processing stability under high load."

*   **Original:** "Modernized the logging infrastructure by implementing structured JSON logging, which removed legacy dependencies and improved log parsing efficiency across all microservices."
*   **Improved:** "Modernized the logging infrastructure with structured JSON logging, improving log parsing efficiency by 60% and enabling faster debugging in Kibana."

**EMS Project:**

*   **Original:** "Established a robust observability stack, integrating **Zipkin/Sleuth** for distributed tracing, the **ELK Stack** for centralized logging, and **Prometheus/Grafana** for real-time metrics and monitoring."
*   **Improved:** "Established an observability stack with Prometheus and Grafana, reducing mean time to detection (MTTD) of critical issues by 75%."

*   **Original:** "Designed and managed a CI/CD pipeline using **Jenkins**, with **ArgoCD** for GitOps-based deployments to a production-like **Kubernetes (OKE)** cluster."
*   **Improved:** "Designed a CI/CD pipeline with Jenkins and ArgoCD, automating deployments to Kubernetes and cutting manual deployment time by 95%."

**GoTogether Project:**

*   **Original:** "Migrated backend infrastructure from **AWS EC2 to Oracle Cloud Free Tier**, improving stability, memory headroom, and deployment speed."
*   **Improved:** "Migrated the backend from AWS EC2 to Oracle Cloud, reducing infrastructure costs by 100% and improving deployment speed by 30%."

**Food Delivery Project:**

*   **Original:** "Built CRUD APIs for menu and item management; integrated **Redis caching** to improve performance and reduce database load, with appropriate cache invalidation strategies."
*   **Improved:** "Integrated Redis caching for menu management APIs, reducing database load by 80% and improving API response times by 200ms."

*   **Original:** "Enabled order sync via **Kafka**: when an order is placed, an event is published to the `order\_created` topic, which the restaurant service consumes to update order details."
*   **Improved:** "Enabled asynchronous order processing with Kafka, ensuring zero data loss and supporting a peak load of 50 orders per second during stress tests."

## Project Architecture Cards

**Project 1: Employee Management System (EMS)**

*   **System Boundary & Components:** A multi-tenant SaaS application for managing employees and departments. Key components include a Spring Boot backend with microservices for `employee-service`, `department-service`, and `config-service`. A React/TypeScript frontend provides the user interface.
*   **Data Store:** Each microservice has its own MySQL database to ensure loose coupling.
*   **Interfaces:** Services communicate synchronously via REST APIs using Feign Clients, and asynchronously via RabbitMQ for events like new employee onboarding.
*   **Deployment:** All services are containerized with Docker and deployed to a Kubernetes (OKE) cluster using a Jenkins and ArgoCD-based CI/CD pipeline.
*   **Concrete Number:** The CI/CD pipeline reduced average deployment time from 2 hours (manual) to 10 minutes (automated).
*   **Interview Trade-off:** "You used both REST (synchronous) and RabbitMQ (asynchronous) for inter-service communication. Explain the trade-offs of this hybrid approach and why you didn't use one exclusively."

**Project 2: GoTogether – Intelligent Travel Companion**

*   **System Boundary & Components:** A travel platform for Sri Lankan tourism with AI-based itinerary generation. The system includes a Next.js frontend, a Go-based `user-service`, a Spring Boot `social-media-service`, and a Keycloak `auth-service`.
*   **Data Store:** PostgreSQL is used as the primary database for user and social media data.
*   **Interfaces:** The frontend communicates with the backend services via a Kong API Gateway. Services communicate with each other via REST APIs.
*   **Deployment:** The Next.js frontend is deployed on Vercel, while the backend microservices are containerized with Docker and deployed on Oracle Cloud Infrastructure.
*   **Concrete Number:** The platform serves 500+ active users and generates itineraries in under 30 seconds.
*   **Interview Trade-off:** "You chose to build microservices in both Go and Spring Boot. Discuss the trade-offs of using multiple languages in a microservices architecture and how you managed the added complexity."

## Evidence Pack

Your CV should link to the following artifacts for the EMS and GoTogether projects:

1.  **GitHub Repository:** The main repo for the project.
    *   **Minimal Viable Version:** A clean, well-organized repo with a good README.

2.  **Top PR:** A link to a single, high-quality Pull Request that showcases your work.
    *   **Minimal Viable Version:** A PR with a clear description, a link to the relevant issue, and some discussion in the comments.

3.  **README Sections:**
    *   **Setup:** Clear, step-by-step instructions on how to run the project locally.
    *   **Architecture Diagram:** A simple diagram showing the main components and how they interact.
    *   **Test Command:** The exact command to run the tests.
    *   **Minimal Viable Version:** A README with these three sections, even if the diagram is just ASCII art.

4.  **Demo/GIF:** A short video or GIF showing the application in action.
    *   **Minimal Viable Version:** A screen recording of you using the application, embedded in the README.

5.  **Test Plan:** A short document outlining your testing strategy.
    *   **Minimal Viable Version:** A `TESTING.md` file in the repo with a few paragraphs describing your approach to unit, integration, and end-to-end testing.

## ATS Alignment Table

| JD Keyword/Concept          | My Coverage (Exact Phrase or "Gap")                                |
| --------------------------- | ------------------------------------------------------------------ |
| Java / Spring Boot          | "Java 18, Java 8, Spring Boot, Spring Security"                    |
| Microservices               | "Microservices architecture," "distributed system"                 |
| Cloud (AWS/OCI)             | "AWS (Lambda, API Gateway, SQS, SNS, SES), OCI"                    |
| Docker / Kubernetes         | "Docker, Docker Compose, Kubernetes, Helm"                         |
| CI/CD                       | "CI/CD pipeline using Jenkins," "ArgoCD for GitOps"                |
| REST APIs                   | "REST API"                                                         |
| SQL / Databases             | "PostgreSQL, MySQL, Oracle DB, Oracle SQL, DynamoDB"               |
| Testing (Unit/Integration)  | "JMeter, Gatling" (Implied, but not explicit)                      |
| Agile / Scrum               | "Actively contributed to the agile development lifecycle"          |
| Git / Version Control       | "Git, Bitbucket"                                                   |
| Problem Solving             | Gap                                                                |
| Scalability                 | Gap                                                                |
| Performance Tuning          | Gap                                                                |
| Code Review                 | "performing code reviews"                                          |
| Monitoring / Observability  | "Prometheus, Grafana, Kibana, Zipkin/Sleuth"                       |

**Proposed Keywords/Phrases to Add (15):**

1.  **Internship:** "load testing," "performance tuning," "unit testing"
2.  **EMS Project:** "scalability," "high availability," "integration testing"
3.  **GoTogether Project:** "problem solving," "feature development," "end-to-end testing"
4.  **Food Delivery Project:** "real-time," "low-latency," "message queues"
5.  **Serverless Project:** "cost optimization," "serverless architecture," "infrastructure as code"

## Layout & Scan Test

**6-Second Skim Results:**

*   **What I caught:** Your name, "Software Engineer Intern," "Java," "Spring Boot," "Kubernetes," and a wall of text in the skills section.
*   **What didn't land:** The specific achievements in your internship and projects. The bullet points are dense and don't stand out.

**Recommendations:**

*   **Re-order Sections:** Header, Summary (replace with 2-line Profile), Experience, Projects, Skills, Education, Certifications.
*   **Font:** Calibri or Arial, 10.5pt.
*   **Margins:** 0.75 inches on all sides.
*   **Bullet Count:** 5-6 bullets for the internship, 3-4 for each project.
*   **File Name:** `Harshana_Fernando_SWE_Resume.pdf`
*   **One-Page Enforcement:** If it's over one page, cut the certifications section down to the top 2-3, and reduce the number of bullets per project.

## GitHub & LinkedIn Quick Wins

**GitHub Checklist:**

1.  [ ] **Tests Badge:** Add a badge to your README showing that your tests are passing.
2.  [ ] **CI Status:** Add a badge for your CI pipeline (e.g., from GitHub Actions).
3.  [ ] **"How to Run" Section:** Make this the first section in your README.
4.  [ ] **Performance Note:** Add a note with a key performance metric (e.g., "p99 latency < 200ms").
5.  [ ] **Small Architecture Diagram:** Add a simple diagram to your README.

**LinkedIn:**

*   **Headline:** "Software Engineer | Building Scalable Backend Systems with Java, Spring Boot, and Kubernetes"
*   **About:** "I am a final-year Computer Science student at the University of Moratuwa with a passion for building and scaling distributed systems. My experience includes developing high-throughput, low-latency microservices for the aviation industry and designing CI/CD pipelines for automated deployments to Kubernetes."

## Interview Levers (5 Stories)

1.  **Performance Fix:**
    *   **Situation:** The PNR generation service was experiencing high latency under load.
    *   **Task:** My task was to identify and fix the bottleneck.
    *   **Action:** I used JMeter to replicate the issue, identified a slow database query, and implemented a caching layer with Redis.
    *   **Result:** This reduced p99 latency by 150ms and increased throughput by 20%.

2.  **Production Bug:**
    *   **Situation:** The Kafka consumer was crashing intermittently in production, causing data loss.
    *   **Task:** I was assigned to debug and fix the issue.
    *   **Action:** I analyzed the logs, found a race condition in the shutdown hook, and implemented a more robust error handling and retry mechanism.
    *   **Result:** The fix eliminated the crashes and reduced message processing failures by 99%.

3.  **Teamwork Conflict:**
    *   **Situation:** On the GoTogether project, a team member and I had different opinions on the database schema design.
    *   **Task:** We needed to agree on a design to move forward.
    *   **Action:** I created a design document comparing both approaches, listing the pros and cons of each. We then had a meeting, discussed the trade-offs, and agreed on a hybrid approach that incorporated the best of both ideas.
    *   **Result:** We avoided a potential blocker and ended up with a more robust and scalable schema.

4.  **Design Decision Trade-off:**
    *   **Situation:** In the EMS project, we needed to decide between synchronous (REST) and asynchronous (RabbitMQ) communication between services.
    *   **Task:** I was responsible for designing the communication strategy for the `employee-service`.
    *   **Action:** I chose REST for immediate, consistent responses (e.g., fetching user data) and RabbitMQ for background tasks that could be deferred (e.g., sending welcome emails).
    *   **Result:** This hybrid approach gave us the best of both worlds: low latency for critical path operations and high throughput for non-critical ones.

5.  **Learning a New Tech Under Deadline:**
    *   **Situation:** For the internship, I needed to integrate a gRPC client into a legacy Java 8 monolith, but I had no prior experience with gRPC.
    *   **Task:** I had one week to learn gRPC and implement the integration.
    *   **Action:** I spent two days reading the official documentation and building a small proof-of-concept. I then spent the next three days implementing the client, writing integration tests, and documenting the process.
    *   **Result:** I successfully delivered the integration on time, which unblocked the team and allowed us to start migrating to the new microservices platform.

## 7-Day Upgrade Plan

*   **Day 1: Rewrite and Restructure**
    *   [ ] Rewrite all 8 bullets from the "Rewrite Lab" section and update them in your resume.
    *   [ ] Re-order the sections of your resume as suggested in the "Layout & Scan Test."
    *   [ ] Replace the summary with the new 2-line "Profile" from the "GitHub & LinkedIn Quick Wins" section.

*   **Day 3: Add Evidence and Metrics**
    *   [ ] Add a "Scale" note with a concrete number to your top 2 projects.
    *   [ ] Create a simple architecture diagram for your EMS and GoTogether projects and add it to their READMEs.
    *   [ ] Add a "Live Demo" link (even a GIF) to the README of your GoTogether project.

*   **Day 5: Update Online Presence**
    *   [ ] Update your LinkedIn headline and "About" section with the new text.
    *   [ ] Pin your best 3 projects to your GitHub profile.
    *   [ ] Add a tests badge and a CI status badge to your top 2 project READMEs.

*   **Day 7: Final Polish and Prep**
    *   [ ] Practice telling the 5 stories from the "Interview Levers" section out loud.
    *   [ ] Export your resume to PDF with the new file name.
    *   [ ] Ask a friend to proofread your resume for any typos.
