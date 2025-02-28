# Personal Tasks Repository

This repository is designed for submitting individual programming tasks for the Advanced Python course. Please follow these instructions carefully to submit your work.

## Repository Structure

Each student has their own designated folder within this repository. You only have write access to your personal folder as specified in the CODEOWNERS file.

## How to Submit Your Tasks

### 1. Initial Setup
```bash
# Clone the repository
git clone <repository-url>
cd Personal-Tasks

# Create and switch to a new branch for your task
git checkout -b task/your-student-id/task-name
```

### 2. Adding Your Work
- Place your files ONLY in your designated folder
- Make sure to include:
  - Source code files (.py)
  - Requirements.txt (if needed)
  - Brief documentation explaining your solution

### 3. Committing and Pushing
```bash
# Add your changes
git add your-folder/*

# Commit with a descriptive message
git commit -m "Add solution for Task X"

# Push to your branch
git push origin task/your-student-id/task-name
```

### 4. Creating a Pull Request
1. Go to the repository on GitHub
2. Click on "Pull Requests" and then "New Pull Request"
3. Select your branch as the source
4. Write a clear description of your changes
5. Submit the pull request

## Important Notes

- ⚠️ Never commit directly to the main branch
- ⚠️ Only modify files within your designated folder
- ✅ Each task should be submitted in a separate branch
- ✅ Wait for the instructor's review before merging
- ❌ Pull requests modifying other students' folders will be rejected

## Best Practices

1. Keep your commits atomic and well-described
2. Test your code thoroughly before submitting
3. Follow the Python style guide (PEP 8)
4. Include proper documentation
5. Respond to review comments promptly

## Need Help?

If you encounter any issues with the submission process, please contact the course instructor or teaching assistants.