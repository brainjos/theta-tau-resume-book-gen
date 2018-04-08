# THETA TAU RHO BETA PLEDGE PROJECT 
## PART B: THETA TAU: "A PROFESSIONAL ENGINEERING FRATERNITY"

This resume book creation tool is intended for use by the Theta Tau Theta Gamma Chapter 
Corporate Sponsorship Committee. It's used in conjunction with a Google Form to compile
resume books for whatever companies the chapter has decided to submit to, based on events
that the chapter has worked on with these companies in the past.  

## Getting Started

The user should install the python library "pandas", a common data analysis library.
More information can be found [here](https://pandas.pydata.org/).  

### Google Forms

A Google Form is the best way to collect data and format it into a CSV file. The form
should be formatted as such:

- Applicant Name
  - Firstname Lastname
- Major
  - In this example, we've made each College of Engineering major its own radio checkbox option, with a field for an "Other" major. This allows for variation in how users input their majors (e.g. MechE vs. Mechanical Engineering vs. ME)
- Year
  - We elected to set the categories as "Freshman," "Sophomore," "Junior," "Senior," and "Graduate," but with some small modifications to the code, graduation year could be used as well.
- Companies Applicant is Applying to:
  - These companies will be determined by the Corporate Sponsorship Committee based on events held with them previously in the year, among other factors.
- Resume
  - The naming convention used here is firstname_lastname_resume.pdf which is very important.

### Downloading Resumes

Resumes should be downloaded in a folder called `resumes` in the working directory. The user should take care to ensure that every resume has been named correctly, as even one incorrectly named resume will prevent the program from working. They can be downloaded as a zip from Google Drive by anyone with access.

## Running the Program

In terminal, navigate to the folder with the resume folder and resume book program. Run `python resumebook` and follow the prompts in the terminal. This will generate a folder called `books` which contains a book for each company that the fraternity is working with. These compiled resumes can then be sent to companies by a Corporate Sponsorship Committee Chair.

## Authors

* **Josh Brainard** <brainjos@umich.edu>
* **Ryan Dailey** <rpdailey@umich.edu>, 
* **Sri Gulukota** <srig@umich.edu>
* **Andrew Pospeshil** <aposp@umich.edu>

## License

This project has no license so please don't steal it.

## Acknowledgments

* Aditya Tamanna
* Varun Rana
* Franklin Luo