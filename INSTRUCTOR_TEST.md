# Instructor testing and publication

## Implementation

The repository contains exactly these ten files:

```text
.devcontainer/devcontainer.json
.vscode/settings.json
data/state_unemployment.csv
notebooks/01_getting_started.ipynb
examples/interactive_window_demo.py
requirements.txt
README.md
STUDENT_GUIDE.md
INSTRUCTOR_TEST.md
.gitignore
```

The [Microsoft Python image](https://github.com/devcontainers/images/tree/main/src/python) uses Python 3.12 on Debian Bookworm. A post creation command installs the pinned requirements, then registers the named kernel. Editor preferences live in workspace settings; the container configuration sets the interpreter path and a container default for Interactive Window Shift+Enter. Minimum host requirements request 2 cores and 8 GB RAM. They do not force a particular machine size. Larger machines are supported, but unnecessary for this lab. No server or background analytical service is launched.

Polars 1.35.2 and Altair 5.5.0 work together directly in local validation. No Arrow conversion, PyArrow, or pandas is needed. Altair's mimetype renderer explicitly supplies the Vega-Lite format used by VS Code. ipykernel installs its own necessary dependencies, including matplotlib-inline, which is an IPython support package rather than a matplotlib analytical workflow. Direct dependencies are pinned; transitive dependencies, the image tag, and marketplace extensions can change. Retest before each term.

The 50 fixed CSV observations are synthetic, manually constructed plausible values for five states from 2014 through 2023. Their provenance and percentage point units are stated in the README, notebook, and script. They must never be cited as BLS estimates.

## Automatic validation completed

Local validation completed on November 13, 2026, with Python 3.12.7 in an isolated temporary environment:

- Both configuration files parse as JSON. Required image, extensions, setup command, and workspace settings were inspected.
- Notebook JSON passes nbformat schema validation. The distributed notebook has empty outputs and execution counts.
- Pinned requirements install successfully. Polars 1.35.2, Altair 5.5.0, and ipykernel 6.30.1 are available.
- The CSV contains 50 unique state/year pairs, five states, ten years, and no missing values.
- All worked notebook code executes in sequence from `notebooks/` and through a real local Jupyter kernel. California has ten rows; the summary has five rows.
- Chart specifications pass Altair schema validation and render to SVG with a temporary validation tool, `vl-convert-python`. Rate labels add `%` without multiplying stored values by 100. Vega-Lite MIME output is generated.
- The optional script parses and its three cells execute in order from the project root. Its path fallback supports a direct course subfolder as the working directory.
- Neither pandas nor PyArrow is installed in the validation environment.
- Exercise cells contain comments only, with no completed Texas solutions. Documentation paths match the ten delivered files.

`nbclient`, `nbformat`, and `vl-convert-python` were used only in the temporary validation environment. They are not student requirements. Executed notebooks and rendered charts were kept outside the repository. Local sandbox restrictions initially blocked kernel ports; the kernel test passed after allowing local execution.

No Docker executable or authenticated live Codespace was available for this test. JSON parsing and configuration inspection do not establish that the image builds or that browser extensions finish installing. The complete browser workflow, 2 core performance, first build time, and five minute ready environment target remain unverified.

## Requested settings

Both instructor supplied settings are preserved exactly in `.vscode/settings.json`.

`interactiveWindow.executeWithShiftEnter: true` also enables Shift+Enter inside the Interactive Window input box, leaving Enter available for a new line. This is separate from executing selected text in a Python editor. The [VS Code declaration](https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/interactive/browser/interactive.contribution.ts) defaults this option to false. It was added after the first browser test identified the missing preference. A subsequent fresh Codespace test reported that workspace configuration alone did not activate the behavior, while checking the User setting did. The devcontainer now also sets this value as a container default through `customizations.vscode.settings`. This is a workaround pending a fresh Codespace test, not a confirmed diagnosis of the underlying VS Code behavior. General editor preferences remain only in workspace settings.

- `jupyter.interactiveWindow.textEditor.executeSelection: true` is declared as a resource scoped Boolean in the [official Jupyter manifest](https://github.com/microsoft/vscode-jupyter/blob/main/package.json), whose retrieved version was 2026.6.1. Its Shift+Enter command is also declared there.
- `interactiveWindow.collapseCellInputCode: "never"` is a VS Code setting rather than a Jupyter namespaced setting. Its recognition in the installed Codespaces release is not yet verified. Do not silently remove or rename it. Check it using the browser procedure below. No replacement is asserted without verifying the deployed release.
- `jupyter.notebookFileRoot: "${fileDirname}"` is declared in that Jupyter manifest and makes the notebook's `../data/` path explicit. The script separately handles root and subfolder working directories.

The fetched upstream manifest is evidence about upstream declarations, not about a locally installed extension. None of the installed Codespaces extension versions or UI effects has been verified yet. Record exact versions during the live test. If the collapse setting is reported as unknown, inspect that VS Code release's default settings and document the supported replacement here before class.

## Browser acceptance checklist

Use a second GitHub account with no prior setup or a volunteer student's account. Do not give them terminal commands. Mark each item only after observing it.

- [ ] Fork from the instructor repository into the tester's personal account. Confirm the heading shows the tester's username.
- [ ] Create a new Codespace from that fork on a 2 core, 8 GB machine. Record browser, OS, machine type, repository revision, and cold build duration.
- [ ] Wait for setup; confirm dependencies install automatically without prompts requiring package commands. Record any trust or authentication prompts.
- [ ] In Extensions, confirm Python, Pylance, and Jupyter install remotely. Record their versions and the VS Code version from Help > About.
- [ ] Open Lab 1. Confirm the named kernel is available. Record whether selecting it is necessary and how long it takes to run the first cell after setup. Target about five minutes from an already built environment.
- [ ] Run every worked cell. Confirm readable Polars tables and a visible California chart with ordered years and percent labels such as 5%, not 500%.
- [ ] Edit a code cell and a Markdown answer, complete the exercises, run them, and save. No terminal or Git operations should be needed.
- [ ] In Explorer, right click the saved notebook and choose Download. Confirm the browser receives one `.ipynb` containing the edited answers and outputs.
- [ ] Open the downloaded file in a local notebook viewer or local VS Code to verify content. This local inspection is an instructor test, not a student software requirement. Check Canvas upload and submission confirmation in a test assignment if available.
- [ ] Stop the Codespace explicitly from github.com/codespaces. Reopen that same Codespace and confirm the saved edits remain. Rerun cells after a kernel restart.
- [ ] Open `examples/interactive_window_demo.py`; choose Run Cell on all three cells. Confirm tables and the chart display in the Interactive Window.
- [ ] In a fresh Codespace, before touching any settings checkbox, confirm Enter inserts a newline and Shift+Enter executes in the Interactive Window input box. Record User, Remote, and Workspace values if this fails. A previously enabled User setting can mask this regression.
- [ ] Confirm code inputs remain visible. In Settings search `@id:interactiveWindow.collapseCellInputCode` and confirm `never` is recognized. Also check `@id:jupyter.interactiveWindow.textEditor.executeSelection` is true at Workspace scope. Inspect settings JSON for unknown setting warnings.
- [ ] Select `california.head()` typed temporarily in the script, press Shift+Enter, and confirm execution in the Interactive Window. Undo the temporary edit.
- [ ] Confirm font size 14, hidden minimap, and word wrapping. Confirm the notebook reads data from its folder and the script works from the Interactive Window's actual starting directory.
- [ ] Set a five minute timeout, verify stopping and reopening, and check account usage visibility. If permitted, optionally repeat on 4 cores and 16 GB RAM.

Saved workspace files persist across stop/start without commits. They are not backed up to the fork. Codespace deletion and retention expiry remove unexported work, so teach downloading backups. GitHub documents [lifecycle behavior](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle) and [allowance considerations](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-included-usage).

## Troubleshooting

| Symptom | Instructor response |
| --- | --- |
| Missing kernel | Wait for setup and extensions to finish. Reload the browser window. Use Select Kernel > Select Another Kernel and inspect Jupyter Kernel or Python Environments for Python 3.12. If absent, inspect the creation log and repair setup; students should not register kernels manually. |
| Dependency installation failed | Inspect the Codespaces creation log for network or package errors. After resolving the cause, use the Command Palette's Codespaces rebuild command. Back up saved work first; do not ask students to pip install packages. |
| Notebook execution failure | Run cells from the top. Check spelling, quotes, and the last error line. Confirm the correct kernel. A restarted kernel forgets variables. |
| Blank Altair output | Run the imports cell, including the mimetype renderer line, then the chart cell. Confirm the Jupyter renderer extension installed as part of Jupyter. Reload the window and rerun. Check output logs; do not switch to pandas. |
| Slow startup | Record cold versus resumed startup separately. Check GitHub status, creation logs, network, and account capacity. Test before class. The first image download is not the five minute ready environment benchmark. |
| CSV not found | The notebook belongs in `notebooks/` and reads `../data/state_unemployment.csv`. Confirm notebookFileRoot is the file directory. The optional script searches the root or parent of its current folder. Do not move files or use a root working directory for the notebook. |
| Codespace belongs to instructor repository | Download any work first. Stop the mistaken Codespace. Fork the instructor repository, check the tester's username in the repository heading, then create from that fork. |
| Usage allowance exceeded | Check current account usage, eligibility, billing policy, and machine size. Stop unused machines and download before deleting unused storage. Arrange another course access option if needed; do not require students to enable paid usage. |
| Saved changes missing | Confirm the student reopened the same Codespace rather than creating a new one. Recover from the downloaded copy if the old Codespace was deleted. Saving alone does not update the GitHub fork. |

## Publish and ask for a test

1. Create an empty GitHub repository named `econ3030-codespaces`. Public visibility makes personal forks straightforward. If private, verify the institution's permissions permit student forks and Codespaces.
2. Using an instructor Git client, publish this folder as the repository root. Include `.devcontainer`, `.vscode`, and `.gitignore`; hidden folders are required. Alternatively use GitHub's Add file > Upload files, then verify hidden configuration files appear in the repository tree. There is no requirement for students to publish or commit anything.
3. Confirm all ten files appear on the default branch with the same structure. No username or instructor Codespaces badge needs replacement.
4. Send the repository URL to another GitHub user and ask them to follow README and STUDENT_GUIDE without instructor intervention. Use the checklist above before assigning this to a class.

Ask the tester to report:

- Whether they forked and launched successfully, with account owner and machine size.
- Cold setup time and time to the first successful cell after setup.
- Any terminal commands, manual installation, unexpected prompts, or unclear instructions.
- Whether tables, both charts, and all exercises worked.
- Whether download, saved answers, Canvas submission, and reopening worked.
- Whether the Interactive Window settings worked, plus browser and extension versions and exact error text for failures.

Do not record account secrets or billing details in the report. Use the test results to compare reliability, time, and student confusion with the existing Posit Cloud workflow. This prototype alone does not establish that Codespaces is the simpler option.
