## Activities Performed
1. Project Setup
Uploaded the project files to GitHub and initialized it as a repository.
Updated the repository with relevant details, and connected collaborators to ensure smooth teamwork.
2. Git Hooks for Software Quality Assurance
Added a command in the main directory to automatically log git commits:
Integrated Bandit static code analysis tool by adding a .pre-commit file to the Git hooks. This file ensures that Bandit runs on the repository to perform static checks on the code whenever changes are committed.
Created and modified the pre-commit script, ensuring that Bandit checks the entire repository for potential security vulnerabilities.
Installed the pre-commit package using pip, ensuring that the pre-commit hooks work effectively in the local development environment.
3. Fuzzing for Testing and Quality Assurance
Developed a method to randomly generate file names of length 10, which is useful for fuzz testing.
This method calls these functions with random file names to simulate diverse input scenarios.
Developed a simpleFuzzer method that runs the fuzzing tests 10 times for each method, ensuring robust testing of all implemented functions.
4. Forensics and Logging for Traceability
Created a logging module at forensic.py  by logging: Start time of the method execution. End time after execution.
Any critical values associated with the method's processing.
End time after execution. Any critical values associated with the method's processing.
5. Continuous Integration (CI)
Explored Codacy's continuous integration (CI) sequence to automate code quality analysis.
Set up a CI pipeline by adding the codacy-analysis.yaml file to the .github/workflows directory, which integrates the Codacy Analysis into the GitHub repository’s Actions tab.
The integration automatically analyzes each commit made to the repository, helping maintain consistent code quality and automating the process of code reviews.

## Lessons Learned

GitHub Repository Management:

Gained hands-on experience with GitHub’s interface, including how to upload, manage, and collaborate on a project via the platform’s features.

Git Hooks and Bandit Integration:

Learned how to effectively implement Git hooks to automate static code analysis using Bandit. This enhances code quality by ensuring security checks are run automatically with each commit.
Realized the value of having tools that continuously monitor code for security vulnerabilities, which can significantly improve development workflows.

Fuzzing for Testing:

Discovered the importance of fuzz testing in software quality assurance. By generating random inputs, we can expose vulnerabilities or bugs that might not be caught by traditional testing methods.
Gained insight into simplifying the process of running fuzz tests across multiple methods, improving efficiency.

Logging for Debugging and Traceability:

Understood the significance of logging in data manipulation and function execution tracking. Proper logging not only helps in debugging but also in maintaining clear records of operations, which are essential for project auditing and troubleshooting.
Identified which parts of the code would benefit most from detailed logging to track important metrics and events, thus enhancing transparency.

Continuous Integration (CI) and Automated Code Reviews:

Learned the immense value of automated code reviews via CI tools like Codacy. Continuous integration tools streamline the review process by catching potential issues before they are merged into the main codebase.
Familiarized myself with GitHub Actions, understanding how it can integrate with CI tools to automate the process of code review and analysis, saving time and reducing human error.

Improved Development Efficiency:

Gained practical experience in integrating quality assurance practices directly into the development pipeline, which reduces manual errors and improves team collaboration.
Recognized how these tools and practices can be applied to both personal and professional projects to maintain high-quality code consistently.
By implementing these practices, we not only ensured the integrity and security of the code but also learned valuable skills in automation, testing, logging, and continuous integration that will be useful in both academic and professional settings. These tools have made the development process smoother, faster, and more reliable, providing a solid foundation for any future collaborative projects.