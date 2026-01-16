# How to synch solution from the pkoffee repository

Here is a concise tutorial for participants to fetch the latest changes from the upstream `main` branch into their local directory.

In your directory where you cloned from https://www.github.com/s3-school/pkoffee, you should have something like this:
```bash
➜  pkoffee (main) git remote -v      

upstream	git@github.com:s3-school/pkoffee.git (fetch)
upstream	git@github.com:s3-school/pkoffee.git (push)
origin  	git@github.com:<your-github-username>/pkoffee.git (fetch)
origin  	git@github.com:<your-github-username>/pkoffee.git (push)
``` 

If not, use `git remote add` or `git remote rename` ⬇️ 

#### 1. **Add the Upstream Remote**
```bash
git remote add upstream git@github.com:s3-school/pkoffee.git
```

#### 2. **Fetch the Latest Changes**
Fetch the latest changes from the upstream repository:
```bash
git fetch upstream
```

#### 3. **Checkout Your Local Branch**
Ensure you are on your local branch (e.g., `main` or your working branch):
```bash
git switch main
```

#### 4. **Merge Upstream Changes**
Merge the upstream `main` branch into your local branch:
```bash
git rebase upstream/main
```

#### 5. **Resolve Conflicts (if any)**
If there are merge conflicts, resolve them manually, then commit the changes:
```bash
git add .
git rebase --continue
```

#### 6. **Push Changes to Your Fork**
Push the updated branch to your fork (`<usernam>`):
```bash
git push --force <username> main
```

---

This ensures your local directory and fork are synchronized with the latest upstream changes.
