# LinkedIn Job Analytics 

### Introduction

LinkedIn Job Analytics is a project aimed at extracting valuable insights from job listings on the professional networking platform LinkedIn. By scraping data from LinkedIn job collections, the project provides a comprehensive analysis of job distribution across various parameters such as location, industry, and company size. The generated insights can benefit job seekers, recruiters, and career analysts by offering valuable information for decision-making and trend analysis.

### Overview

The project involves scraping data from LinkedIn job collections and organizing it into structured tables. These tables are then used to generate aggregations and insights for creating an interactive dashboard. The dashboard provides visualizations and analytics to help users understand job market trends, compare job opportunities across different criteria, and make informed decisions.

## Phase 1:

Scraping data from LinkedIn job collections.
Organizing the scraped data into structured tables (jobs, company, and details).
Generating aggregations and insights for creating an interactive dashboard.

### Tables

#### Jobs

|   |   |
| ------------ | ------------ |
| job_id  | Primary key for jobs table  |
|  company_id |  A key to map with company table (table - 2) as one company can have multiple jobs  |
|  location |   The location of the job |
| designation  |  The designation of the job |
| details_id  | A key to map with details table (table - 3) as every job has some description  |

#### Company
|   |   |
| ------------ | ------------ |
|  company_id |  The primary key |
|  name |  Name of the company |
| industry  |   Industry in which the company operates |
|  employees_count |  Count of employees |
| linkedin_followers  | Number of followers on LinkedIn  |

#### details
|   |   |
| ------------ | ------------ |
|  details_id |  The primary key |
|  involvement |  The nature of involvement in the job, for instance: Full-time, part-time  |
| level  |  The seniority level like Mid-Senior level |
| total_applicants  |  Total number of applicants |

### Scraping 
The project involves scraping data from LinkedIn job collections using Python libraries such as Selenium. By accessing the LinkedIn job collections URL, the project extracts relevant job details including job ID, company information, job location, job designation, company industry, number of employees, number of LinkedIn followers, job involvement, job level, and total number of applicants.


## Phase 2: 

- Enhancing the details table by adding a column for necessary skills required for each job 
   position.
- Categorizing companies based on employee count and LinkedIn followers using clustering 
  algorithms.

### Website
- Creating a search bar feature allowing users to search for specific skills.
- Displaying relevant information such as experience level, industry, company class, and number 
  of job openings for the searched skills.
#### Search Functionality
- Users can search for skills using the search bar.
- Upon searching, the following information will be displayed:

  1.Most common experience level required for the skill(s) from the details table.
  
  2.Most common industry where the skill(s) are required.
  
  3.Most common company class where the skill(s) are required.
  
  4.Number of available jobs for the skill(s).

## Final Outcome

The final outcome will be an interactive dashboard providing insights and analytics based on scraped LinkedIn data, including job distribution, skill requirements, company classifications, and more.
