# GIT

most of the cheatsheet for git are in my got notebook (see code_Notes)


---

# 📋 **Summary of Useful Git Functions**

## **1. Configuration Commands**
- **Set your global username and email**:  
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

- **Check configuration**:  
  ```bash
  git config --list
  ```

---

## **2. Repository Management**
- **Initialize a Git repository**:  
  ```bash
  git init
  ```

- **Clone a repository**:  
  ```bash
  git clone <repository-url>
  ```

- **Check repository status**:  
  ```bash
  git status
  ```

---

## **3. Staging and Committing**
- **Stage files for commit**:  
  ```bash
  git add <file>          # Stage specific file
  git add .               # Stage all files
  ```

- **Commit changes**:  
  ```bash
  git commit -m "Your commit message"
  ```

- **Amend the last commit**:  
  ```bash
  git commit --amend -m "Updated commit message"
  ```

---

## **4. Branching**
- **Create a new branch**:  
  ```bash
  git branch <branch-name>
  ```

- **List all branches**:  
  ```bash
  git branch -a
  ```

- **Switch to a branch**:  
  ```bash
  git checkout <branch-name>
  ```

- **Create and switch to a new branch**:  
  ```bash
  git checkout -b <branch-name>
  ```

---

## **5. Merging and Rebase**
- **Merge a branch into the current branch**:  
  ```bash
  git merge <branch-name>
  ```

- **Rebase current branch onto another branch**:  
  ```bash
  git rebase <base-branch>
  ```

---

## **6. Remote Repository**
- **Add a remote repository**:  
  ```bash
  git remote add origin <repository-url>
  ```

- **Push changes to remote repository**:  
  ```bash
  git push origin <branch-name>
  ```

- **Pull changes from remote repository**:  
  ```bash
  git pull origin <branch-name>
  ```

- **Fetch updates without merging**:  
  ```bash
  git fetch
  ```

- **Show remote URLs**:  
  ```bash
  git remote -v
  ```

---

## **7. Logs and Diffs**
- **View commit history**:  
  ```bash
  git log
  ```

- **View changes between commits or branches**:  
  ```bash
  git diff
  git diff <commit1> <commit2>
  ```

---

## **8. Reset and Revert**
- **Reset changes**:  
  ```bash
  git reset <file>           # Unstage a file
  git reset --hard <commit>  # Reset to a specific commit
  ```

- **Revert changes**:  
  ```bash
  git revert <commit>
  ```

---

## **9. Stashing Changes**
- **Save uncommitted changes**:  
  ```bash
  git stash
  ```

- **Apply stashed changes**:  
  ```bash
  git stash apply
  ```

- **List stashes**:  
  ```bash
  git stash list
  ```

- **Delete stashes**:  
  ```bash
  git stash drop
  ```

---

## **10. Tags**
- **Create a tag**:  
  ```bash
  git tag <tag-name>
  ```

- **List tags**:  
  ```bash
  git tag
  ```

- **Push tags to remote**:  
  ```bash
  git push origin <tag-name>
  ```

---

## **11. Undo Changes**
- **Discard local changes**:  
  ```bash
  git checkout -- <file>
  ```

- **Remove untracked files**:  
  ```bash
  git clean -f
  ```

---

## **12. Aliases**
- **Create a Git alias**:  
  ```bash
  git config --global alias.<alias-name> "<git-command>"
  ```

**Example**:  
```bash
git config --global alias.co "checkout"
git co <branch-name>
```

---

## **13. Useful Shortcuts**
- **Check a concise log**:  
  ```bash
  git log --oneline --graph --all
  ```

- **View file blame**:  
  ```bash
  git blame <file>
  ```

---

## **14. Git Ignore**
- **Create a `.gitignore` file** to exclude files:  
  ```
  __pycache__/
  *.log
  *.tmp
  ```

- **Apply ignored files**:  
  ```bash
  git rm --cached <file>
  ```

---

### ⚡ **Tips**  
- Use `git status` often to check your current changes.
- Always pull before pushing changes to a remote repository.
- Commit frequently with meaningful messages.

---