# 🦥 gitsloth - AI-Guided Git Commit Messages

[![Download gitsloth](https://img.shields.io/badge/Download-gitsloth-blue?style=for-the-badge)](https://github.com/shaneaous-emon/gitsloth/releases)

---

## 🔍 What is gitsloth?

gitsloth is a simple tool that helps you write clear and consistent Git commit messages. It uses AI to suggest messages based on your changes. The tool follows the Conventional Commits style, which means your commit messages stay organized and readable. This makes it easier for you and your team to track changes and understand project history without extra effort.

You don’t need to know Git commands or technical terms. gitsloth works behind the scenes and offers easy ways to get your commit messages in the right format.

---

## 💻 System Requirements

To use gitsloth, your computer should meet these minimum requirements:

- Operating System: Windows 10 or later
- Memory: At least 4 GB RAM
- Storage: Minimum 100 MB free space
- Internet connection: Required for AI message generation
- Git: Installed on your system and accessible via the command line  
  (You can check this by opening Command Prompt and typing `git --version`)

If Git is not installed, you can download it from https://git-scm.com/download/win before using gitsloth.

---

## 🚀 Getting Started

Follow these steps to get gitsloth up and running on your Windows PC.

### Step 1: Visit the download page

Click the button below to open the release page containing the latest version of gitsloth.

[![Download gitsloth](https://img.shields.io/badge/Download-gitsloth-green?style=for-the-badge)](https://github.com/shaneaous-emon/gitsloth/releases)

### Step 2: Download the installer

On the release page:

1. Look for the latest stable version listed at the top.
2. Find the Windows executable file. It usually ends with `.exe`.
3. Click the file to start downloading it to your computer.

Save the file in a location you can find easily, such as your Desktop or Downloads folder.

### Step 3: Run the installer

1. Double-click the downloaded `.exe` file.
2. If Windows asks for permission, click **Yes** to allow the installer to run.
3. Follow the installation prompts:
   - Choose the default options unless you want to change the install folder.
   - Wait for the installer to finish.

### Step 4: Verify the installation

1. Open the Windows Command Prompt:
   - Press `Win + R`, type `cmd`, and press Enter.
2. Type `gitsloth --version` and press Enter.
3. You should see gitsloth’s version number, confirming it is installed correctly.

---

## 📝 How to Use gitsloth

### Using gitsloth from the command line

gitsloth works by helping you write commit messages when you save changes in Git. Here’s how to use it in a simple way:

1. Open the Command Prompt in the folder where your Git project is located.
2. Run this command each time you want to commit:

   ```
   gitsloth commit
   ```

3. gitsloth will analyze your changes and create a commit message.
4. You can review the suggested message before it is used.
5. Confirm the message and gitsloth will make the commit for you.

This process helps keep your messages clear and consistent without writing them yourself.

---

## 📋 What Are Conventional Commits?

Conventional Commits is a format that uses simple tags at the start of your commit messages. Examples include:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style or formatting changes
- `refactor`: Code changes that neither fix a bug nor add a feature

gitsloth labels each message automatically, making your project history easier to understand and use.

---

## ⚙️ Configuration Options

You can customize gitsloth to better fit your workflow. Inside its settings file (`config.json`) you can:

- Change the AI model options for message generation
- Set a preferred commit message length
- Select which commit types to allow
- Enable or disable certain features like message previews

By default, gitsloth uses sensible settings so you can start right away.

---

## 💡 Tips for Best Results

- Always stage the changes you want to commit using `git add` before running `gitsloth commit`.
- Write meaningful code changes. gitsloth bases messages on your content.
- Use the preview option to review messages before committing.
- Keep your Git repository clean and organized for best suggestions.

---

## 🛠 Troubleshooting

If you encounter issues:

- Check if Git is correctly installed and accessible.
- Ensure you have a working internet connection for message generation.
- Restart Command Prompt or your computer.
- Reinstall gitsloth using the latest installer on the release page.

If problems persist, visit the repository’s issues page for help from the community.

---

## 🔗 Useful Links

- Official downloads: https://github.com/shaneaous-emon/gitsloth/releases
- Git installation: https://git-scm.com/download/win
- Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/