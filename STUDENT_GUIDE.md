# Student guide

## Start the lab

1. Create a free account at [GitHub](https://github.com), or sign in.
2. Open the repository link your instructor provides. Click **Fork**, choose your personal account as owner, then **Create fork**. A fork is your own copy.
3. Confirm your username appears before the repository name. Choose **Code > Codespaces > Create codespace on main**, or the default branch shown. A 2 core machine with 8 GB RAM is sufficient.
4. Wait for VS Code to open and environment setup to finish. The first build can take several minutes. Packages and extensions install automatically. If setup fails, contact your instructor rather than installing anything yourself.
5. In the left Explorer, expand `notebooks` and open `01_getting_started.ipynb`.
6. If a kernel is not selected, click **Select Kernel** at the top right. Choose **Select Another Kernel > Jupyter Kernel > Python 3.12 (ECON 3030)**. If offered under **Python Environments** instead, choose Python 3.12 at `/usr/local/bin/python`. The kernel is the Python process that runs your code.
7. Click the triangle beside the first code cell. Wait for it to finish. Continue from top to bottom. You do not need a terminal.
8. Complete the three Texas exercises and the written answers. Double click a Markdown cell to edit its text, then press Shift+Enter to display it. Run each code cell after editing.

## Save and submit

9. Choose **File > Save** or press Ctrl+S on Windows/Linux or Cmd+S on Mac. Wait for the unsaved indicator on the tab to disappear.
10. In the left Explorer, right click `notebooks/01_getting_started.ipynb` and choose **Download**. Accept your browser's download prompt if shown. Find the file in your computer's Downloads folder. It should end in `.ipynb`. This is the [supported VS Code download workflow](https://code.visualstudio.com/docs/remote/codespaces).
11. Open Canvas, open the Lab 1 assignment, attach that one `.ipynb` file, and complete the submission. Check the submission confirmation. Do not submit the CSV, a screenshot, or a link to your Codespace.
12. Visit [Your codespaces](https://github.com/codespaces), find this Codespace, open its three dot menu, and choose **Stop codespace**. Closing the browser can leave it running until it times out.

## Come back later

Open [Your codespaces](https://github.com/codespaces) and click the existing Codespace's name. Do not create a new Codespace for each class. Saved files persist when you stop and restart the same Codespace, without commits or branches. Variables in memory may be gone; rerun the notebook from the top.

Saving in a Codespace does not update your fork on GitHub. Keep downloaded backups. Stopped Codespaces can eventually be automatically deleted according to your retention settings. Deleting a Codespace removes its unexported work. Download before deleting or before a retention deadline.

## Conserve your allowance

In GitHub, choose your profile picture > **Settings > Codespaces**. Under **Default idle timeout**, enter **5** minutes and save. Check the timeout for an existing Codespace too; default changes may apply only to new Codespaces. See [GitHub's timeout instructions](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces).

Computing and storage allowances depend on account eligibility, machine size, and GitHub billing policies. Check your account's billing and usage settings. Larger machines use the allowance faster, and stopped Codespaces still occupy storage. If access is blocked by an allowance, tell your instructor before adding a paid plan.

A 4 core machine with 16 GB RAM is optional when your account permits it. To change an existing one, use its three dot menu on Your codespaces > **Change machine type**, choose a size, and update. Available sizes can be restricted by account or organization policy. See [GitHub's machine instructions](https://docs.github.com/en/codespaces/customizing-your-codespace/changing-the-machine-type-for-your-codespace).
